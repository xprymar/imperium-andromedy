# IA–MEDA–OBS/002/2026 — Dziennik MEDA 1.0 (nadawanie Morse'a)

**Departament:** Departament Badań Kosmicznych  
**Data przygotowania:** 13.11.2026  
**Status:** PRZYGOTOWANO DO TESTÓW; BRAK POTWIERDZONYCH EMISJI

## Cel próby
Trzy poprawne, fizycznie zaobserwowane emisje krótkiej odezwy za pomocą wbudowanej diody Raspberry Pi Pico 2 WH. Sterowanie przez komendy START, STOP i TEMPO w powłoce Thonny. Bez nowych zakupów.

**Wiadomość:** `IMPERIUM ANDROMEDY JAKUB I ZIEMIA 10 11 2026`  
**Kod:** `programy/meda/meda_1_0_morse.py`  
**Tempo domyślne:** 12 WPM (możliwość regulacji 5–25 WPM).

## Ewidencja emisji
| Próba | Data i godzina | Tempo WPM | Czy program zakończył transmisję? | Czy LED nadawała prawidłowo? | Ocena operatora |
|---|---|---|---|---|---|
| 1 | — | — | NIEPOTWIERDZONE | NIEPOTWIERDZONE | DO WYKONANIA |
| 2 | — | — | NIEPOTWIERDZONE | NIEPOTWIERDZONE | DO WYKONANIA |
| 3 | — | — | NIEPOTWIERDZONE | NIEPOTWIERDZONE | DO WYKONANIA |

**Warunek zaliczenia:** trzy kolejne lub odrębne emisje, każda zakończona i potwierdzona przez obserwatora. Komunikat programu ani licznik nie stanowią niezależnego potwierdzenia fizycznej transmisji.

**Uwagi techniczne:** program w trybie MicroPython na Pico 2 WH, LED wbudowana; brak zewnętrznej emisji w kierunku nieba. Ctrl+C może przerwać transmisję; polecenie STOP kończy sesję między emisjami.

**Wynik końcowy:** OCZEKUJE NA MELDUNEK OPERATORA.  
**Wydatki Fazy II:** 0,00 zł; nowego sprzętu nie kupowano.
