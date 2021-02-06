import json

class Location:
    def __init__(self, lat, lon, name, region=None, country=None, tz_id=None, localtime_epoch=None, localtime=None):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.region = region
        self.country = country
        self.tz_id = tz_id
        self.localtime_epoch = localtime_epoch
        self.localtime = localtime

    @classmethod
    def from_raw(cls, data):
        return cls(**data)

    @classmethod
    def from_json(cls, data):
        return cls(**json.loads(data))
        