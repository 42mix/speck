import json
import requests

import os
from pathlib import Path

from datetime import datetime as dt

class Forecaster:
    def __init__(self, token):
        self.token = token

    @staticmethod
    def __find_cache(city, mode):
        try:
            with open(f"cache/{mode.split('-')[0]}/{city}-{mode}.json", "r") as f:
                return json.load(f.read())
        except:
            return None

    @staticmethod
    def __dump_cache(city, mode, data):
        Forecaster.__cleanup_cache(city, mode)

        Path(f"cache/{mode.split('-')[0]}").mkdir(parents=True, exist_ok=True)
        
        with open(f"cache/{mode.split('-')[0]}/{city}-{mode}.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def __cleanup_cache(city, mode):
        try:
            for i in os.listdir(f"cache/{mode.split('-')[0]}"):
                os.remove(f"cache/{mode.split('-')[0]}/{i}")
        except FileNotFoundError:
            return None

    def current_weather_in(self, city):
        """
        Get current weather conditions in a city.

        Paramters
        ---------
        * **city:** Query parameter based on which data is sent back. It could be following:

                    - Latitude and Longitude (Decimal degree). e.g.:'48.8567,2.3508'
                    - city name e.g.: 'Paris'
                    - US zip e.g.: '10001'
                    - UK postcode e.g: 'SW1'
                    - Canada postal code e.g: 'G2J'
                    - metar:<metar code> e.g: 'metar:EGLL'
                    - iata:<3 digit airport code> e.g: 'iata:DXB'
                    - auto:ip IP lookup e.g: 'auto:ip'
                    - IP address (IPv4 and IPv6 supported) e.g: '100.0.0.1'
        """
        mode = f"forecast-{str(dt.now()).split('.')[0][:-4]}"

        if (n := Forecaster.__find_cache(city, mode)):
            return n

        req = f"http://api.weatherapi.com/v1/current.json?key={self.token}&q={city}"

        response = requests.get(req).json()
        Forecaster.__dump_cache(city, f"forecast-{mode}", response)
        return response

    def forecast_for(self, city, days=7):
        """
        API request to weatherapi.com for future weather forecast.

        Paramters
        ---------
        * **city:** Query parameter based on which data is sent back. It could be following:

                    - Latitude and Longitude (Decimal degree). e.g.:'48.8567,2.3508'
                    - city name e.g.: 'Paris'
                    - US zip e.g.: '10001'
                    - UK postcode e.g: 'SW1'
                    - Canada postal code e.g: 'G2J'
                    - metar:<metar code> e.g: 'metar:EGLL'
                    - iata:<3 digit airport code> e.g: 'iata:DXB'
                    - auto:ip IP lookup e.g: 'auto:ip'
                    - IP address (IPv4 and IPv6 supported) e.g: '100.0.0.1'

        * **days:** Number of days to forecast for. Maximum is 10.
        """
        mode = str(dt.now()).split()[0]

        if (n := Forecaster.__find_cache(city, mode)):
            return n

        req = f"http://api.weatherapi.com/v1/forecast.json?key={self.token}&q={city}&days={min(days, 10)}"

        response = requests.get(req).json()
        Forecaster.__dump_cache(city, f"forecast-{mode}-{days}", response)
        return response["forecast"]["forecastday"]
