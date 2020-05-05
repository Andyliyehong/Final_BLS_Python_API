'''Code required to pull data from the World Bank REST APIs

Attributes:
    BASE_URL (str): The base URL for the PPP World Bank API
'''

import requests
import json

BASE_URL = "https://api.worldbank.org/v2/country/all/indicator/PA.NUS.PPP"

def get_ppp_data(year):
    params = {
        'date': year,
        'per_page': 300,
        'format': 'json'
    }
    
    response = requests.get(BASE_URL, params=params)
    json_data = json.loads(response.text)

    return json_data
