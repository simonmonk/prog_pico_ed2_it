from machine import Pin, PWM
from utime import sleep

led = PWM(Pin(15))

while True:
    luminosita_str = input("luminosita (0-65534):")
    luminosita = int(luminosita_str)
    led.duty_u16(luminosita)
    
