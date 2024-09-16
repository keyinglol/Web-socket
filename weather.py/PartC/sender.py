from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime
import json
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/alert')
def alert():
    return render_template('./send_alert.html')

def alert_received():
    print('Alert was received!')

@socketio.on('connect', namespace='/alert')
def handle_connect_alert():
    print('Connected to /alert')

@socketio.on('client_connected', namespace='/alert')
def handle_client_connected_alert(json):
    print('Connection Status: {}'.format(json['connected']))

@socketio.on('alert_sent', namespace='/alert')
def handle_client_send_alert(json_data):
    date_time = json_data['date_time']
    alert_type = json_data['alert_type']
    location = json_data['location']
    description = json_data['description']

    data = {
        'timestamp': str(datetime.now()),
        'date_time': date_time, 
        'alert_type': alert_type,
        'location': location,
        'description': description,
    }

    emit('alert_broadcast', json.dumps(data), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
