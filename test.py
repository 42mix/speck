from forecaster.forecaster import Forecaster as Fs
from forecaster.data import Data

import json

def format_inaccuracy_score(score): # Make stuff prettier
    if score < 14:
        return f"\033[92m{score}\033[0m"
    elif score < 31:
        return f"\033[93m{score}\033[0m"
    else:
        return f"\033[91m{score}\033[0m"

def test_daily(city, param, year):
    forecaster = Fs(city)

    inaccuracy_score = 0

    data = Data(f"data/parsed/{city}.json")

    for i in range(1, 13):
        for j in range(1, 29):
            predicted = forecaster.forecast_overall("{:04d}-{:02d}-{:02d}".format(year, i, j), token_path="token.txt")[param]
            actual = data["{:04d}-{:02d}-{:02d} 00:00:00".format(year, i, j)][param]

            diff = abs(predicted - int(actual))

            if diff > 4:
                inaccuracy_score += 1

    print(f"({param}) \033[1m\033[92mDaily score {year}: {format_inaccuracy_score(inaccuracy_score)}")

def test_complete():
    print("\033[1m\033[93m[WARNING] Complete test may use up a lot of CPU\033[0m")
    for i in range(2010, 2020):
        test_daily("delhi", "maxtempC", i)
        test_daily("delhi", "mintempC", i)

if __name__ == "__main__":
    test_complete()
