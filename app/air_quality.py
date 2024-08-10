import requests
import os
from dotenv import load_dotenv

load_dotenv()

AIR_QUALITY_API_KEY = os.getenv('AIR_QUALITY_API_KEY')

def get_air_quality(lat, lng):
    response = requests.get(f'<https://api.airqualityapi.com/v1/current?lat={lat}&lng={lng}&key={AIR_QUALITY_API_KEY}>')
    data = response.json()
    return data
