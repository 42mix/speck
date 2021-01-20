import forecaster

forecaster.parser.Parser.dump_json_to_file(forecaster.parser.Parser.parse_csv_file_to_json("data/raw/bengaluru.csv"), "data/parsed/bengaluru.json")

data = forecaster.data.Data("data/parsed/bengaluru.json")
i_forecaster = forecaster.forecaster.Forecatser(data)

i_forecaster.forecast_max_temp_c("2019-02-02", accuracy=6)