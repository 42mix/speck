from datetime import datetime, date as dt
from datetime import timedelta

import requests

from .data import Data

class Forecaster:
    """Forecaster object for a city. Create one for each city."""
    def __init__(self, city, data=None, data_path="data/parsed"):
        self.data = data if data else Data(f"{data_path}/{city}.json")
        self.city = city

    def __historic_fornight_avg(self, date, accuracy, param):
        """Get historic average for `parameter` around a two week range for each year based on accuracy value."""
        weeks = []
        fortnight_avgs = []

        date_year = 2019 - accuracy

        for i in range(min(accuracy, 10)):
            weeks.append([])

            date_year += 1
            date = datetime(date_year, date.month, date.day)

            for j in range(-6, 8):
                weeks[i].append(
                    int(
                        self.data[
                            "{:04d}-{:02d}-{:02d} 00:00:00".format(date.year, date.month, (date + timedelta(days=1)).day)
                        ]
                        [param]
                    )
            )

        for i in weeks:
            fortnight_avgs.append(sum(i) / len(i))
        
        return fortnight_avgs

    def get_current_data(self, token_path):
        """Get current weather data for the internal city. Path to openweathermap api key must be provided."""
        
        with open(token_path, "r") as f:
            token = f.read().rstrip("\n")

        base = "http://api.openweathermap.org/data/2.5/weather?"

        req = f"{base}appid={token}&q={self.city}"

        response = requests.get(req).json()

        if response["cod"] != "404":
            return response
        else:
            raise ValueError("OpenWeatherMap error - 404") # For now

    def forecast_overall(self, date, accuracy, token_path=None):
        """
        Forecast's all weather parameters for given date.

        Parameters
        ----------
        * `date` - Date to forecast weather for. Must be in the format YYYY-MM-DD
        * `accuracy` - Years of historic data to include. Maximum is 10.
        * `token_path` - Path to file containing OpenWeatherMap API key. Ignore if current data is to be ignored.
        """
        ignore_current_data = False

        predicted = {}

        date_year, date_month, date_day = (int(i) for i in date.split('-'))
        date = datetime(date_year, date_month, date_day)

        if abs(date - datetime.now()) > timedelta(days=14): # Current date outside a 2 week range of prediction.
            ignore_current_data = True                      # Using current data will be inaccurate

        if not token_path:
            ignore_current_data = True

        if not ignore_current_data:
            try:
                fornight_avg_max_temp = self.__historic_fornight_avg(date, accuracy, "maxtempC")
                current_max_temp      = self.get_current_data(token_path)["main"]["temp_max"] - 273.15 if token_path else None

                predicted["maxtempC"] = ((sum(fornight_avg_max_temp) / len(fornight_avg_max_temp)) + current_max_temp) / 2

                return predicted
            except ValueError: # OpenWeatherMap not accessible
                pass
            except Exception as e: # Something else
                raise Exception
            
        # Prediction without current data ----------
        fornight_avg_max_temp = self.__historic_fornight_avg(date, accuracy, "maxtempC")

        predicted["maxtempC"] = ((sum(fornight_avg_max_temp) / len(fornight_avg_max_temp)) + fornight_avg_max_temp[-1]) / 2

        return predicted
