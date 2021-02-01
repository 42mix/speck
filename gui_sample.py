"""
Example usage file for SPECK
"""
from speck.forecaster import Forecaster as Fs

with open("token.txt", "r") as f: # Your token is your "password" to be able to use the weatherapi.com API
    token = f.read()              # In this case, it is stored in a file locally for security reasons

fster = Fs(token) # Create a "Forecaster" object.

ln1 = fster.current_weather_in("London") # Returns a dict of the current conditions in the city - Dict
ln2 = fster.forecast_for("London") # Forecasts weather for city - list of dicts

print(ln2[0]["hour"][13]["temp_c"])

print(ln2[0]["day"]["maxtemp_c"])

sum1 = 0

for i in ln2[0]["hour"]:
    sum1 += i["temp_c"]

print("Avg:", sum1 / 24)
