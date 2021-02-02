import json
import pickle

class Ace:
    def __init__(self, name, /, data=None, file=None, data_id_key=None):
        if not data: # Data must be a list
            if not file:
                raise ValueError("Either data or file must be provided.")

            with open(file, "r") as f:
                try:
                    data = json.load(f)
                except:
                    raise TypeError("Data must be in JSON format.")
        
        self.name = name
        self.data = data
        self.index = {} # We'll try to read the index from a file later on
        self.data_id_key = data_id_key # `data_id_key` is only applicable if data is a list of dicts/list

    def complete(self, phrase: str, truncate=32): # Returns list
        if phrase in self.index:
            return self.index[phrase]

        completion = []

        for i in self.data:
            if self.data_id_key:
                if phrase in str(i[self.data_id_key]).lower():
                    completion.append(i)
            else:
                if phrase in str(i).lower():
                    completion.append(i)

        self.index[phrase] = completion

        return completion
