#!/usr/bin/env python
import Adafruit_DHT as dht
import BlynkLib
import time

BLYNK_AUTH = '0308f332bf72472c9c802ba9d1f5046a'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    h, t = dht.read_retry(dht.DHT22, 4)
    blynk.virtual_write(1, t)
    #print('Current V1 value: {}'.format(h))

@blynk.VIRTUAL_READ(2)
def my_read_handler():
    h, t = dht.read_retry(dht.DHT22, 4)
    blynk.virtual_write(2, h)

# Start Blynk (this call should never return)
blynk.run()