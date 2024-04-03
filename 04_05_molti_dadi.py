from machine import Pin
from utime import sleep
from random import randint

led = Pin('LED', Pin.OUT)

def lancio_dadi(num_dadi=1):
    totale = 0
    for x in range(1, num_dadi+1):
        totale += randint(1, 6)
    return totale

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    input()
    risultato = lancio_dadi(num_dadi=2)
    print(risultato)
    blink(risultato, 0.2)
    
