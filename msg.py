import requests
import csv
import time
from twilio.rest import Client

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

account_sid = 'Twillio_Account_SID'
auth_token = 'Twilio_Auth_Token'
twilio_phone_number = 'twilio_phone_number'

send_to = '+919892709032'

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

message=f"The ISS is currently at {lat},{lon}. The location is {location}"

print(message)
twilio_client=Client(account_sid,auth_token)

message = twilio_client.messages.create(
    body=message,
    from_=twilio_phone_number,
    to=send_to
)
print(f"Message sent to {send_to}")