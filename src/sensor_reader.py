import Adafruit_DHT
from Adafruit_DHT import raspberry_pi  # импортируем объект платформы для Raspberry Pi

class DHT11Reader:
    def __init__(self, sensor=Adafruit_DHT.DHT11, pin=7):
        self.sensor = sensor
        self.pin = pin  # Физический порт 7. При необходимости измените на BCM-номер

    def read(self):
        # Передаём объект платформы вместо строки
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin, platform=raspberry_pi)
        return temperature, humidity
