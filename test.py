import tests
import forecaster

data = forecaster.data.Data("data/parsed/bengaluru.json")
i_forecaster = forecaster.forecaster.Forecatser(data)

if not tests.forecast.forecast_max_temp_c(i_forecaster, "2018-01-01 00:00:00"):
    assert(False, "Test Forecast failed.")
else:
    print("Test Forecast passed!")