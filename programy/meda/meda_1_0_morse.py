# IA-MEDA-1.0 | Optyczny nadajnik Morse'a
# Raspberry Pi Pico 2 WH | MicroPython (firmware Pico 2 W)
# Departament Badan Kosmicznych Imperium Andromedy
# Program przygotowany 13.11.2026; testy do wykonania przez operatora.
#
# START        - nadaj wiadomosc jeden raz
# TEMPO 12     - ustaw tempo (5-25 WPM)
# STATUS       - pokaz wyniki tej sesji
# STOP         - zakoncz program, wylacz LED
# Ctrl+C       - przerwij transmisje; LED zostanie wylaczona

from machine import Pin
from time import sleep_ms

LED = Pin("LED", Pin.OUT)

WIADOMOSC = "IMPERIUM ANDROMEDY JAKUB I ZIEMIA 10 11 2026"

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "/": "-..-.",
    "?": "..--.."
}

def zakoduj(tekst):
    wyrazy = []
    for wyraz in tekst.upper().split():
        litery = []
        for znak in wyraz:
            if znak not in MORSE:
                raise ValueError("Nieznany znak: " + znak)
            litery.append(MORSE[znak])
        wyrazy.append(" ".join(litery))
    return " / ".join(wyrazy)

def nadaj(tekst, tempo_wpm):
    # Standardowe jednostki Morse'a:
    # kropka 1, kreska 3, przerwa w znaku 1,
    # miedzy literami 3, miedzy wyrazami 7.
    jednostka_ms = 1200 // tempo_wpm
    tekst = " ".join(tekst.upper().split())
    try:
        for i, znak in enumerate(tekst):
            if znak == " ":
                continue
            kod = MORSE[znak]
            for j, impuls in enumerate(kod):
                LED.on()
                sleep_ms(jednostka_ms if impuls == "." else 3 * jednostka_ms)
                LED.off()
                if j < len(kod) - 1:
                    sleep_ms(jednostka_ms)
            if i < len(tekst) - 1:
                nastepny = tekst[i + 1]
                sleep_ms(7 * jednostka_ms if nastepny == " " else 3 * jednostka_ms)
    finally:
        LED.off()

def uruchom():
    tempo = 12
    zakonczone = 0
    potwierdzone = 0
    LED.off()
    print("=== IMPERIUM ANDROMEDY | MEDA 1.0 ===")
    print("Wiadomosc:", WIADOMOSC)
    print("Kod Morse'a:", zakoduj(WIADOMOSC))
    print("Komendy: START | TEMPO 12 | STATUS | STOP")
    try:
        while True:
            polecenie = input("MEDA> ").strip().upper()
            if polecenie == "START":
                print("Nadawanie... obserwuj diode LED.")
                try:
                    nadaj(WIADOMOSC, tempo)
                except KeyboardInterrupt:
                    print("Transmisja przerwana; LED wylaczona.")
                    continue
                zakonczone += 1
                print("Kod zostal wyslany przez program.")
                wynik = input("Czy dioda nadawala prawidlowo? (T/N): ").strip().upper()
                if wynik == "T":
                    potwierdzone += 1
                    print("Sesje potwierdzone przez operatora:", potwierdzone, "/3")
                else:
                    print("Sesja NIEPOTWIERDZONA (brak T).")
                if potwierdzone >= 3:
                    print("TRZY SESJE POTWIERDZONE. Zapisz wynik do dziennika.")
                    break
            elif polecenie.startswith("TEMPO "):
                try:
                    nowe = int(polecenie.split()[1])
                    if 5 <= nowe <= 25:
                        tempo = nowe
                        print("Tempo:", tempo, "WPM")
                    else:
                        print("Podaj liczbe od 5 do 25.")
                except (ValueError, IndexError):
                    print("Uzyj np. TEMPO 10")
            elif polecenie == "STATUS":
                print("Tempo:", tempo, "WPM | zakonczone:", zakonczone,
                      "| potwierdzone:", potwierdzone, "/3")
            elif polecenie == "STOP":
                print("Zatrzymano. LED wylaczona.")
                break
            else:
                print("Nieznana komenda. START | TEMPO 12 | STATUS | STOP")
    except KeyboardInterrupt:
        print("Przerwano przez Ctrl+C.")
    finally:
        LED.off()
        print("MEDA 1.0 — koniec programu; LED wylaczona.")

uruchom()
