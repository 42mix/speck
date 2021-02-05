import json
import pickle
import requests

import os

from datetime import datetime as dt

from . import errors
from .cache import Cache

class Forecaster:
    """Primary interface to `weatherapi.com`."""
    BASE = "http://api.weatherapi.com/v1"

    def __init__(self, token):
        self.token = token
        self.cache = Cache("cache")
        
        with open(f"{os.path.abspath(os.path.dirname(__file__))}/cities_p.json", "r", encoding="utf-8") as f:
            self.cities = json.loads(f.read())

    @staticmethod
    def __error_code_to_error(response):
        """
        Convert weatherapi.com provided error code to Error Type.
        
        * Parameter `response` should be the raw weatherapi.com response.
        """
        if "error" in response:
            code = response["error"]["code"]
            message = response["error"]["message"]

            # This monstrosity
            if code == 1002:
                return errors.NoApiKey(message, code)
            elif code == 1003:
                return errors.QueryNotProvided(message, code)
            elif code == 1005:
                return errors.InvalidRequestUrl(message, code)
            elif code == 1006:
                return errors.InvalidLocation(message, code)
            elif code == 2006:
                return errors.InvalidApiKey(message, code)
            elif code == 2007:
                return errors.QuotaExceeded(message, code)
            elif code == 2008:
                return errors.ApiKeyDisabled(message, code)
            elif code == 9999:
                return errors.InternalError(message, code)
            else:
                return errors.WeatherApiError(message, code)

        return None

    def find_city(self, loc):
        return [
            i for i in self.cities if loc in i["name"]
        ]

    def __make_request(self, endpoint, parameters):
        return requests.get(f"{self.BASE}/{endpoint}{parameters}").json()

    def current_weather_in(self, loc):
        """
        Get current weather conditions in a city.

        Paramters
        ---------
        * **loc:** Query parameter based on which data is sent back. It could be following:

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
        mode = f"current-{loc}-now-{str(dt.now())[:15]}"
        
        if (n := self.cache.read(mode)):
            return n

        response = self.__make_request("current.json", f"?key={self.token}&q={loc}")

        if (e := Forecaster.__error_code_to_error(response)):
            raise e

        self.cache.cleanup(mode.split("-now-")[0] + '-now-*')
        self.cache.dump(mode, response) # Writes the response dictionary from the Forecaster to the current cache file

        return response

    def forecast_for(self, loc, days=3):
        """
        API request to weatherapi.com for future weather forecast.

        Paramters
        ---------
        * **loc:** Query parameter based on which data is sent back. It could be following:

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
        mode = f"forecast-{loc}-now-{str(dt.now()).split()[0]}-{days}" # In this case, the mode's type is 'forecast', and
                                                             # and identifier is 'date-days' where date ignores time.
        if (n := self.cache.read(mode)):
            return n

        response = self.__make_request("forecast.json", f"?key={self.token}&q={loc}&days={min(days, 10)}")

        if (e := Forecaster.__error_code_to_error(response)):
            raise e

        self.cache.cleanup(mode.split("-now-")[0] + '-now-*')
        self.cache.dump(mode, response["forecast"]["forecastday"])

        return response["forecast"]["forecastday"]
