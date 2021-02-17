import os

from speck.speck import Speck
from speck.errors import *

from misc import calculator

from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from datetime import datetime as dt
from datetime import timedelta as td

# print(os.environ)

class SpeckFrontend:
    def __init__(self):
        ##     Application Flow
        ##     ----------------
        ##
        ##      Welcome Screen
        ##  Username and Password Entry
        ##      Login Button
        ##             ↓
        ##    Location Entry Screen
        ##       Location Entry
        ##        "GET" Button
        ##             ↓
        ##      Type Entry Screen                       ---> (Doesn't change state)
        ##  Current, Forecast, Astro Buttons
        ##             ↓
        ##     Unique TopLevels

        # Initialize

        self.root = None

        self.main_canvas = None

        self.welcome_username_entry = None
        self.welcome_password_entry = None
        self.welcome_login_button = None

        self.location_input_entry = None
        self.location_input_button = None

        self.current_search_button = None
        self.forecast_search_button = None
        self.astronomy_search_button = None
        self.caclulator_init_button = None

        self.bg = None

        with open("token.txt", "r") as f:
            self.speck = Speck(f.read().rstrip())

    def welcome(self):
        """Implementation for Welcome screen."""
        # Step 1 in application flow
        if ('SPECK_DEV' not in os.environ and \
            (self.welcome_username_entry.get() == 'username' or \
            self.welcome_username_entry.get() == '' or \
            self.welcome_password_entry.get() == 'password' or \
            self.welcome_password_entry.get() == '')):

            response = messagebox.showwarning("ERROR","ENTER USERNAME AND PASSWORD")

        elif ('SPECK_DEV' not in os.environ and \
            (self.welcome_username_entry.get() != '11C' or \
            self.welcome_password_entry.get() != '11c2021')):
             
            response = messagebox.showwarning("ERROR","ENTER CORRECT USERNAME AND PASSWORD")

        else:
            self.welcome_username_entry.destroy()
            self.welcome_password_entry.destroy()
            self.welcome_login_button.destroy()
            self.main_canvas.destroy()

            self.location_entry() # Move onto step 2

    def location_entry(self):
        """Implementation for Location Entry Screen."""
        # Step 2 in application flow

        self.main_canvas = Canvas(self.root, width=323, height=576, bd=0, highlightthickness=0) # reset canvas
        self.main_canvas.pack(fill="both", expand=True)
        self.main_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.location_entry = Entry(self.root, font=("Helvetica", 22), width=15, fg="dark blue", bd=0)
        self.location_entry.insert(0, "Enter Location")

        def clear_location_entry():
            if self.location_entry.get() == "Enter Location":
                self.location_entry.delete(0, END)

        self.location_entry.bind("<Button-1>", lambda e: clear_location_entry())

        location_entry_window = self.main_canvas.create_window(38, 340, anchor='nw', window=self.location_entry)

        self.location_input_button = Button(self.root, text='Continue', font=('Helvetica', 20), width=15, fg='dark blue', bd=0, bg="white", command=self.type_entry)
        location_input_button_win = self.main_canvas.create_window(36, 420, anchor='nw', window=self.location_input_button)

    def type_entry(self):
        """Implementation for Data Type Entry Screen."""
        # Step 3 in application flow
        actual_loc = self.location_entry.get()

        self.bg = ImageTk.PhotoImage(file='./res/secondary_logo.png')

        self.location_entry.destroy()
        self.location_input_button.destroy()
        self.main_canvas.destroy()

        self.main_canvas = Canvas(self.root, width=323, height=576, bd=0, highlightthickness=0)
        self.main_canvas.pack(fill="both", expand=True)
        self.main_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.current_search_button = Button(self.root, text="Current", font=("Helvetica", 20), width=14, fg="dark blue", command=lambda: self.current_search(actual_loc))
        self.forecast_search_button = Button(self.root, text="Forecast", font=("Helvetica", 20), width=14, fg="dark blue", command=lambda: self.forecast_search(actual_loc))
        self.astronomy_search_button = Button(self.root, text="Astronomy", font=("Helvetica", 20), width=14, fg="dark blue", command=lambda: self.astro_search(actual_loc))
        self.caclulator_init_button = Button(self.root, text="Calculator", font=("Helvetica", 20), width=14, fg="dark blue", command=lambda: self.calculator_search())

        curr_btn_win = self.main_canvas.create_window(38, 220, anchor='nw', window=self.current_search_button)
        fore_btn_win = self.main_canvas.create_window(38, 280, anchor='nw', window=self.forecast_search_button)
        astro_btn_win = self.main_canvas.create_window(38, 340, anchor='nw', window=self.astronomy_search_button)
        calc_btn_win = self.main_canvas.create_window(38, 400, anchor='nw', window=self.caclulator_init_button)

    ## Step 3 Implementations ===================

    def current_search(self, loc):
        """Implementation for Current Weather screen."""
        try:
            cur_data = self.speck.current(loc)
        except InvalidRequestUrl:
            rloc = self.speck.find_city(loc)[0]
            cur_data = self.speck.current(f"{rloc['lat']},{rloc['lon']}")

        font = int(min((30 - len(cur_data.location.name)), 24))

        print(30 - len(cur_data.location.name))
        
        top = Toplevel()
        top.title(f"Current weather in {cur_data.location.name}")
        top.geometry('323x576')
        top.resizable(width=False, height="false")

        loc_label = Label(top, text=f"{cur_data.location.name},\n{cur_data.location.country}", font=("Helvetica", font))
        temp_label = Label(top, text=f"{cur_data.temp_c()}°C", font=("Helvetica", 24), fg="dark blue")

        loc_label.pack()
        temp_label.pack()

        temp_unit = StringVar()
        temp_unit.set("°C")

        for i in ['°C', '°F']:
            Radiobutton(top, text=i, variable=temp_unit, value=i, font=("Helvetica",20)).pack(anchor=W)

        def clicked(val):
            if val == 'C':
                temp_label.config(text=f"{cur_data.temp_c()}°C")
            else:
                temp_label.config(text=f"{cur_data.temp_c.fahrenheit()}°F")

        checkbtn = Button(top,text="update", font=("Helvetica",20), width=15, fg="dark blue", command=lambda: clicked(temp_unit.get()))
        checkbtn.pack()

        close_btn_1 = Button(top, text="Close", font=("Helvetica",20), width=15, fg="dark blue", command=top.destroy).pack()

    def forecast_search(self, loc):
        """Implementation for Weather Forecast screen."""
        try:
            fore_data = self.speck.forecast(loc)
        except InvalidRequestUrl:
            rloc = self.speck.find_city(loc)[0]
            fore_data = self.speck.forecast(f"{rloc['lat']},{rloc['lon']}")

        font = int(min((30 - len(fore_data[0].location.name)), 24))

        top = Toplevel()
        top.title(f"Forecast weather in {fore_data[0].location.name}")
        top.geometry('323x576')
        top.resizable(width=False, height="false")

        lbl = Label(top, text=f"\n{fore_data[0].location.name},\n{fore_data[0].location.country}", font=("Helvetica", font))
        lbl.pack()

        options = []

        for n, i in enumerate(fore_data):
            ndt = dt.now() + td(days=n+1)

            options.append(f"{ndt.day}-{ndt.month}-{ndt.year}")

        main_info_lbl = Label(top, text=f"\n\nAverage temperature on {options[0]}:\n{fore_data[0].day.avgtemp_c()}°C\n\n", font=("Helvetica", 12), fg="dark blue")
        main_info_lbl.pack()

        day_select_menu = StringVar()
        day_select_menu.set(options[0])

        day_select_drop = OptionMenu(top, day_select_menu, *options)
        day_select_drop.pack()
        day_select_drop.config(width=16, font=("Helvetica", 16), fg="dark blue")

        def callback():
            n = options.index(day_select_menu.get())
            main_info_lbl.config(text=f"\n\nAverage temperature on {options[n]}:\n{fore_data[n].day.avgtemp_c()}°C\n\n", fg="dark blue")

        _lbl = Label(top, text="\n\n\n\n")
        _lbl.pack()

        update_btn = Button(top, text="Update", font=("Helvetica", 12), command=callback).pack()

    def astro_search(self, loc):
        """Implementation for Astronomy Information screen."""
        try:
            cur_data = self.speck.astro(loc)
        except InvalidRequestUrl:
            rloc = self.speck.astro(loc)[0]
            cur_data = self.speck.astro(f"{rloc['lat']},{rloc['lon']}")

        font = int(min((30 - len(cur_data.location.name)), 24))

        print(30 - len(cur_data.location.name))
        
        top = Toplevel()
        top.title(f"Astronomy Information in {cur_data.location.name}")
        top.geometry('323x576')
        top.resizable(width=False, height="false")

        
        lbl2 = Label(top, text=f"\n\n{cur_data.location.name},\n{cur_data.location.country}", font=("Helvetica", font))
        lbl = Label(top, text=f"\n\nMoon Phase Today:\n{cur_data.moon_phase}\n\n", font=("Helvetica", 16), fg="dark blue")

        lbl2.pack()
        lbl.pack()

        close_btn_1 = Button(top, text="Close", font=("Helvetica",20), width=15, fg="dark blue", command=top.destroy).pack()

    def calculator_search(self):
        """Run the calculator."""
        calculator.main()

    ## ==========================================

    def run(self):
        """Run the entire application. This is blocking."""
        self.root = Tk()
        self.root.title('Speck Frontend')
        self.root.geometry('323x576')
        # make sure app cant be resized
        self.root.resizable(width=False, height="false")

        self.bg = ImageTk.PhotoImage(file='./res/base_login.png')

        self.main_canvas = Canvas(self.root, width=323, height=576, bd=0, highlightthickness=0)
        self.main_canvas.pack(fill="both", expand=True)

        # put img on canvas
        self.main_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.welcome_username_entry = Entry(self.root, font=("Helvetica", 22), width=15, fg="dark blue", bd=0)
        self.welcome_password_entry = Entry(self.root, font=("Helvetica", 22), width=15, fg="dark blue", bd=0)

        self.welcome_username_entry.insert(0, "username")
        self.welcome_password_entry.insert(0, "password")

        def entry_clear(e):
            if (self.welcome_username_entry.get() == 'username' or \
                self.welcome_password_entry.get() == 'password'):

                self.welcome_username_entry.delete(0, END)
                self.welcome_password_entry.delete(0, END)
                # change pw to ***
                self.welcome_password_entry.config(show='*')

        # bind the entry boxes, ie when you click it, the text on input box shd vanish
        self.welcome_username_entry.bind("<Button-1>", entry_clear)
        self.welcome_password_entry.bind("<Button-1>", entry_clear)

        # add entry boxes to canvas
        un_window = self.main_canvas.create_window(38, 300, anchor='nw', window=self.welcome_username_entry)
        pw_window = self.main_canvas.create_window(38, 370, anchor='nw', window=self.welcome_password_entry)

        self.welcome_login_button = Button(self.root, text="LOGIN", font=("Helvetica", 18), width=16, fg="dark blue", bg="white", bd=0, command=self.welcome)
        welcome_login_button_win = self.main_canvas.create_window(44, 442, anchor='nw', window=self.welcome_login_button)

        self.root.mainloop()

if __name__ == '__main__':
    app = SpeckFrontend() # Create an instance
    app.run()