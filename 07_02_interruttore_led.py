from machine import Pin
from utime import sleep

interruttore = Pin(10, Pin.IN, Pin.PULL_UP)
led = Pin('LED', Pin.OUT)

while True:
    if interruttore.value() == 0:
        led.on()
        sleep(10)
        led.off()
