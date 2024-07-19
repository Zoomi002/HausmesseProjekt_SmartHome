import logging
from flask import Flask, render_template, request, jsonify
from logging.handlers import TimedRotatingFileHandler
import threading
import time

app = Flask(__name__)

# Sample data representing the state of the smart home
home_state = {
    'living_room_light': False,
    'bedroom_light': False,
    'kitchen_light': False,
    'temperature': 22,  # Example temperature
    'daylight': 'bright',  # Example daylight sensor status
    'humidity': 45  # Example humidity
}

# Set up logging
logger = logging.getLogger('SmartHomeLogger')
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('logs.log', when='midnight', interval=1, backupCount=7)
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(handler)

def log_sensor_data():
    while True:
        time.sleep(60)  # Log every minute
        sensor_data = f"Temperature: {home_state['temperature']}°C, Daylight: {home_state['daylight']}, Humidity: {home_state['humidity']}%"
        logger.info(f"Sensor Data: {sensor_data}")

# Start logging sensor data in a separate thread
threading.Thread(target=log_sensor_data, daemon=True).start()

@app.route('/')
def home():
    return render_template('index.html', state=home_state)

@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    room = request.form['room']
    if room in home_state:
        home_state[room] = not home_state[room]
        logger.info(f"{room.replace('_', ' ').title()} Light turned {'On' if home_state[room] else 'Off'}")
    return jsonify({room: home_state[room]})

@app.route('/get_sensor_data', methods=['GET'])
def get_sensor_data():
    return jsonify({
        'temperature': home_state['temperature'],
        'daylight': home_state['daylight'],
        'humidity': home_state['humidity']
    })

@app.route('/get_logs', methods=['GET'])
def get_logs():
    with open('logs.log', 'r') as f:
        logs = f.readlines()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
