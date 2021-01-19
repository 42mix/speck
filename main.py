import csv
import json

def parse_csv_to_json(file):
    with open(file, "r") as data:
        reader = list(csv.reader(data, delimiter=","))

        data_json = {  }
        # Structured as so:
        # {
        #    date: { data }, ...
        # }

        raw_file_name = str(file).split('/')[-1].split('\\')[-1].rstrip('.csv') # \ in f-string

        with open(f"data/parsed/{raw_file_name}.json", "w") as target:
            for row in reader[1:]: # Exclude column headers
                if int(row[0].split("-")[0]) > 2015: # Data only from 2016
                    data_json[row[0]] = {  }

                    for index, col in enumerate(row[1:]):
                        data_json[row[0]][reader[0][index + 1]] = col

            json.dump(data_json, target, indent=4)

parse_csv_to_json("data/raw/bengaluru.csv")
