from machine import Pin
from utime import sleep

led = Pin('LED', Pin.OUT)

durata_punto = 0.2
durata_linea = durata_punto * 3
intervallo = durata_punto * 7

durate = {'.' : durata_punto, '-' : durata_linea}

codici = {
    'a' : '.-',   'b' : '-...',  'c' : '-.-.',
    'd' : '-..',  'e' : '.',     'f' : '..-.',
    'g' : '--.',  'h' : '....',  'i' : '..',
    'j' : '.---', 'k' : '-.-',   'l' : '.-..',
    'm' : '--',   'n' : '-.',    'o' : '---',
    'p' : '.--.', 'q' : '--.-',  'r' : '.-.',
    's' : '...',  't' : '-',     'u' : '..-',
    'v' : '...-', 'w' : '.--',   'x' : '-..-',
    'y' : '-.--', 'z' : '--..'
}

def send_pulse(punti_e_linee):
    if punti_e_linee == '.':
        ritardo = durata_punto
    else:
        ritardo = durata_linea
    led.on()
    sleep(ritardo)
    led.off()
    sleep(ritardo)

def send_morse_for(caratttere):
    if carattere == ' ':
        sleep(intervallo)
    else:
        punti_e_linee = codici.get(carattere.lower())
        if punti_e_linee:
            print(carattere + ' ' + punti_e_linee)
            for impulso in punti_e_linee:
                send_pulse(impulso)
            sleep(durata_linea)
        else:
            print('carattere sconosciuto: ' + carattere)
            

while True:
    testo = input('Messaggio: ')
    for carattere in testo:
        send_morse_for(carattere)
