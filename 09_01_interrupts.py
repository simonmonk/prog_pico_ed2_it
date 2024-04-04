from machine import Pin
from utime import sleep

bottone = Pin(12, Pin.IN, Pin.PULL_UP)

def handle_button(ignore):
    print('BOTTONE PREMUTO')

bottone.irq(handle_button, Pin.IRQ_RISING)

i = 0

while True:
    i += 1
    print(i)
    sleep(0.2)
