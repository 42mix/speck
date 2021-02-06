import json
from datetime import datetime as dt

class Location:
    """Represents location data such as coordinates, time zone, region, at a particular time."""
    def __init__(self, lat, lon, name, region=None, country=None, tz_id=None, localtime=None, *args, **kwargs):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.region = region
        self.country = country
        self.tz_id = tz_id
        self.localtime = dt.strptime(localtime, "%Y-%m-%d %H:%M")

    @classmethod
    def from_json(cls, data):
        """Return `Location` object from json converted `weatherapi` response."""
        return cls(**data)

    @classmethod
    def from_raw(cls, data):
        """Return `Location` object from raw `weatherapi` response."""
        return cls(**json.loads(data))
        