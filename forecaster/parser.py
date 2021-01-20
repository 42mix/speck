import csv
import json
            
class Parser:
    @staticmethod
    def parse_csv_file_to_json(file):
        # Flaw: highly specialized
        with open(file, "r") as data:
            reader = list(csv.reader(data, delimiter=","))

            raw_file_name = str(file).split('/')[-1].split('\\')[-1].rstrip('.csv') # \ in f-string

            data_json = {  }
            # Structured as so:
            # {
            #    date: { data }, ...
            # }

            for row in reader[1:]: # Exclude column headers
                data_json[row[0]] = {  }
                for index, col in enumerate(row[1:]):
                    data_json[row[0]][reader[0][index + 1]] = col
                        
            return data_json

    @staticmethod
    def dump_json_to_file(data, file):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_data_from_json_file(file): # really the most important function
        with open(file, "r") as f:
            return json.loads(f.read())
