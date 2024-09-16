import csv
import requests


# Define the API endpoint
API_URL = 'http://127.0.0.1:5000/api/weather'

def upload_weather_data(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            response = requests.post(API_URL, json=row)
            if response.status_code == 201:
                print(f"Uploaded weather data for station {row['station_id']}")
            else:
                print(f"Failed to upload data for station {row['station_id']}")

if __name__ == '__main__':
    upload_weather_data('weather_data.csv')

