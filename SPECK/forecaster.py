import json
import requests

import os
from pathlib import Path

from datetime import datetime as dt

class Forecaster:
    def __init__(self, token_path):
        with open(token_path, "r") as f:
            self.token = f.read().rstrip("\n").rstrip(" ")

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
        """Get current weather data for the internal city. Path to openweathermap api key must be provided."""
        mode = f"forecast-{str(dt.now()).split('.')[0][:-4]}"

        if (n := Forecaster.__find_cache(city, mode)):
            return n

        req = f"http://api.weatherapi.com/v1/current.json?key={selftoken}&q={city}"

        response = requests.get(req).json()
        Forecaster.__dump_cache(city, f"forecast-{mode}", response)
        return response

    def forecast_for(self, city, days=7):
        """Get current weather data for the internal city. Path to openweathermap api key must be provided."""
        mode = str(dt.now()).split()[0]

        if (n := Forecaster.__find_cache(city, mode)):
            return n

        req = f"http://api.weatherapi.com/v1/forecast.json?key={self.token}&q={city}&days={max(days, 10)}"

        response = requests.get(req).json()
        Forecaster.__dump_cache(city, f"forecast-{mode}-{days}", response)
        return response
