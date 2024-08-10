import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY')

def geocode_address(address):
    response = requests.get(f'<https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GEOCODING_API_KEY}>')
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        raise Exception("Geocoding API error")
