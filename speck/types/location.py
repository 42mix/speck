import json
from datetime import datetime as dt

class Location:
    def __init__(self, lat, lon, name, region=None, country=None, tz_id=None, localtime=None, *args, **kwargs):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.region = region
        self.country = country
        self.tz_id = tz_id
        self.localtime = dt.strptime(localtime, "%Y-%m-%d %H:%M")

    @classmethod
    def from_raw(cls, data):
        return cls(**data)

    @classmethod
    def from_json(cls, data):
        return cls(**json.loads(data))
        