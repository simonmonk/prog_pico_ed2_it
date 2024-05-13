from machine import Pin, PWM
from utime import sleep

bottone_up = Pin(14, Pin.IN, Pin.PULL_UP)
bottone_down = Pin(15, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(16))
servo.freq(50) # impulso ogni 20ms

def set_angle(angolo, impulso_minimo_us=500, impulso_massimo_us=2500):
    us_per_grado = (impulso_massimo_us - impulso_minimo_us) / 180
    impulso_us = us_per_grado * angolo + impulso_minimo_us
    # duty 0 to 1023. A 50Hz, ogni duty_point è 20000/65535 = 0.305 µs/duty_point
    duty = int(impulso_us / 0.305)
    # print("angolo =" + str(angolo) + " impulso_us=" + str(impulso_us) + " duty=" + str(duty))
    print(angolo)
    servo.duty_u16(duty)
    
angolo = 90
set_angle(90)
min_angolo = 10
max_angolo = 160

while True:
    if bottone_up.value() == 0 and angolo <= max_angolo:
        angolo += 1
        set_angle(angolo)
        #print(angolo)
        sleep(0.01)
    elif bottone_down.value() == 0 and angolo > min_angolo:
        angolo -= 1
        set_angle(angolo)
        #print(angolo)
        sleep(0.01)
