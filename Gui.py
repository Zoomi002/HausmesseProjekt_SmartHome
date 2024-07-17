from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data representing the state of the smart home
home_state = {
    'living_room_light': False,
    'bedroom_light': False,
    'kitchen_light': False,
    'temperature': 22,  # Example temperature
    'daylight': 'Bright'  # Example daylight sensor status
}

@app.route('/')
def home():
    return render_template('index.html', state=home_state)

@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    room = request.form['room']
    if room in home_state:
        home_state[room] = not home_state[room]
    return jsonify({room: home_state[room]})

@app.route('/get_sensor_data', methods=['GET'])
def get_sensor_data():
    return jsonify({
        'temperature': home_state['temperature'],
        'daylight': home_state['daylight']
    })

if __name__ == '__main__':
    app.run(debug=True)
