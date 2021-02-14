from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root=Tk()
root.title("new window")

root.filename= filedialog.askopenfilename(initialdir="C:/Users/nevin/OneDrive/Pictures/peace.png",title="select a file", filetypes=(("png files","*.png"),("all files","*.*"),("jpg files","*.jpg")))
my_label= Label(root, text=root.filename).pack()
my_image=ImageTk.PhotoImage(Image.open(root.filename))
my_img_label= Label(image=my_image).pack()

def open():
    global my_image
    root.filename= filedialog.askopenfilename(initialdir="C:/Users/nevin/OneDrive/Pictures/peace.png",title="select a file", filetypes=(("png files","*.png"),("all files","*.*"),("jpg files","*.jpg")))
    my_label= Label(root, text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label= Label(image=my_image).pack()

my_btn= Button(root, text="open file", command=open).pack()

mainloop()
