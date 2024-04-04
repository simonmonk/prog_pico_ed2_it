from machine import Pin
from utime import sleep

interruttore = Pin(10, Pin.IN, Pin.PULL_UP)

while True:
    print(interruttore.value())
    sleep(0.1)
