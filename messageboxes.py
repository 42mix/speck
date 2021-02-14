from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('NOICE')

def popup():
    response=messagebox.showinfo("this is my popup","hello world")
    #(what the text on the button will show, what they will display when button is clicked)
    Label(root, text=response).pack()
    '''showerror, showinfo, showwarning all have only one button 'ok' , which it will display when clicked '''


    

    '''if its askquestion, the output will be yes or no , unlike askyesno or askokcancel

    if response=='yes':
        Label(root,text="you clicked yes!").pack()
    else:
        Label(root,text="you clicked no!").pack()'''



    
    '''response=messagebox.askyesno("this is my popup","hello world")
    if response==1:
        Label(root,text="you clicked yes!"),pack()
    else:
        Label(root,text="you clicked no!").pack()
this(or if we use askokcancel) will give output when we click: yes=1, no=0
but if its askquestion no need of if statements, directly will give yes and no
        '''

#showinfo, showwarning(warning icon[!]), showerror(shows an [X]),
#askquestion(shows[?] and buttons that can be clicked are yes or no)
#askokcancel(shows[?] and buttons that can be clicked are yes or cancel),
#askyesno(shows[?] and buttons that can be clicked are yes or no)
#the above are the diff message boxes and have diff sounds also

Button(root, text='popup', command=popup).pack()


mainloop()

