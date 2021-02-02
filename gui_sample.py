"""
Example usage file for SPECK
"""
from speck.forecaster import Forecaster as Fs

with open("token.txt", "r") as f: # Your token is your "password" to be able to use the weatherapi.com API
    token = f.read()              # In this case, it is stored in a file locally for security reasons

fster = Fs(token) # Create a "Forecaster" object.

ln1 = fster.current_weather_in("Ras al-Khaimah") # Returns a dict of the current conditions in the city - Dict
ln2 = fster.forecast_for("Ras al-Khaimah") # Forecasts weather for city - list of dicts

print(ln1["current"]["temp_c"])
print(ln1["current"]["last_updated"])
print(ln1["location"]["name"])
