from machine import Pin
from utime import sleep
import _thread

interruttore = Pin(10, Pin.IN, Pin.PULL_UP)

def core0():
    x = 0
    while True:
        x += 1
        print(x)
        sleep(1)
        
def core1():
    while True:
        if interruttore.value() == 0:
            print("interruttore premuto")
            sleep(0.1)

_thread.start_new_thread(core1, ( ))
core0()
