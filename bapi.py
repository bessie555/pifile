#!/usr/bin/env python
import Adafruit_DHT as dht
import BlynkLib
import time

BLYNK_AUTH = '0308f332bf72472c9c802ba9d1f5046a'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register Virtual Pins
@blynk.VIRTUAL_READ(1)
def my_read_handler_temp():
    h, t = dht.read_retry(dht.DHT22, 4)
    blynk.virtual_write(1, t)
    print "Read Temp"

@blynk.VIRTUAL_READ(2)
def my_read_handler_humitidy():
    h, t = dht.read_retry(dht.DHT22, 4)
    blynk.virtual_write(2, h)

@blynk.VIRTUAL_READ(3)
def my_read_handler_time():
    blynk.virtual_write(3, time.ticks_ms() // 1000)

@blynk.VIRTUAL_READ(4)
def my_read_handler_test():
    blynk.virtual_write(4, 100)

# Start Blynk (this call should never return)
blynk.run()