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

class HourlyPoint(BasePoint):
    """Represents weather data at a particular time in some location."""
    def __init__(
        self, location,
        temp_c, feelslike_c,
        condition,
        wind_kph, wind_degree, wind_dir, gust_kph,
        pressure_mb, precip_mm, humidity,
        cloud, is_day, uv,
        last_updated=None, time=None,
        windchill_c=None, heatindex_c=None, dewpoint_c=None,
        will_it_rain=None, will_it_snow=None,
        chance_of_rain=None, chance_of_snow=None,
        vis_km=None,
        *args, **kwargs
        ):
        if isinstance(location, Location):
            self.location = location
        else:
            self.location = Location.from_raw(location)

        self.time = dt.strptime(last_updated if not time else time, "%Y-%m-%d %H:%M") # localtime

        self.temp_c = Cel(temp_c)
        self.feelslike_c = Cel(feelslike_c)

        self.windchill_c = Cel(windchill_c)
        self.heatindex_c = Cel(heatindex_c)
        self.dewpoint_c = Cel(dewpoint_c)

        self.condition = condition

        self.wind_kph = Kph(wind_kph)
        self.gust_kph = Kph(gust_kph)

        self.wind_degree = wind_degree
        self.wind_dir = wind_dir

        self.pressure_mb = Mb(pressure_mb)
        self.precip_mm = Mm(precip_mm)

        self.will_it_rain = will_it_rain
        self.will_it_snow = will_it_snow
        self.chance_of_rain = chance_of_rain
        self.chance_of_snow = chance_of_snow

        self.humidity = humidity
        self.cloud = cloud

        self.is_day = True if is_day else False

        self.uv = uv
        self.vis_km = Km(vis_km)

class DayPoint(BasePoint):
    def __init__(
        self, location,
        maxtemp_c, mintemp_c, avgtemp_c, maxwind_kph, totalprecip_mm, avgvis_km, avghumidity, condition, uv,
        *args, **kwargs
        ):
        if isinstance(location, Location):
            self.location = location
        else:
            self.location = Location.from_raw(location)

        self.maxtemp_c = Cel(maxtemp_c)
        self.mintemp_c = Cel(mintemp_c)
        self.avgtemp_c = Cel(avgtemp_c)

        self.condition = condition
        
        self.maxwind_kph = Kph(maxwind_kph)
        
        self.totalprecip_mm = Mm(totalprecip_mm)
        self.avgvis_km = Km(avgvis_km)
        self.avghumidity = avghumidity

        self.uv = uv

class AstroPoint(BasePoint):
    def __init__(self, location, sunrise, sunset, moonrise, moonset, moon_phase):
        if isinstance(location, Location):
            self.location = location
        else:
            self.location = Location.from_raw(location)

        self.sunrise = sunrise
        self.sunset = sunset

        self.moonrise = moonrise
        self.moonset = moonset

        self.moon_phase = moon_phase

class DailyPoint(BasePoint):
    def __init__(self, location, day, astro, hour):
        if isinstance(location, Location):
            self.location = location
        else:
            self.location = Location.from_raw(location)
        
        # self.date = dt.strptime(date, "%Y-%m-%d %H:%M") # localtime

        if isinstance(day, DayPoint):
            self.day = day
        else:
            self.day = DayPoint.from_raw(location, day)

        self.astro = astro

        self.hour = []

        for i in hour:
            if isinstance(i, HourlyPoint):
                self.hour.append(i)
            else:
                self.hour.append(HourlyPoint.from_raw(location, i))
