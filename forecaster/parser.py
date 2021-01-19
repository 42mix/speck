import csv
import json
            
class Parser:
    @staticmethod
    def parse_file_csv_to_dict(file):
        with open(file, "r") as data:
            reader = list(csv.reader(data, delimiter=","))

            raw_file_name = str(file).split('/')[-1].split('\\')[-1].rstrip('.csv') # \ in f-string

            data_json = {  }
            # Structured as so:
            # {
            #    date: { data }, ...
            # }

            for row in reader[1:]: # Exclude column headers
                if int(row[0].split("-")[0]) > 2015: # Data only from 2016
                    data_json[row[0]] = {  }
                    for index, col in enumerate(row[1:]):
                        data_json[row[0]][reader[0][index + 1]] = col
                        
            return data_json

    @staticmethod
    def dump_json_to_file(data, file):
        with open(file, "w") as f:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_data_from_json_file(file):
        with open(file, "r") as f:
            return json.loads(f.read())
