from forecaster.forecaster import Forecaster as Fs

import json

def format_inaccuracy_score(score): # Make stuff prettier
    if score < 1:
        return f"\033[92m{score}\033[0m"
    elif score < 5:
        return f"\033[93m{score}\033[0m"
    else:
        return f"\033[91m{score}\033[0m"

def test_2019_monthly():
    forecaster = Fs("bengaluru")

    inaccuracy_score = 0

    with open("data/parsed/bengaluru.json", "r") as f:
        data = json.load(f)

    for i in range(1, 13):
        predicted = forecaster.forecast_overall("2019-{:02d}-02".format(i), accuracy=8, token_path="token.txt")["maxtempC"]
        actual = data["2019-{:02d}-02 00:00:00".format(i)]["maxtempC"]

        diff = abs(predicted - int(actual))

        if diff > 5:
            inaccuracy_score += 5
        elif diff > 2:
            inaccuracy_score += 1

    print(f"\033[1m\033[92mMonthly score: {format_inaccuracy_score(inaccuracy_score)}")

def test_2019_daily():
    if input("Warning: daily test may eat up a lot of CPU usage. Continue? [y/n] ").lower() not in ["yes", "y"]:
        return False

    forecaster = Fs("bengaluru")

    inaccuracy_score = 0

    with open("data/parsed/bengaluru.json", "r") as f:
        data = json.load(f)

    for i in range(1, 13):
        for j in range(1, 29):
            predicted = forecaster.forecast_overall("2019-{:02d}-{:02d}".format(i, j), accuracy=8, token_path="token.txt")["maxtempC"]
            actual = data["2019-{:02d}-{:02d} 00:00:00".format(i, j)]["maxtempC"]

            diff = abs(predicted - int(actual))

            if diff > 5:
                inaccuracy_score += 5 / 29
            elif diff > 2:
                inaccuracy_score += 1 / 29

    print(f"\033[1m\033[92mDaily score: {format_inaccuracy_score(inaccuracy_score)}")

if __name__ == "__main__":
    test_2019_monthly()    
    test_2019_daily()
