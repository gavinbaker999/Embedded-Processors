import dht
from machine import Pin

# Set GPIO pin for sensor
sensor = dht.DHT11(Pin(14))

# Take sensor readings
sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()

# Turn readings into a string to display
readings = ("Temperature: {}°C   Humidity: {}% ".format(temp, hum))
print(readings)
