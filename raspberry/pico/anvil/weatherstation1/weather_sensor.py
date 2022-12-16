import anvil.pico
import uasyncio as a
import dht
from machine import Pin

UPLINK_KEY = "server_ADUOJYAJ7TNWCQAYXHDLRC4S-MQ7DWK5YFSN43Y5V"

# Set GPIO pin for sensor
sensor = dht.DHT11(Pin(14))

# Callable function for sensor readings 
@anvil.pico.callable_async
async def dht11read():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    readings = ("Temperature: {}°C   Humidity: {}% ".format(temp, hum))
    return(readings)

# Connect the Anvil Uplink. In MicroPython, this call will block forever.
anvil.pico.connect(UPLINK_KEY)