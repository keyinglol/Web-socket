import csv
import requests

# Define the base API URL
API_URL_TEMPLATE = 'http://127.0.0.1:5000/api/weather/{}'

def update_station_ids(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            old_station_id = row['old_station_id']
            new_station_id = row['new_station_id']
            update_data = {'new_station_id': new_station_id}  # Use 'new_station_id' as key
            
            # Format the URL with the old_station_id
            url = API_URL_TEMPLATE.format(old_station_id)
            
            # Send the PUT request
            response = requests.put(url, json=update_data)
            
            # Check if the update was successful
            if response.status_code == 200:
                print(f"Updated station ID from {old_station_id} to {new_station_id}")
            else:
                print(f"Failed to update station ID {old_station_id}. Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    update_station_ids('station_id_updates.csv')



# import csv
# import requests

# # Define the API endpoint template
# API_URL_TEMPLATE = 'http://127.0.0.1:5000/api/weather/{}'

# def update_station_ids(csv_file):
#     with open(csv_file, mode='r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             old_station_id = row['old_station_id']
#             new_station_id = row['new_station_id']
#             print(f"Processing: old_station_id={old_station_id}, new_station_id={new_station_id}")
            
#             update_data = {'station_id': new_station_id}
#             print(f"Data to send: {update_data}")
            
#             response = requests.put(API_URL_TEMPLATE.format(old_station_id), json=update_data)
#             print(f"HTTP PUT to {API_URL_TEMPLATE.format(old_station_id)} returned status code {response.status_code}")
#             print(f"Response content: {response.text}")

#             if response.status_code == 200:
#                 print(f"Successfully updated station ID from {old_station_id} to {new_station_id}")
#             else:
#                 print(f"Failed to update station ID {old_station_id}. Server responded with: {response.status_code} - {response.text}")

# if __name__ == '__main__':
#     update_station_ids('station_id_updates.csv')
