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
                Parser.load_json(file_name) # try to load parsed weather data
            except:
                self.data = Parser.parse_csv(data, f"data/parsed/{file_name}.json")
                Parser.dump_json(self.data) # save so it doesn't need to be parsed at runtime again

    def __getitem__(self, key):
        return self.data[key]
