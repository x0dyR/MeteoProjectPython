import Adafruit_DHT

class DHT11Reader:
    def __init__(self, sensor=Adafruit_DHT.DHT11, pin=7):
        self.sensor = sensor
        self.pin = pin  # Физический порт 7. При необходимости измените на BCM-номер

    def read(self):
        # Принудительно указываем платформу для корректной работы
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin, platform="raspberrypi")
        return temperature, humidity
