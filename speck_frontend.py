from speck.forecaster import Forecaster as Fs
import speck.errors as els
from speck_gui.speck_gui import SpeckFrontend

with open("token.txt", "r") as f:
    token = f.read()

speck_frontend_inst = SpeckFrontend(Fs(token))
speck_frontend_inst.gui_main()
