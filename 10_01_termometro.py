from machine import Pin, ADC
from utime import sleep

sensore_temp = ADC(4)
punti_per_volt = 3.3 / 65535

def leggi_temp_c():
    lettura = sensore_temp.read_u16() * punti_per_volt
    temp_c = 27 - (lettura - 0.706)/0.001721
    return temp_c

while True:
    temp_c = leggi_temp_c()
    print(temp_c)
    sleep(0.5)
