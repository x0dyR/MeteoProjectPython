import os
os.environ['ADAFRUIT_DHT_FORCE_RPI'] = '1'  # Принудительно указываем, что работаем на Raspberry Pi

import Adafruit_DHT

class DHT11Reader:
    def __init__(self, sensor=Adafruit_DHT.DHT11, pin=7):
        self.sensor = sensor
        self.pin = pin  # Физический порт 7. Если нужно, замените на BCM-номер

    def read(self):
        # Вызываем read_retry без передачи параметра platform
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temperature, humidity
