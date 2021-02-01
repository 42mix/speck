import json

from tkinter import Tk, Label

class SpeckFrontend:
    def __init__(self, forecaster):
        self.forecaster = forecaster

    def gui_main(self):
        city = input("Enter your location: ")

        current = self.forecaster.current_weather_in(city)
        predicted = self.forecaster.forecast_for(city)

        with open("sample_cur.json", "w") as f:
            json.dump(current, f, indent=4)

        with open("sample_pre.json", "w") as f:
            json.dump(predicted, f, indent=4)

        print("Current temperature in", city, ":",  current['current']['temp_c'])
        print("Current conditions in", city, ":",  current['current']['condition']['text'])
