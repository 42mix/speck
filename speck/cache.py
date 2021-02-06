import os
import json
import pickle

from pathlib import Path

class Cache:
    def __init__(self, path):
        self.path = path

        Path(path).mkdir(parents=True, exist_ok=True) # Creates cache folder
    
    def read(self, name):
        """Tries to read cache with `name`. Returns `None` if no such file is found."""
        try:
            with open(f"{self.path}/{name}.dat", "rb") as f: # Cache is stored as a dictionary/list
                return pickle.load(f)                        # in a binary file, which can be read later on.
        except:
            return None

    def dump(self, name, data):
        """Writes data to a cache file with `name`. `name` must be kept track of manually."""
        with open(f"{self.path}/{name}.dat", "wb") as f:
            pickle.dump(data, f)

    def cleanup(self, name):
        """Cleans up all cache files with a given `name`. Supports wildcard (*) deletion."""
        els = name.split('*')

        try:
            for i in os.listdir(self.path):
                for n, j in enumerate(els):
                    if not (j in i and (i.index(j) <= i.index(els[min(n, len(name) - 1)]) or j == '')): # NEED to cleanup - written at 4 am
                        break
                else:
                    os.remove(f"{self.path}/{i}")

        except FileNotFoundError:
            return None
