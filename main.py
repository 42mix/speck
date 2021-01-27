from forecaster.forecaster import Forecaster as Fs

forecaster = Fs("bengaluru")
predicted = forecaster.forecast_overall("2019-12-02", accuracy=8, token_path="token.txt") # arbitrary accuracy

print(predicted)
