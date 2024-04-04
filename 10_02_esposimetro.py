from machine import ADC, Pin
from utime import sleep
from math import sqrt

sensore_luce = ADC(28)
lettura_buio = 200
fattore_di_scala = 2.5

def lettura_luce():
    lettura = sensore_luce.read_u16()
    # print(lettura)
    percent = int(sqrt(lettura - lettura_buio) / fattore_di_scala)
    if percent < 0:
        percent = 0
    elif percent > 100:
        percent = 100
    return (percent)

while True:
    livello_luminoso = lettura_luce()
    print(livello_luminoso)
    sleep(0.2)
