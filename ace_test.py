from speck.ace import Ace

acstance = Ace("cities", file="res/cities.json", data_id_key="name")

res = acstance.complete("to")

for i in res:
    if i['name'] == 'Tokyo':
        print(i)
