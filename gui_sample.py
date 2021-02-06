import random

from speck.speck import Speck

def main():
    with open("token.txt") as f:
        token = f.read()

    fster = Speck(token=token)

    city = fster.find_city("to")[0]
    coords = city["name"]

    cur = fster.current(coords)

    print(cur.last_updated)

if __name__ == '__main__':
    main()
