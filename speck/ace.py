import json

class Ace:
    """
    Wrapper around simple data in the form of a list.
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
        self.data_id_key = data_id_key # `data_id_key` is only applicable if data is a list of dicts/lists

    def complete(self, phrase, truncate=32):
        """
        Return a list of all elements in the data set that contains a phrase. Importance
        is given to elements that **begin** with the phrase, and are inserted into the fron of the list.

        Parameters
        ----------
        * phrase - search query. Elements that contain this phrase will be returned.
        * truncate - Maximum length of results. Only `truncate` number of elements will be returned, but all results will be cached.
        """
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

        return completion[:truncate]
