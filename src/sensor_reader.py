import Adafruit_DHT

class DHT11Reader:
    def __init__(self, sensor=Adafruit_DHT.DHT11, pin=7):
        self.sensor = sensor
        self.pin = pin  # Физический порт 7; при необходимости замените на корректное значение BCM

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperature, humidity
