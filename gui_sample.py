import random

from speck.forecaster import Forecaster as Fs

def main():
    with open("token.txt") as f:
        token = f.read()

    fster = Fs(token=token)

    city = random.choice(fster.find_city('to'))
    coords = f"{city['lat']},{city['lng']}"

    print(fster.current_weather_in(coords))
    _ = fster.forecast_for(coords)

if __name__ == '__main__':
    main()
