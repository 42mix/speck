"""
Autocompletion Engine for Speck (ACE) that focuses on speed.

Rather than simply looking through an entire file for all values
that may contain a phrase, Ace indexes results into memory and a
cache file for future use. This allows significantly faster
search times.
"""
import json
import pickle

import os
import sys
from pathlib import Path

import atexit

class Ace:
    """
    Wrapper around simple data in the form of a list.

    Ace uses indexing to store queries in memory (and a cache file for future use)
    to return a list of all elements containing the query.
    """
    def __init__(self, /, data=None, file=None, data_id_key=None):
        if not data: # Data must be a list
            if not file:
                raise ValueError("Either data or file must be provided.")

            with open(file, "r", encoding="utf-8") as f: # Doesn't work on windows without the `encoding` flag :/
                try:
                    data = json.loads(f.read()) # This is slow
                except:
                    raise TypeError("Data must be in JSON format.")
        
        self.data = data
        self.file = file
        self.index = {} # We'll try to read the index from a file later on
        self.data_hash = ""
        self.data_id_key = data_id_key # `data_id_key` is only applicable if data is a list of dicts/lists

        atexit.register(self.cache_index) # Destructor

        self.__create_data_hash()
        self.__try_read_index_cache()

    def __create_data_hash(self):
        """Create unique identifier for data for caching."""
        l_ = str(sys.getsizeof(self.data))
        lt = str(len(self.data))
        fn = str(self.file).replace('/', '.').replace('\\', '.') # str cast for None case

        self.data_hash = f"{l_}-{lt}-{fn}"

    def __try_read_index_cache(self):
        """Private method to load index-cache to memory."""
        try:
            with open(f"cache/ace/{self.data_hash}.dat", "rb") as f: 
                self.index = pickle.load(f)
        except:
            return None

    def cache_index(self):
        """Write index from memory to a cache file."""
        Path(f"cache/ace").mkdir(parents=True, exist_ok=True) # Makes cache dir

        with open(f"cache/ace/{self.data_hash}.dat", "wb") as f:
            pickle.dump(self.index, f)

    def complete(self, phrase, truncate=32, force_truncate=None):
        """
        Return a list of all elements in the data set that contains a phrase. Importance
        is given to elements that **begin** with the phrase, and are inserted into the fron of the list.

        Parameters
        ----------
        * phrase - search query. Elements that contain this phrase will be returned.
        * truncate - Maximum length of results. Only `truncate` number of elements will be returned, but all results will be cached.
        * force_truncate - Maximum values to look through. The function will return once `force_truncate` number of elements have been found.
        """
        if phrase in self.index:
            return self.index[phrase]

        completion = []

        for i in self.data:
            if self.data_id_key:
                entry = str(i[self.data_id_key]).lower()
            else:
                entry = str(i).lower()

            if entry.startswith(phrase):
                completion.insert(0, i) # Priority to entries starting with the phrase
            elif phrase in entry:
                completion.append(i)

            if force_truncate and len(completion) > force_truncate:
                break

        self.index[phrase] = completion

        return completion
