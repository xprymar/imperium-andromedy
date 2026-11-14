# MEDA 1.5 — test bezpośredni Pico ↔ telefon (tryb AP)

**Departament Badań Kosmicznych | Status: przygotowano, niepotwierdzono wykonania.**

## Dlaczego ten test?
Pico 2 WH w trybie stacji Wi-Fi (STA) działa z komputera po Ethernecie pod adresem 192.168.18.110, ale przeglądarka telefonu po Wi-Fi zgłosiła ERR_TOO_MANY_RETRIES. Domowy router ARRIS TG6441B może blokować wzajemną komunikację klientów bezprzewodowych. Ten test omija router: Pico wystawia osobną, hasłowaną sieć Wi-Fi.

## Przygotowanie
1. Podłącz Pico do komputera i uruchom Thonny z interpreterem MicroPython (Raspberry Pi Pico).
2. W Thonny utwórz plik `meda_ap_config.py` z dwoma wpisami: `AP_SSID = "MEDA-TEST"` oraz `AP_PASSWORD = "TU_WLASNE_HASLO_MIN_8_ZNAKOW"`. Zastąp hasło własnym, niepublikowanym hasłem.
3. **Zapisz `meda_ap_config.py` w pamięci płytki Pico, nie w publicznym repozytorium.**
4. Pobierz i uruchom przez F5 `programy/meda/meda_1_5_pico_ap_test.py`. Nie zapisuj go jako `main.py`. Zachowujemy oryginalny program MEDA 1.5.
5. W konsoli Thonny odczytaj rzeczywisty adres IP punktu dostępowego (typowo `192.168.4.1`; nie zakładaj go bez sprawdzenia).
6. Na telefonie wybierz Wi-Fi `MEDA-TEST`, wprowadź własne hasło i wybierz **pozostanie przy tej sieci pomimo braku Internetu**. Na czas testu wyłącz mobilne dane i VPN, jeśli telefon przełącza połączenie.
7. W przeglądarce otwórz `http://ADRES_Z_THONNY/`. Sprawdź stronę oraz przyciski WŁĄCZ / WYŁĄCZ LED.
8. Po próbie w Thonny naciśnij Ctrl+C. Punkt Wi-Fi i dioda zostaną wyłączone.

## Wynik do uzupełnienia
| Warunek | Status |
|---|---|
| Pico nadaje własną sieć `MEDA-TEST` | NIEPOTWIERDZONE |
| Telefon łączy się z siecią MEDA | NIEPOTWIERDZONE |
| Panel otwiera się z telefonu | NIEPOTWIERDZONE |
| LED reaguje na przyciski ON/OFF | NIEPOTWIERDZONE |

**Wydatki:** 0,00 zł.

## Interpretacja
Jeśli test w trybie AP działa, a analogiczny panel przez router nadal jest niedostępny, wskazuje to na problem komunikacji lub izolacji w sieci routera, nie na niezdolność Pico do obsługi HTTP na telefonie. Jeśli test nie działa, sprawdzamy ustawienia telefonu, firmware MicroPython, błędy w Shell i zgodność parametrów AP.

**Bezpieczeństwo:** lokalny serwer HTTP nie używa HTTPS ani logowania do panelu. Sieć AP musi mieć mocne hasło WPA2 i być uruchamiana tylko na czas testów. Nie wpisuj do repozytorium haseł Wi-Fi. Jeśli AP pozostaje włączony, każde urządzenie posiadające jego hasło może sterować LED.
