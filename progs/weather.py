# elastic index structure
#      "it": {"type": "float"},
#      "ih": {"type": "float"},
#      "et": {"type": "float"},
#      "eh": {"type": "float"},
#      "etmin": {"type": "float"},
#      "etmax": {"type": "float"},
#      "dt": {"type": "date", "format": "date_time_no_millis" }  

import json
import pyowm
import subprocess
import requests
from time import gmtime, strftime

import pigpio
import DHT22
import time

### get weather data from openweather ###
owm = pyowm.OWM('API_KEY')
endpoint = 'http://localhost:9200/ieth/th'

observation = owm.weather_at_place('Ghaziabad,India')
w = observation.get_weather()
h = w.get_humidity()
t = w.get_temperature('celsius')

data = {}
data['et'] = t['temp']
data['eh'] = h
data['etmin'] = t['temp_min']
data['etmax'] = t['temp_max']

### get weather data from sensor ###

pi = pigpio.pi()
s = DHT22.sensor(pi, 4, 27)
s.trigger()
time.sleep(0.2)

data['it'] = s.temperature()
data['ih'] = s.humidity()

s.cancel()
pi.stop()

### index data ###

data['dt'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())

json_data = json.dumps(data)
print("{}".format(json_data))

# print("{}".format(json_data))

if data['it'] > -10:
    r = requests.post(endpoint, json_data)
    print("{}".format(r.text))
else:
    print("Not logging.")

