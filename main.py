import forecaster

data = forecaster.data.Data("data/parsed/bengaluru.json")
i_forecaster = forecaster.forecaster.Forecatser(data)

i_forecaster.forecast_max_temp_c("2019-02-02")