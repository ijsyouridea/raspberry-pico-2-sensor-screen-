import time

from dht import DHT11
from machine import Pin

from lcd1602 import LCD

lcd = LCD()

# Initialize DHT11 on GPIO 16 (Pin 21)
sensor = DHT11(Pin("GP16", Pin.OUT))
green = Pin("GP0", Pin.OUT)
red = Pin("GP1", Pin.OUT)
# Allow sensor to boot up
time.sleep(2)


while True:
    try:
        lcd.clear()
        green.on()
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        green.off()
        red.on()
        # print(f"Temperature: {temp}°C   Humidity: {hum}%")
        lcd.write(0, 0, f"Temp: {temp}C")
        lcd.write(0, 1, f"Hum: {hum}%")
        red.off()
    except OSError as e:
        print("Failed to read sensor.", e)

    time.sleep(2)
