from forecaster.forecaster import Forecaster as Fs

forecaster = Fs("bengaluru")
forecaster.forecast_overall("2019-02-02", accuracy=8, token_path="token.txt") # arbitrary accuracy
