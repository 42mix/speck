import random

from speck.forecaster import Speck

def main():
    with open("token.txt") as f:
        token = f.read()

    fster = Speck(token=token)

    city = fster.find_city("to")[0]
    coords = city["name"]

    print(fster.current(coords))
    _ = fster.forecast(coords)

if __name__ == '__main__':
    main()
