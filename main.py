from forecaster.forecaster import Forecaster as Fs

forecaster = Fs("bengaluru")
predicted = forecaster.forecast_overall("2021-01-28", token_path="token.txt") # arbitrary accuracy

print(predicted)
