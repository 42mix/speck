from speck.forecaster import Forecaster as Fs

with open("token.txt", "r") as f:
    token = f.read()

fster = Fs(token)
cur = fster.current_weather_in("Kochi")
fut = fster.forecast_for("Kochi", days=2)

print(cur)
