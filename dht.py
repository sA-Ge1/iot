from flask import Flask, render_template_string
from time import sleep
import random
# from RPLCD.i2c import CharLCD  # Uncomment if LCD is used

# Simulate sensor pin
pin = 4

# Uncomment if using actual LCD hardware
# lcd = CharLCD('PCF8574', 0x27)

app = Flask(__name__)

@app.route('/')
def index():
    # Generate simulated sensor values
    temperature = round(random.uniform(20.0, 35.0), 1)  # Simulated temperature in °C
    humidity = round(random.uniform(30.0, 90.0), 1)     # Simulated humidity in %

    # Uncomment if LCD is connected
    # lcd.clear()
    # lcd.write_string(f'Temp: {temperature}C')
    # lcd.crlf()
    # lcd.write_string(f'Humidity: {humidity}%')

    return render_template_string('''
        <h1>Weather Station (Simulated)</h1>
        <p><strong>Temperature:</strong> {{ temp }}°C</p>
        <p><strong>Humidity:</strong> {{ hum }}%</p>
    ''', temp=temperature, hum=humidity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
