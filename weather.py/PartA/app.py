from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

#initialise db name
DATABASE = 'weather_data.sqlite'

#connect to db
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/weather', methods=['GET'])
def get_all_weather_data():
    conn = get_db_connection()
    weather_data = conn.execute('SELECT * FROM weather_data').fetchall()
    conn.close()
    return jsonify([dict(row) for row in weather_data])

@app.route('/api/weather/<string:station_id>', methods=['GET'])
def get_weather_by_station_id(station_id):
    conn = get_db_connection()
    weather_data = conn.execute('SELECT * FROM weather_data WHERE station_id = ?', (station_id,)).fetchall()
    conn.close()
    if not weather_data:
        return jsonify({'error': 'Station ID not found'}), 404
    return jsonify([dict(row) for row in weather_data])

@app.route('/api/weather', methods=['POST'])
def add_weather_data():
    data = request.get_json()
    station_id = data.get('station_id')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    wind_speed = data.get('wind_speed')
    pressure = data.get('pressure')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not all([station_id, temperature, humidity, wind_speed, pressure]):
        return jsonify({'error': 'All fields are required'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO weather_data (station_id, temperature, humidity, wind_speed, pressure, timestamp) VALUES (?, ?, ?, ?, ?, ?)',
                 (station_id, temperature, humidity, wind_speed, pressure, timestamp))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Weather data added successfully'}), 201

@app.route('/api/weather/<string:station_id>', methods=['PUT'])
def update_weather_data(station_id):
    data = request.get_json()

    # Check if the new station_id is provided
    new_station_id = data.get('new_station_id')
    if not new_station_id:
        return jsonify({'error': 'New station_id is required'}), 400

    # Retrieve existing weather data for the current station_id
    conn = get_db_connection()
    weather_data = conn.execute('SELECT * FROM weather_data WHERE station_id = ?', (station_id,)).fetchone()

    if weather_data is None:
        return jsonify({'error': 'Station ID not found'}), 404

    # Update only the station_id, keeping other data intact
    conn.execute('UPDATE weather_data SET station_id = ? WHERE station_id = ?', (new_station_id, station_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Station ID updated successfully'})


@app.route('/api/weather/<string:station_id>', methods=['DELETE'])
def delete_weather_data(station_id):
    conn = get_db_connection()
    deleted = conn.execute('DELETE FROM weather_data WHERE station_id = ?', (station_id,))
    conn.commit()
    conn.close()
    if deleted.rowcount == 0:
        return jsonify({'error': 'Station ID not found'}), 404
    return jsonify({'message': 'Weather data deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
