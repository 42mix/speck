from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title('image app')
root.iconbitmap("C:/Users/Nevin/OneDrive/Pictures/peace.png")

my_img=ImageTk.PhotoImage(Image.open("C:/Users/Nevin/OneDrive/Pictures/peace.png"))
my_label= Label(image=my_img)
my_label.pack()

