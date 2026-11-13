# IA-MEDA-0.1 | Pierwszy test LED na Raspberry Pi Pico 2 WH
# MicroPython dla modelu Pico 2 W (RPI_PICO2_W)
# Test: 10 kontrolowanych blyskow (0.5 s ON / 0.5 s OFF)
# Nie uruchamiac jako Python na komputerze - interpreter musi byc na Pico.
from machine import Pin
from time import sleep
import sys

LED = Pin("LED", Pin.OUT)
LICZBA_BLYSKOW = 10

print("IMPERIUM ANDROMEDY | MEDA 0.1")
print("Hello MEDA — start testu", LICZBA_BLYSKOW, "blyskow")
print("MicroPython:", sys.version)

try:
    for nr in range(1, LICZBA_BLYSKOW + 1):
        LED.on()
        sleep(0.5)
        LED.off()
        sleep(0.5)
        print("Blysk", nr, "z", LICZBA_BLYSKOW)
    print("KONIEC PROGRAMU: wyslano 10 polecen blysku.")
    print("UWAGA: wynik fizyczny musi potwierdzic obserwator.")
finally:
    LED.off()
