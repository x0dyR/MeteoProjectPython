from flask import Flask
from sensor_reader import DHT11Reader

app = Flask(__name__)
sensor = DHT11Reader()

@app.route("/")
def index():
    temperature, humidity = sensor.read()
    if temperature is None or humidity is None:
        message = "Не удалось получить показания. Попробуйте снова!"
    else:
        message = f"Температура: {temperature}°C, Влажность: {humidity}%"
    return f"<h1>{message}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
