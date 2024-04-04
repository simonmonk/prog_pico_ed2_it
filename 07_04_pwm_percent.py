from machine import Pin, PWM
from utime import sleep

led = PWM(Pin('LED'))

while True:
    luminosita_str = input('luminosita (0-100):')
    luminosita = int(int(luminosita_str) * 65534 / 100)
    led.duty_u16(luminosita)
