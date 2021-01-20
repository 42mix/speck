import data
from datetime import datetime
from datetime import timedelta

class Forecatser:
    def __init__(self, data):
        self.data = data

    def forecast_max_temp_c(self, date, accuracy):
        _, date_month, date_day = (int(i) for i in date.split('-'))
        date_year = 2019 - accuracy

        weeks = []

        for i in range(min(accuracy, 10)):
            weeks.append([[], []])

            date_year += 1
            date = datetime(date_year, date_month, date_day)

            for j in range(-6, 1):
                weeks[i][0].append(
                    self.data.raw_data[
                        "{:04d}-{:02d}-{:02d} 00:00:00".format(date.year, date.month, (date + timedelta(days=1)).day)
                    ]
                    ["maxtempC"]
            )

            for j in range(1, 8):
                weeks[i][1].append(
                    self.data.raw_data[
                        "{:04d}-{:02d}-{:02d} 00:00:00".format(date.year, date.month, (date + timedelta(days=1)).day)
                    ]
                    ["maxtempC"]
            )

        for i in range(len(weeks[0][0])):
            print([weeks[j][0][i] for j in range(len(weeks))])

        for i in range(len(weeks[0][1])):
            print([weeks[j][1][i] for j in range(len(weeks))])
