import json
from . import parser

class Data:
    def __init__(self, path):
        self.raw_data = parser.Parser.load_data_from_json_file(path)
