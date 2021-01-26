import csv
import json
            
class Parser:
    """Helper class."""

    @staticmethod
    def parse_csv(file_path):
        """Parse CSV weather data from a file to JSON."""
        with open(file_path, "r") as data:
            reader = list(csv.reader(data, delimiter=","))

            data_json = {  }
            # Structured as so:
            # {
            #    date: { data }, ...
            # }

            for row in reader[1:]: # Exclude column headers
                data_json[row[0]] = {  }
                for index, col in enumerate(row[1:]):
                    data_json[row[0]][reader[0][index + 1]] = col

                ## NOTE
                ## Weather data from after 00.00 MAY be excluded to save on file size and processing power
                ## but right now, is included.
                        
            return data_json

    @staticmethod
    def dump_json(data, file_path):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_json(file_path): # really the most important function
        with open(file_path, "r") as f:
            return json.loads(f.read())
