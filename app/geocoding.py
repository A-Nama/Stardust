import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY')

def geocode_address(address):
    # Send a GET request to the Google Maps Geocoding API
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GEOCODING_API_KEY}')
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            raise Exception(f"Geocoding API error: {data['status']}")
    else:
        # Handle HTTP request errors
        raise Exception(f"HTTP request failed with status code {response.status_code}")

# Example usage
# lat, lng = geocode_address('1600 Amphitheatre Parkway, Mountain View, CA')
# print(f'Latitude: {lat}, Longitude: {lng}')
