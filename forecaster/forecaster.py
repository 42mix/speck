import data
from datetime import datetime
from datetime import timedelta

class Forecatser:
    def __init__(self, data):
        self.data = data

    def forecast_max_temp_c(self, date):
        date_year = int(date.split('-')[0])
        date_month = int(date.split('-')[1])
        date_day = int(date.split('-')[2])

        weeks = [[[], []], [[], []], [[], []]]

        for i in weeks:
            date_year -= 1
            date = datetime(date_year, date_month, date_day)

            for j in range(-6, 1):
                i[0].append(self.data.raw_data["{:04d}-{:02d}-{:02d} 00:00:00".format(date.year, date.month, (date - timedelta(days=1)).day)])

            for j in range(1, 8):
                i[1].append(self.data.raw_data["{:04d}-{:02d}-{:02d} 00:00:00".format(date.year, date.month, (date - timedelta(days=1)).day)])

        for i in range(len(weeks[0][0]) - 1):
            print(weeks[0][0][i]["maxtempC"], weeks[1][0][i]["maxtempC"], weeks[2][0][i]["maxtempC"])        

        for i in range(len(weeks[0][1]) - 1):
            print(weeks[0][1][i]["maxtempC"], weeks[1][1][i]["maxtempC"], weeks[2][1][i]["maxtempC"])    