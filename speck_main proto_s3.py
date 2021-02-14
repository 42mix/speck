from speck.speck import Speck
from speck.errors import *

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

import calculator

with open("token.txt", "r") as f:
    speck = Speck(f.read().rstrip())

root=Tk()
root.title('entry box on canvas')
root.geometry('323x576')
#make sure app cant be resized
root.resizable(width=False, height="false")

#define bg img
bg = ImageTk.PhotoImage(file='./res/beach.png')

#define canvas
my_canvas= Canvas(root, width=323, height=576,bd=0,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)

#put img on canvas
my_canvas.create_image(0,0,image=bg, anchor="nw")

#def entry boxes

un_entry= Entry(root,font=("Helvetica",24), width=14, fg="dark blue",bd=0)
pw_entry= Entry(root,font=("Helvetica",24), width=14, fg="dark blue",bd=0)

un_entry.insert(0,"username")
pw_entry.insert(0,"password")

#def entry_clear func
def entry_clear(e):
    if un_entry.get()=="username" or pw_entry.get()=='password':
        un_entry.delete(0,END)
        pw_entry.delete(0,END)
        #change pw to ***
        pw_entry.config(show='*')

#bind the entry boxes, ie when you click it, the text on input box shd vanish
un_entry.bind("<Button-1>",entry_clear)
pw_entry.bind("<Button-1>",entry_clear)

#add entry boxes to canvas
un_window= my_canvas.create_window(34,290, anchor='nw', window=un_entry)
pw_window= my_canvas.create_window(34,370, anchor='nw', window=pw_entry)

'''
def new_window():
    main_entry = Entry(root, font=("Helvetica",24), width=14, fg="dark blue", bd=0)
    main_entry.bind("<Button-1>",entry_clear)
'''

def welcome():
    # if un_entry.get()=="username" or pw_entry.get()=='password' or un_entry.get()=="" or pw_entry.get()=='':
        # response=messagebox.showwarning("ERROR","ENTER USERNAME AND PASSWORD")
    # elif un_entry.get()!="11C" or pw_entry.get()!='11c2021':
        # response=messagebox.showwarning("ERROR","ENTER CORRECT USERNAME AND PASSWORD")

    if 0:
        pass

    else:
        un_entry.destroy()
        pw_entry.destroy()
        login_btn.destroy()
        my_canvas.destroy()

        ##################################

        my_can2 = Canvas(root, width=323, height=576,bd=0, highlightthickness=0)
        my_can2.pack(fill="both",expand=True)
        my_can2.create_image(0, 0, image=bg, anchor="nw")

        loc_entry= Entry(root,font=("Helvetica",24), width=14, fg="dark blue",bd=0)

        def loc_clear(e):
            if loc_entry.get()=="Enter Location":
                loc_entry.delete(0,END)

        loc_entry.insert(0, "Enter Location")
        loc_entry.bind("<Button-1>", loc_clear)

        loc_entry_win = my_can2.create_window(34, 290, anchor='nw', window=loc_entry)

        def page_2():
            actual_loc = loc_entry.get()

            loc_entry.destroy()
            get_btn.destroy()
            my_can2.destroy()

            my_can3 = Canvas(root, width=323, height=576,bd=0, highlightthickness=0)
            my_can3.pack(fill="both",expand=True)
            my_can3.create_image(0, 0, image=bg, anchor="nw")

            def c():
                try:
                    cur_data = speck.current(actual_loc)
                except InvalidRequestUrl:
                    rloc = speck.find_city(actual_loc)[0]
                    cur_data = speck.current(f"{rloc['lat']},{rloc['lon']}")
                
                top = Toplevel()
                top.title("This is a new window")
                top.geometry('323x576')
                top.resizable(width=False, height="false")

                lbl = Label(top, text=cur_data.temp_c(), font=("Helvetica",24))
                lbl2 = Label(top, text=f"{cur_data.location.name}, {cur_data.location.country}", font=("Helvetica",24))

                lbl.pack()
                lbl2.pack()

                temp_unit = StringVar()
                temp_unit.set("C")
                for i in ['C', 'F']:
                    Radiobutton(top, text=i, variable=temp_unit, value=i, font=("Helvetica",20)).pack(anchor=W)

                def clicked(val):
                    if val == 'C':
                        lbl.config(text=cur_data.temp_c())
                    else:
                        lbl.config(text=cur_data.temp_c.fahrenheit())

                checkbtn=Button(top,text="update", font=("Helvetica",20), width=15,fg="dark blue", command=lambda: clicked(temp_unit.get()))
                checkbtn.pack()

                close_btn_1 = Button(top, text="Close",font=("Helvetica",20), width=15,fg="dark blue", command=top.destroy).pack()
                
            def f():
                top = Toplevel()
                top.title("This is a new window")
                top.geometry('323x576')
                top.resizable(width=False, height="false")

                close_btn_2 = Button(top, text="Close",font=("Helvetica",20), width=15,fg="dark blue", command=top.destroy).pack()

            def a():
                top = Toplevel()
                top.title("This is a new window")
                top.geometry('323x576')
                top.resizable(width=False, height="false")

                close_btn_3 = Button(top, text="Close",font=("Helvetica",20), width=15,fg="dark blue", command=top.destroy).pack()

            def calc():
                calculator.main()

            curr_btn = Button(root, text="Current",font=("Helvetica",20), width=15,fg="dark blue", command=c)
            fore_btn = Button(root, text="Forecast",font=("Helvetica",20), width=15,fg="dark blue", command=f)
            astro_btn = Button(root, text="Astronomy",font=("Helvetica",20), width=15,fg="dark blue", command=a)
            calc_btn = Button(root, text="Calculator",font=("Helvetica",20), width=15,fg="dark blue", command=calc)

            curr_btn_win = my_can3.create_window(36,120, anchor='nw', window=curr_btn)
            fore_btn_win = my_can3.create_window(36,240, anchor='nw', window=fore_btn)
            astro_btn_win = my_can3.create_window(36,360, anchor='nw', window=astro_btn)
            calc_btn_win = my_can3.create_window(36,480, anchor='nw', window=calc_btn) 

        get_btn = Button(root, text="Continue",font=("Helvetica",20), width=15,fg="dark blue", command=page_2)
        get_btn_window = my_can2.create_window(36,470, anchor='nw', window=get_btn)

#def btn
login_btn= Button(root, text="LOGIN",font=("Helvetica",20), width=15,fg="dark blue", command=welcome)
login_btn_window= my_canvas.create_window(36,470, anchor='nw', window=login_btn)

root.mainloop()
