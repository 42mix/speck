from speck.ace import Ace

from datetime import datetime as dt

import json

st = dt.now()
acstance = Ace(file="res/cities_p.json", data_id_key="name")
dif = dt.now() - st

print(f"Insantiation: {dif}")

def index():
    st = dt.now()
    res = acstance.complete("tok")
    initial = dt.now()
    res = acstance.complete("tok")
    final = dt.now()

    return initial - st, final - initial

x_first = index()
x_second = index()

print(str(x_first[0]), str(x_first[1]))
print(str(x_second[0]), str(x_second[1]))
