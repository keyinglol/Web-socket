
import csv
import requests
import http.client
import json

# Define the API endpoint
API_URL = 'http://127.0.0.1:5000/api/weather'
conn = http.client.HTTPConnection("localhost", 5000)

def download_weather_data(csv_file):
    conn.request('GET', '/api/weather')
    response = conn.getresponse()
    if response.status == 200:
        weather = json.loads(response.read())

        # Extract fieldnames from the first weather_data dictionary
        fields = list(weather[0].keys())
        # Exclude 'id' from the fields list
        fields.remove('id')

        with open(csv_file, 'w', newline='') as file:
            fields = [
                'station_id',
                'temperature',
                'humidity',
                'wind_speed',
                'pressure',
                'timestamp',
                ]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for weather_data in weather:
                # Remove 'id' from each weather_data entry
                weather_data.pop('id', None)
                writer.writerow(weather_data)
            print('### Writing completed!')
    else:
        print('### ERROR: {}'.format(response.status))

if __name__ == '__main__':
    download_weather_data('get_weather_data.csv')
