import requests
import csv
import time
def get_location(lat, lon, api_key):
    param = {
        "key": api_key,
        "q": f"{lat}+{lon}"
    }
    url = "https://api.opencagedata.com/geocode/v1/json"
    response = requests.get(url, params=param)
    data = response.json()
    # print (data)
    if data['results']:
        location = data['results'][0]['formatted']
        return location
    else:
        return "Location not found."

api_key = "991559085bf84fd3b0681008610eb690" 


while True :
    resp = requests.get('http://api.open-notify.org/iss-now.json')
    # resp.status_code
    print(resp.status_code)
    print(f"Error:{resp.raise_for_status()}")
    print(resp.json())
    lat = resp.json()['iss_position']['latitude']
    lon = resp.json()['iss_position']['longitude']
    print(lat)
    print(lon)

    location = get_location(lat, lon, api_key)
    print(location)

    # Write data to CSV file
    filename = 'iss_location.csv'
    with open(filename, mode='a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        # writer.writerow(["Latitude", "Longitude", "Location"])
        writer.writerow([lat, lon, location])
    print(f"Data written to '{filename}' successfully.")
    time.sleep(30)
