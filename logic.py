import RPi.GPIO as GPIO
from flask import Flask, render_template, request, jsonify
import threading
import time

app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
LED_PINS = {
    'living_room_light': 23,
    'bedroom_light': 24,
    'kitchen_light': 25,
    'daylight_led': 26,
    'temperature_led': 27,
    'photoelectric_led': 28
}

SENSOR_PINS = {
    'daylight': 17,
    'temperature': 18,
    'photoelectric': 19
}

# Set up LEDs as outputs and sensors as inputs
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

for pin in SENSOR_PINS.values():
    GPIO.setup(pin, GPIO.IN)

# Sample data representing the state of the smart home
home_state = {
    'living_room_light': False,
    'bedroom_light': False,
    'kitchen_light': False,
    'temperature': 22,  # Example temperature
    'daylight': 'bright',  # Example daylight sensor status
    'humidity': 45,  # Example humidity
    'daylight_led': False,
    'temperature_led': False,
    'photoelectric_led': False
}

def update_sensors():
    while True:
        time.sleep(1)
        home_state['daylight'] = 'dark' if GPIO.input(SENSOR_PINS['daylight']) == GPIO.LOW else 'bright'
        home_state['temperature'] = 22  # Replace with actual temperature reading
        home_state['photoelectric'] = 'triggered' if GPIO.input(SENSOR_PINS['photoelectric']) == GPIO.HIGH else 'clear'

        # Control LEDs based on sensor values
        if home_state['daylight'] == 'dark':
            GPIO.output(LED_PINS['daylight_led'], GPIO.HIGH)
            home_state['daylight_led'] = True
        else:
            GPIO.output(LED_PINS['daylight_led'], GPIO.LOW)
            home_state['daylight_led'] = False

        if home_state['temperature'] > 25:  # Example threshold
            GPIO.output(LED_PINS['temperature_led'], GPIO.HIGH)
            home_state['temperature_led'] = True
        else:
            GPIO.output(LED_PINS['temperature_led'], GPIO.LOW)
            home_state['temperature_led'] = False

        if home_state['photoelectric'] == 'triggered':
            GPIO.output(LED_PINS['photoelectric_led'], GPIO.HIGH)
            home_state['photoelectric_led'] = True
        else:
            GPIO.output(LED_PINS['photoelectric_led'], GPIO.LOW)
            home_state['photoelectric_led'] = False

threading.Thread(target=update_sensors, daemon=True).start()

@app.route('/')
def home():
    return render_template('index.html', state=home_state)

@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    room = request.form['room']
    if room in home_state:
        home_state[room] = not home_state[room]
        GPIO.output(LED_PINS[room], GPIO.HIGH if home_state[room] else GPIO.LOW)
    return jsonify({room: home_state[room]})

@app.route('/get_sensor_data', methods=['GET'])
def get_sensor_data():
    return jsonify({
        'temperature': home_state['temperature'],
        'daylight': home_state['daylight'],
        'humidity': home_state['humidity'],
        'daylight_led': home_state['daylight_led'],
        'temperature_led': home_state['temperature_led'],
        'photoelectric_led': home_state['photoelectric_led']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
