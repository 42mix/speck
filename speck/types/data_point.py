from .raw import *

import json
from datetime import datetime as dt

class RealTimePoint:
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
        self.last_updated = dt.strptime(last_updated, "%Y-%m-%d %H-%M-%S-%f") # localtime

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

    @classmethod
    def from_raw(cls, location, data):
        return cls(location, **data)

    @classmethod
    def from_json(cls, location, data):
        return cls(location, **json.loads(data))
