import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
AIR_QUALITY_API_KEY = os.getenv('AIR_QUALITY_API_KEY')

def get_air_quality(lat, lng):
    # Send a GET request to the Air Quality API
    response = requests.get(f'https://api.airqualityapi.com/v1/current?lat={lat}&lng={lng}&key={AIR_QUALITY_API_KEY}')
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle errors or unsuccessful requests
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

# Example usage
# lat, lng = 37.7749, -122.4194  # Example coordinates (San Francisco)
# air_quality_data = get_air_quality(lat, lng)
# print(air_quality_data)
