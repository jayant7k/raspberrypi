import sys
# Specify the path where you downloaded the pigpio DHT22.py module
sys.path.append('/home/pi/progs')

import pigpio
# this connects to the pigpio daemon which must be started first
pi = pigpio.pi()

import DHT22
s = DHT22.sensor(pi, 4)
s.trigger()
print('{:3.2f}'.format(s.humidity() / 1.))
print('{:3.2f}'.format(s.temperature() / 1.))
s.cancel()
pi.stop()
