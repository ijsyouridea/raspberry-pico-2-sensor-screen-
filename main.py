import time

from dht import DHT11
from machine import Pin

from lcd1602 import LCD

lcd = LCD()
counter_file = "counter.txt"


def read_counter():
    try:
        with open(counter_file, "r") as file:
            return int(file.read().strip() or "0")
    except (OSError, ValueError):
        return 0


def write_counter(counter):
    with open(counter_file, "w") as file:
        file.write(str(counter))


# Initialize DHT11 on GPIO 16 (Pin 21)
sensor = DHT11(Pin("GP16", Pin.OUT))
green = Pin("GP0", Pin.OUT)
red = Pin("GP1", Pin.OUT)
yellow = Pin("GP12", Pin.OUT)
# Allow sensor to boot up
time.sleep(2)


while True:
    try:
        yellow.on()
        counter = read_counter()
        yellow.off()

        counter += 1

        green.on()
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        green.off()

        yellow.on()
        write_counter(counter)
        yellow.off()

        red.on()
        # print(f"Temperature: {temp}°C   Humidity: {hum}%")
        lcd.clear()
        lcd.write(0, 0, f"Count: {counter}")
        lcd.write(0, 1, f"Temp:{temp}C Hum:{hum}%")
        red.off()

    except OSError as e:
        yellow.off()
        print("Failed to read sensor.", e)

    time.sleep(2)
