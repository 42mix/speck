import json
import pickle
import requests

import os

from datetime import datetime as dt

from . import errors
from . import cache
from . import types

class Speck:
    """A Speck object represents the interface to `weatherapi.com`."""
    
    BASE = "http://api.weatherapi.com/v1"

    def __init__(self, token):
        self.token = token
        self.cache = cache.Cache('cache')
        
        # `os.path.abspath(os.path.dirname(__file__))` is the absolute location of the cities list file
        with open(f'{os.path.abspath(os.path.dirname(__file__))}/cities_p.json', 'r', encoding='utf-8') as f: # This looks for the cities list file
            self.cities = json.loads(f.read())

    @staticmethod
    def __error_code_to_error(response):
        """
        Convert weatherapi.com provided error code to Error Type.
        
        * Parameter `response` should be the raw weatherapi.com response.
        """
        if "error" in response:
            code = response['error']['code']
            message = response['error']['message']

            # These are hardcoded
            if code == 1002:
                return errors.NoApiKey(message, code)
            elif code == 1003:
                return errors.QueryNotProvided(message, code)
            elif code == 1005:
                return errors.InvalidRequestUrl(message, code)
            elif code == 1006:
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

    def __make_request(self, endpoint, parameters):
        """Private method to make a request to `weatherapi.com`."""
        try:
            return requests.get(f"{self.BASE}/{endpoint}{parameters}").json() # Does the acutal request
        except:
            raise errors.InternalError("Unable to fetch data at this time.", 9999)

    def find_city(self, loc):
        """Returns an array of city names and coordinates containing a search pattern."""
        return [
            i for i in self.cities if loc.lower() in i['name'].lower() # Generates a list of city names containing the string `loc`
        ]

    def current(self, loc):
        """
        Get current weather conditions in a location.

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
        
        n = self.cache.read(mode)
        if n:
            # If cache exists (not None), it will be read and an `HourlyPoint` object will be returned
            res = types.HourlyPoint.from_raw(n["location"], n["current"])

            return res

        response = self.__make_request('current.json', f'?key={self.token}&q={loc}')

        e = Speck.__error_code_to_error(response)
        if e:
            raise e # We're not going to handle the error here, so anyone using the function can do it themselves

        res = types.HourlyPoint.from_raw(response["location"], response["current"]) # Creates the `HourlyPoint` object

        self.cache.cleanup(mode.split('-now-')[0] + '-now-*') # Discard any old cache
        self.cache.dump(mode, response) # Writes cache

        return res

        ## The same pattern is followed for all other API methods implemented.

    def forecast(self, loc, days=3):
        """
        Get weather forecast for a location.

        Paramters
        ---------
        * **loc:** Query parameter based on which data is sent back. See docs on method `current` for more info.

        * **days:** Number of days to forecast for. Maximum is 10.
        """
        mode = f"forecast-{loc}-now-{str(dt.now()).split()[0]}-{days}"

        n = self.cache.read(mode)
        if n:
            res = []

            for i in n["forecast"]["forecastday"]:
                res.append(types.DailyPoint(n["location"], i["day"], i["astro"], i["hour"]))

            return res

        response = self.__make_request('forecast.json', f'?key={self.token}&q={loc}&days={min(days, 10)}')

        e = Speck.__error_code_to_error(response)
        if e:
            raise e

        res = []

        for i in response["forecast"]["forecastday"]: # `forecast->forecastday` is a list of all daily forecasts
            res.append(types.DailyPoint(response["location"], i["day"], i["astro"], i["hour"]))

        self.cache.cleanup(mode.split('-now-')[0] + '-now-*')
        self.cache.dump(mode, response)

        return res

    def astro(self, loc):
        """
        Get current astronomy information in a location.

        Paramters
        ---------
        * **loc:** Query parameter based on which data is sent back. See docs on method `current` for more info.
        """
        mode = f"astro-{loc}-now-{str(dt.now()).split()[0]}"

        n = self.cache.read(mode)
        if n:
            res = types.AstroPoint.from_raw(n["location"], n["astronomy"]["astro"])

            return res

        response = self.__make_request('astronomy.json', f'?key={self.token}&q={loc}')

        res = types.AstroPoint.from_raw(response["location"], response["astronomy"]["astro"])

        e = Speck.__error_code_to_error(response)
        if e:
            raise e

        self.cache.cleanup(mode.split('-now-')[0] + '-now-*')
        self.cache.dump(mode, response)

        return res
