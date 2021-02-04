"""
Example usage file for SPECK
"""
from speck.forecaster import Forecaster as Fs
from speck.ace import Ace

import random
import json
from datetime import datetime as dt

def gen_dummy():
    data = []

    for i in range(128 ** 2):
        x = ""

        for i in range(5):
            x += random.choice("abcdefghifjlmnopqrstuvwxyz")

        data.append(x)

    with open("res/dummy.json", "w") as f:
        json.dump(data, f)

def reg_comp(phrases):
    data = []

    with open("res/cities_p.json", "r") as f:
        data = json.load(f)

    for i in phrases:
        st = dt.now()

        completion = []

        for j in data:
            entry = str(j["name"]).lower()

            if entry.startswith(i):
                completion.insert(0, j) # Priority to entries starting with the phrase
            elif i in entry:
                completion.append(j)

        print(f"Prediction time: {dt.now() - st}")

def ace_comp(phrases):
    ace = Ace(file="res/cities_p.json", data_id_key="name")

    for i in phrases:
        st = dt.now()
        e = ace.complete(i)
        print(f"Prediction time: {dt.now() - st}")

def main():
    test_data = []

    with open("res/cities_p.json", "r") as f:
        data = json.load(f)

    for i in range(500): 
        test_data.append(random.choice(data)["name"][:3])

    st = dt.now()
    ace_comp(test_data)
    et = dt.now()
    reg_comp(test_data)
    ft = dt.now()

    print(f"Regular: {ft - et}")
    print(f"Ace: {et - st}")

if __name__ == '__main__':
    main()
