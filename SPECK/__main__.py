from forecaster import Forecaster as Fs

import os
import json

forecaster = Fs(f"{os.getcwd()}/token.txt")
predicted = forecaster.forecast_for("bengaluru")
    