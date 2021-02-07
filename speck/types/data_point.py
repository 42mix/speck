import json
from datetime import datetime as dt

from .raw import *

class BasePoint:
    """Abstract class representing a single data point."""
    @classmethod
    def from_raw(cls, location, data):
        """Return subclass object from json converted `weatherapi` response."""
        return cls(location, **data)

    @classmethod
    def from_json(cls, location, data):
        """Return subclass object from raw `weatherapi` response."""
        return cls(location, **json.loads(data))

class Location(BasePoint):
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
    def from_raw(cls, data):
        """Return `Location` object from json converted `weatherapi` response."""
        return cls(**data)

    @classmethod
    def from_json(cls, data):
        """Return `Location` object from raw `weatherapi` response."""
        return cls(**json.loads(data))

class RealTimePoint(BasePoint):
    """Represents weather data at a particular time in some location."""
    def __init__(
        self, location,
        last_updated,
        temp_c, feelslike_c,
        condition,
        wind_kph, wind_degree, wind_dir, gust_kph,
        pressure_mb, precip_mm, humidity,
        cloud, is_day,
        uv, *args, **kwargs
        ):
        self.location = location

        self.last_updated = dt.strptime(last_updated, "%Y-%m-%d %H:%M") # localtime

        self.temp_c = Cel(temp_c)
        self.feelslike_c = Cel(feelslike_c)

        self.condition = condition

        self.wind_kph = Kph(wind_kph)
        self.gust_kph = Kph(gust_kph)

        self.wind_degree = wind_degree
        self.wind_dir = wind_dir

        self.pressure_mb = Mb(pressure_mb)
        self.precip_mm = Mm(precip_mm)

        self.humidity = humidity
        self.cloud = cloud

        self.is_day = True if is_day else False

        self.uv = uv
