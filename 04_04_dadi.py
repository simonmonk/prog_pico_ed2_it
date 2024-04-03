from machine import Pin
from utime import sleep
from random import randint

led = Pin('LED', Pin.OUT)

def lancio_dadi():
    return randint(1, 6)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    input()
    risultato = lancio_dadi()
    print(risultato)
    blink(risultato, 0.2)
