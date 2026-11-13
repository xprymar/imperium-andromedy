# IA–MEDA–OBS/003/2026 — MEDA 1.5: panel Wi-Fi

**Departament:** Departament Badań Kosmicznych  
**Data przygotowania:** 13 listopada 2026 r.  
**Status:** PRZYGOTOWANE / NIE PRZETESTOWANO  
**Urządzenie:** Raspberry Pi Pico 2 WH (testy MEDA 0.1 i 1.0 ukończone)  
**Program:** `programy/meda/meda_1_5_panel_wifi.py`  
**Miejsce przechowywania hasła:** tylko lokalny `wifi_local.py` na płytce; nigdy w repozytorium.

## Cel
Połączyć Pico 2 WH z prywatną siecią 2,4 GHz, udostępnić panel HTTP wewnątrz LAN i wykonać z przeglądarki cztery polecenia: LED ON, LED OFF, MORSE i STOP.

## Weryfikacja
| Próba | Kryterium | Wynik |
|---|---|---|
| A — Wi-Fi | Połączenie z siecią, adres IP widoczny w Shell | NIEPOTWIERDZONE |
| B — panel | Otwarcie panelu w przeglądarce pod wskazanym adresem IP | NIEPOTWIERDZONE |
| C — LED ON/OFF | LED reaguje na polecenia z przeglądarki | NIEPOTWIERDZONE |
| D — MORSE/STOP | Dioda nadaje `MEDA ANDROMEDA`; STOP przerywa emisję | NIEPOTWIERDZONE |

**Wydatki:** 0,00 zł. Brak dodatkowych komponentów.  
**Uwagi bezpieczeństwa:** brak HTTPS, panel dostępny dla użytkowników zaufanej sieci lokalnej; nie otwierać portu 80 na świat, nie używać publicznego Wi-Fi; przechowywać hasło w prywatnym pliku.

**Data i godzina testu:** do uzupełnienia  
**Meldunek operatora:** oczekuje  
**Wynik etapu:** OCZEKUJE NA PRÓBĘ

**Ważne:** przygotowanie kodu nie oznacza, że płytka już nawiązała połączenie, panel działa ani że polecenia zostały wykonane.
