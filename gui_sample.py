import random

import json

from speck.speck import Speck
from speck import types

def main():
    with open("token.txt") as f:
        token = f.read()

    fster = Speck(token=token)

    city = fster.find_city("to")[0]
    coords = city["name"]

    cur = fster.current(coords)
    pre = fster.forecast(coords)

if __name__ == '__main__':
    main()
