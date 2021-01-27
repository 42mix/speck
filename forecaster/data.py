import json

from .parser import Parser

class Data:
    """Simple wrapper around json data"""
    def __init__(self, data):
        try:
            self.data = Parser.load_json(data) if type(data) == str else data # JSON
        except:
            file_name = data.split("/")[-1].split("\\")[-1].split(".")[0] # Very clean, yes

            try:
                Parser.load_json(f"data/parsed/{file_name}.json") # try to load parsed weather data
            except:
                self.data = Parser.parse_csv(f"data/raw/{file_name}.csv")
                Parser.dump_json(self.data, f"data/parsed/{file_name}.json") # save so it doesn't need to be parsed at runtime again

    def __getitem__(self, key):
        return self.data[key]
