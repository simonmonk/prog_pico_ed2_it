from machine import ADC, Pin
from utime import sleep

analog = ADC(28)

while True:
    lettura = analog.read_u16()
    print(lettura)
    sleep(0.5)
