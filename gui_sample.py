"""
Example usage file for SPECK
"""
from speck.forecaster import Forecaster as Fs

import json

with open("token.txt", "r") as f: # Your token is your "password" to be able to use the weatherapi.com API
    token = f.read()              # In this case, it is stored in a file locally for security reasons

fster = Fs(token) # Create a "Forecaster" object.

# -------------------------------------
# Current weather
# -------------------------------------

ln = fster.current_weather_in("London")

# Now, we print all available attributes for the current weather

# Note that all these attributes are listed in the
# [WeatherAPI Documentation](https://www.weatherapi.com/docs/)

print("Latest weather update for London was at", ln["current"]["last_updated"]) # Local london time
                                                                                # Key `last_updated_epoch` is also available and shows unix time

if ln["current"]["is_day"]: # can be `0` - night, or `1` - day
    print("Currently day in London")
else:
    print("Currently night in London")

print("Temperature in London", ln["current"]["temp_c"]) # temp_f also available
print("Feels like in London", ln["current"]["feelslike_c"]) # feelslike_f also available

print("Humidity in London", ln["current"]["humidity"]) # Humidity as percentage
print("Cloud cover in London", ln["current"]["cloud"]) # Cloud cover as percentage


print("Conditions in London", ln["current"]["condition"]["text"]) # ["condition"]["icon"] and ["condition"]["code"]
                                                                  # also available, but irrelevant

print("Wind Gust", ln["current"]["gust_kph"]) # gust_mph also available
print("Windspeed in London", ln["current"]["wind_kph"]) # wind_mph also available
print("Wind direction in London", ln["current"]["wind_degree"], "deg") # wind direction in degrees
print("Wind direction in London", ln["current"]["wind_dir"]) # wind direction as shown in compass

print("Pressure in London", ln["current"]["pressure_mb"]) # Air pressure in millibars
print("Pressure in London", ln["current"]["pressure_in"]) # Air pressure in inches

print("Precipitation in London", ln["current"]["precip_mm"]) # Precipitation in millimeters
print("Precipitation in London", ln["current"]["precip_in"]) # Precipitation in inches

print("Visibility in London", ln["current"]["vis_km"]) # vis_miles also available
print("UV index in London", ln["current"]["uv"]) # UV index

# -------------------------------------
# Forecast weather
# -------------------------------------

lp = fster.forecast_for("London", days=7)

