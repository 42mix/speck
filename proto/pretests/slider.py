from tkinter import *

root=Tk()
root.title('sliders')
root.geometry("400x400") #increases size of window ie horizontal x vertical


vertical=Scale(root, from_=0, to=400)
#default is vertical slider
vertical.pack()

horizontal= Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

def slide():
    lbl=Label(root, text=horizontal.get()).pack() #will be static, ie will display zero under horizontal slider and wont change
    root.geometry(str(horizontal.get())+"x400") #horizntl x vertical
my_btn=Button(root,text="click me",command=slide).pack()


root.mainloop()
