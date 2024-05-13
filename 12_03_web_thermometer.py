workfrom microdot import Microdot
from machine import ADC
import mm_wlan

ssid = 'Network'
password = 'password'

temp_sensore = ADC(4)
punti_per_volt = 3.3 / 65535

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

def read_temp_c():
    lettura = temp_sensore.read_u16() * punti_per_volt
    temp_c = 27 - (lettura - 0.706)/0.001721
    return temp_c

@app.route('/')
def index(request):
    return 'Temperatura: ' + str(read_temp_c())

app.run(port=80)
