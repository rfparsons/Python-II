'''File: api.py
Author: Bobby Parsons
Date: 10/19/21

Prints data from the API of thebluealliance.com
'''

import requests
import time

CRAFT = 'ISS'
FLYOVER_LATITUDE = "34.0522"
FLYOVER_LONGITUDE = "118.2437"


response = requests.get("http://api.open-notify.org/iss-now.json")
location = response.json()

response = requests.get("http://api.open-notify.org/astros.json")
residents = response.json()

response = requests.get('http://api.open-notify.org/iss-pass.json?lat=' + FLYOVER_LATITUDE + '&lon=' + FLYOVER_LONGITUDE)
flyovers = response.json()

print("Current location: " + location["iss_position"]["latitude"] + ", " + location["iss_position"]["longitude"])

print("Current residents: ")

for person in residents['people']:
    if (person['craft'] == CRAFT):  # Only get the ones on the ISS
        print(person['name'])

print("Next 5 times the ISS flies over Ankeny: ")

for flyover in flyovers['response']:
    print(flyover['risetime'])
    print(time.ctime(int(flyover['risetime'])))