# IA-MEDA-1.5-DIAG | Diagnostyka bez routera: Pico 2 WH jako punkt Wi-Fi
# Ta wersja nie laczy sie z domowym routerem i nie zmienia jego ustawien.
# Uruchom przez F5 w Thonny. NIE zapisuj jako main.py.
# Haslo i nazwa sieci sa przechowywane w prywatnym pliku NA PICO:
#     meda_ap_config.py (nie przesylaj go do GitHuba)
#     AP_SSID = "MEDA-TEST"
#     AP_PASSWORD = "wlasne_silne_haslo"
# Minimum 8 znakow w hasle.
#
# STATUS: PROGRAM PRZYGOTOWANY. DZIALANIA NA SPRZECIE NIEPOTWIERDZONE.

from machine import Pin
import network
import socket
import time
from meda_ap_config import AP_SSID, AP_PASSWORD

if not isinstance(AP_SSID, str) or not (1 <= len(AP_SSID) <= 32):
    raise ValueError("AP_SSID musi miec 1-32 znaki")
if not isinstance(AP_PASSWORD, str) or not (8 <= len(AP_PASSWORD) <= 63):
    raise ValueError("AP_PASSWORD musi miec 8-63 znaki")

led = Pin("LED", Pin.OUT)
led.off()

ap = None
server = None
stan_led = False

def strona(ip):
    stan = "WLACZONA" if stan_led else "WYLACZONA"
    return ("""<!doctype html><html lang="pl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>MEDA — test sieci bezposredniej</title>
<style>body{font-family:Arial;background:#101526;color:#eee;
padding:20px;max-width:460px;margin:25px auto}
a{display:block;background:#445cba;color:white;padding:18px;
margin:14px 0;border-radius:12px;text-align:center;text-decoration:none}
p{line-height:1.6}</style></head><body>
<h1>MEDA 1.5 — TEST AP</h1>
<p>Polaczenie bezposrednie telefon ↔ Pico</p>
<p>IP: """ + ip + """<br>LED: """ + stan + """</p>
<a href="/on">WLACZ LED</a>
<a href="/off">WYLACZ LED</a>
<p>Ta strona dziala tylko w tymczasowej sieci Wi-Fi tworzonej przez Pico.</p>
</body></html>""").encode("utf-8")

try:
    # Domowe Wi-Fi jest tu celowo wylaczone.
    sta = network.WLAN(network.STA_IF)
    sta.active(False)
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    # 3 = WPA2-PSK w obslugiwanym sterowniku AP.
    ap.config(ssid=AP_SSID, security=3, key=AP_PASSWORD)
    ap.active(True)
    for _ in range(30):
        if ap.active():
            break
        time.sleep_ms(100)
    if not ap.active():
        raise RuntimeError("Nie mozna uruchomic punktu Wi-Fi Pico")

    ip = ap.ifconfig()[0]
    print("================================")
    print("MEDA AP — PUNKT WLASNEJ SIECI")
    print("Polacz telefon z siecia:", AP_SSID)
    print("Haslo: z prywatnego pliku meda_ap_config.py")
    print("Po polaczeniu potwierdz 'Pozostan w tej sieci' (brak Internetu).")
    print("Otworz na telefonie: http://" + ip + "/")
    print("Ctrl+C: zatrzymaj serwer i wylacz Wi-Fi")
    print("================================")

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 80))
    server.listen(2)
    server.settimeout(0.4)

    while True:
        try:
            client, addr = server.accept()
        except OSError:
            continue
        try:
            client.settimeout(2)
            request = client.recv(1024)
            if not request:
                continue
            parts = request.split(b"\r\n", 1)[0].split()
            path = parts[1] if len(parts) >= 2 else b"/"
            print("Zadanie telefonu:", path)
            if path == b"/on":
                led.on()
                stan_led = True
            elif path == b"/off":
                led.off()
                stan_led = False

            body = strona(ip)
            header = ("HTTP/1.1 200 OK\r\n"
                      "Content-Type: text/html; charset=utf-8\r\n"
                      "Cache-Control: no-store\r\n"
                      "Connection: close\r\n"
                      "Content-Length: " + str(len(body)) + "\r\n\r\n")
            client.sendall(header.encode("utf-8") + body)
        except OSError as exc:
            print("Blad klienta:", exc)
        finally:
            client.close()
except KeyboardInterrupt:
    print("Zatrzymano test przez Ctrl+C")
finally:
    led.off()
    if server is not None:
        server.close()
    if ap is not None:
        ap.active(False)
    print("MEDA AP — wylaczono LED i punkt Wi-Fi")
