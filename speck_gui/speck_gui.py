import json

from tkinter import Tk, Label

class SpeckFrontend:
    def __init__(self, forecaster):
        self.forecaster = forecaster

    def gui_main(self):
        city = input("Enter your location: ")

        predicted = self.forecaster.forecast_for(city)

        with open("sample.json", "w") as f:
            json.dump(predicted, f, indent=4)

        win = Tk()
        win.title("speck")

        lbl = Label(win, text=" ".join([str(i["day"]["maxtemp_c"]) for i in predicted]))
        lbl.grid(column=0, row=0)

        win.mainloop()
