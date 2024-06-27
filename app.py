import requests
import csv
import time
from datetime import datetime  # Import the datetime class

def get_location(lat, lon, api_key):
    param = {
        "key": api_key,
        "q": f"{lat}+{lon}"
    }
    url = "https://api.opencagedata.com/geocode/v1/json"
    response = requests.get(url, params=param)
    data = response.json()
    if data['results']:
        location = data['results'][0]['formatted']
        return location
    else:
        return "Location not found."

api_key = "991559085bf84fd3b0681008610eb690"

while True:
    resp = requests.get('http://api.open-notify.org/iss-now.json')
    print(resp.status_code)
    print(f"Error: {resp.raise_for_status()}")
    print(resp.json())
    lat = resp.json()['iss_position']['latitude']
    lon = resp.json()['iss_position']['longitude']
    print(lat)
    print(lon)

    location = get_location(lat, lon, api_key)

    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Write data to CSV file including the current date and time
    filename = 'iss_location.csv'
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Append the current date and time to the data being written
        writer.writerow([lat, lon, location, current_time])

    print(f"Data written to '{filename}' successfully.")
    time.sleep(20)