import json
import pickle
import requests

import os
from pathlib import Path

from datetime import datetime as dt

from . import ace
from . import errors

class Forecaster:
    """Primary interface to `weatherapi.com`."""
    def __init__(self, token):
        self.token = token
        self.ace = ace.Ace(file="res/cities_p.json", data_id_key="name")

    @staticmethod
    def __find_cache(loc, mode): # Cache to reduce API requests
        """
        Look for cache for a specific type of request.

        * Parameter `mode` should be of the format: `type-identifier`, where `type` is
          the type of request (typically something like 'forecast' for forecasted data and 'current' for current data),
          and `identifier` is a string uniquely used to identify a specific dataset, typically a timestamp rounded up.
        """
        try:
            with open(f"cache/{mode.split('-')[0]}/{loc}-{mode}.dat", "rb") as f: # Cache is stored as a dictionary/list
                return pickle.load(f)                                              # in a binary file, which can be read later on.
        except:
            return None

    @staticmethod
    def __dump_cache(loc, mode, data):
        """
        Write data to cache and cleanup old cache.

        * Parameter `mode` should be of the format: `type-identifier`, where `type` is
          the type of request (typically something like 'forecast' for forecasted data and 'current' for current data),
          and `identifier` is a string uniquely used to identify a specific dataset, typically a timestamp rounded up.
        * Parameter `data` is the data to be cached and must be provided.
        """
        Forecaster.__cleanup_cache(loc, mode) # Just to save space

        Path(f"cache/{mode.split('-')[0]}").mkdir(parents=True, exist_ok=True) # Creates cache folder
        
        with open(f"cache/{mode.split('-')[0]}/{loc}-{mode}.dat", "wb") as f: # Uses mode's type as parent dir
            pickle.dump(data, f)

    @staticmethod
    def __cleanup_cache(loc, mode):
        """
        Cleanup old cache, if exists.

        * Parameter `mode` should be of the format: `type-identifier`, where `type` is
          the type of request (typically something like 'forecast' for forecasted data and 'current' for current data),
          and `identifier` is a string uniquely used to identify a specific dataset, typically a timestamp rounded up.
        """
        try:
            for i in os.listdir(f"cache/{mode.split('-')[0]}"): # Lists all the files in the current folder/dir
                if i.startswith(loc): # cache file will **always** begin with location
                    os.remove(f"cache/{mode.split('-')[0]}/{i}")    # Uses mode's type as parent dir
        except FileNotFoundError:
            return None

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

    @staticmethod
    def __make_request(endpoint, parameters):
        base_url = "http://api.weatherapi.com/v1"

        if endpoint[0] != '/':
            raise errors.InvalidRequestUrl("Endpoint must begin with a `/`")

        return requests.get(f"{base_url}{endpoint}{parameters}").json()

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
        mode = f"current-{str(dt.now())[:15]}" # In this case, the mode's type is 'forecast', and
                                              # and identifier is 'date' where date is rounded up to the 10th minute.
        if (n := Forecaster.__find_cache(loc, mode)):
            return n

        response = Forecaster.__make_request("/current.json", f"?key={self.token}&q={loc}")

        if (e := Forecaster.__error_code_to_error(response)):
            raise e

        Forecaster.__dump_cache(loc, mode, response) # Writes the response dictionary from the Forecaster to the current cache file

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
        mode = f"forecast-{str(dt.now()).split()[0]}-{days}" # In this case, the mode's type is 'forecast', and
                                                             # and identifier is 'date-days' where date ignores time.
        if (n := Forecaster.__find_cache(loc, mode)):
            return n

        response = Forecaster.__make_request("/forecast.json", f"?key={self.token}&q={loc}&days={min(days, 10)}")

        if (e := Forecaster.__error_code_to_error(response)):
            raise e

        Forecaster.__dump_cache(loc, mode, response["forecast"]["forecastday"]) # Writes the response dictionary from the Forecaster to the current cache file

        return response["forecast"]["forecastday"]
