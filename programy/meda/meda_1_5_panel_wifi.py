# IA-MEDA-1.5 | Lokalny panel WWW przez Wi-Fi
# Raspberry Pi Pico 2 WH, MicroPython dla Pico 2 W
# Departament Badan Kosmicznych | 13.11.2026
#
# UWAGA: wymagany prywatny plik wifi_local.py NA PLYTCE PICO:
# SSID = "nazwa_sieci_2_4_GHz"
# PASSWORD = "wlasne_haslo_wifi"
#
# Program nie uruchamia sie automatycznie: uruchom go przez F5 w Thonny.
# Tylko do zaufanej sieci lokalnej. Brak HTTPS i kont uzytkownikow.
# Sterowanie przez HTTP w sieci lokalnej; NIE przekierowywac portu 80.
# Test fizyczny NIE jest jeszcze wykonany.

import network
import socket
import time
from machine import Pin

from wifi_local import SSID, PASSWORD

LED = Pin("LED", Pin.OUT)
LED.off()

# Krotki test kodu Morse'a z panelu Wi-Fi (bez dodatkowych czesci).
TEKST = "MEDA ANDROMEDA"
TEMPO_WPM = 12
MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
    "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}

TRYB = "WYLACZONA"
KROKI = []
POZYCJA = 0
TERMIN = 0
LICZNIK_MORSE = 0

HTML = """<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store">
<title>Imperium Andromedy | MEDA 1.5</title>
<style>
body{font-family:Arial,sans-serif;max-width:480px;margin:35px auto;
background:#101526;color:#eef2ff;padding:16px}
h1{font-size:25px}p{line-height:1.5}
.panel{padding:18px;background:#222b41;border-radius:14px;margin:18px 0}
a{display:block;text-align:center;padding:16px;margin:12px 0;
background:#566be5;color:white;text-decoration:none;
border-radius:10px;font-weight:bold}
.stop{background:#c54c4c}
small{color:#c5cce4}
</style></head><body>
<h1>MEDA 1.5</h1><p>Imperium Andromedy | Panel lokalny</p>
<div class="panel"><strong>Stan LED:</strong> @STATUS@<br>
<strong>IP urzadzenia:</strong> @IP@<br>
<strong>Ukonczone emisje Morse'a:</strong> @COUNT@</div>
<a href="/on">WLACZ LED</a>
<a href="/off">WYLACZ LED</a>
<a href="/morse">NADAJ MORSE: MEDA ANDROMEDA</a>
<a class="stop" href="/stop">STOP / PRZERWIJ</a>
<small>Po kliknieciu przycisku strona sie odswiezy. Jezeli trwa nadawanie,
mozesz je przerwac przez STOP. Siec lokalna, bez Internetu i HTTPS.
Nalezy korzystac tylko z zaufanego Wi-Fi.</small>
</body></html>"""

def kroki_morse(tekst, wpm):
    jednostka = 1200 // wpm
    wynik = []
    wyrazy = tekst.upper().split()
    for nr_w, wyraz in enumerate(wyrazy):
        for nr_z, znak in enumerate(wyraz):
            kod = MORSE[znak]
            for nr_s, symbol in enumerate(kod):
                wynik.append((1, jednostka if symbol == "." else 3 * jednostka))
                if nr_s < len(kod) - 1:
                    wynik.append((0, jednostka))
            if nr_z < len(wyraz) - 1:
                wynik.append((0, 3 * jednostka))
        if nr_w < len(wyrazy) - 1:
            wynik.append((0, 7 * jednostka))
    return wynik

def przerwij():
    global TRYB, KROKI, POZYCJA
    KROKI = []
    POZYCJA = 0
    TRYB = "WYLACZONA"
    LED.off()

def rozpocznij_morse():
    global TRYB, KROKI, POZYCJA, TERMIN
    przerwij()
    KROKI = kroki_morse(TEKST, TEMPO_WPM)
    POZYCJA = 0
    TERMIN = time.ticks_ms()
    TRYB = "NADAWANIE MORSE"
    print("MEDA: start Morse'a:", TEKST)

def tykniecie():
    global TRYB, POZYCJA, TERMIN, LICZNIK_MORSE
    if TRYB != "NADAWANIE MORSE":
        return
    teraz = time.ticks_ms()
    if time.ticks_diff(teraz, TERMIN) < 0:
        return
    if POZYCJA < len(KROKI):
        stan, czas_ms = KROKI[POZYCJA]
        LED.value(stan)
        POZYCJA += 1
        TERMIN = time.ticks_add(TERMIN, czas_ms)
    else:
        LED.off()
        TRYB = "WYLACZONA"
        LICZNIK_MORSE += 1
        print("MEDA: koniec Morse'a; licznik:", LICZNIK_MORSE)

def polacz():
    if not SSID or not PASSWORD:
        raise ValueError("Ustaw SSID i PASSWORD w prywatnym wifi_local.py")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("MEDA: laczenie z siecia Wi-Fi 2,4 GHz...")
    wlan.connect(SSID, PASSWORD)
    for _ in range(90):
        if wlan.isconnected():
            break
        time.sleep_ms(500)
    if not wlan.isconnected():
        wlan.active(False)
        raise RuntimeError("Brak Wi-Fi. Sprawdz SSID, haslo, pasmo 2,4 GHz.")
    return wlan

def strona(ip):
    tresc = HTML.replace("@STATUS@", TRYB)
    tresc = tresc.replace("@IP@", ip)
    return tresc.replace("@COUNT@", str(LICZNIK_MORSE)).encode("utf-8")

def obsluz_polaczenie(client, ip):
    global TRYB
    client.settimeout(1.5)
    req = client.recv(1024)
    if not req:
        return
    pierwsza = req.split(b"\r\n", 1)[0].split(b" ")
    sciezka = pierwsza[1] if len(pierwsza) > 1 else b"/"
    if sciezka == b"/on":
        przerwij()
        LED.on()
        TRYB = "WLACZONA"
        print("WWW: LED ON")
    elif sciezka == b"/off" or sciezka == b"/stop":
        przerwij()
        print("WWW: LED OFF / STOP")
    elif sciezka == b"/morse":
        rozpocznij_morse()
        print("WWW: MORSE")
    elif sciezka != b"/" and sciezka != b"/favicon.ico":
        # Nie wykonujemy nieznanych polecen.
        pass
    body = strona(ip)
    header = ("HTTP/1.1 200 OK\r\n"
              "Content-Type: text/html; charset=utf-8\r\n"
              "Cache-Control: no-store\r\n"
              "Content-Length: " + str(len(body)) + "\r\n"
              "Connection: close\r\n\r\n").encode("utf-8")
    client.sendall(header + body)

def uruchom():
    wlan = None
    serwer = None
    try:
        wlan = polacz()
        ip = wlan.ifconfig()[0]
        serwer = socket.socket()
        serwer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serwer.bind(("0.0.0.0", 80))
        serwer.listen(2)
        serwer.settimeout(0.05)
        print("=================================")
        print("MEDA 1.5 — PANEL GOTOWY")
        print("Otworz na urzadzeniu w tej samej sieci:")
        print("http://" + ip + "/")
        print("Zatrzymanie serwera: Ctrl+C w Thonny")
        print("=================================")
        while True:
            tykniecie()
            try:
                client, _ = serwer.accept()
            except OSError:
                continue
            try:
                obsluz_polaczenie(client, ip)
            except OSError as exc:
                print("Blad polaczenia HTTP:", exc)
            finally:
                client.close()
    except KeyboardInterrupt:
        print("MEDA 1.5 zatrzymana.")
    finally:
        przerwij()
        if serwer is not None:
            serwer.close()
        if wlan is not None:
            wlan.active(False)
        print("LED i Wi-Fi wylaczone. Koniec.")

uruchom()
