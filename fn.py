from Tkinter import*
import Tkinter as tk
import os


def change_button_text(name, index, mode):
    buttontext.set(widget1.get())

app=Tk()
app.title("Example")
app.geometry('200x200+200+200')

widget1 = StringVar()
widget1.set('Numbers')
files =["one",'two','three']
widget1DropDown = OptionMenu(app, widget1, *files)
widget1DropDown.config(bg = 'white',foreground='black',font=("Times",16,"italic"))
widget1DropDown["menu"].config(bg = 'white',font=("Times",12,"italic"))
widget1DropDown.pack()
widget1.trace("w", change_button_text)


buttontext=StringVar()
buttontext.set('Zero')
button1=Button(app,textvariable=buttontext,font=("Times", 16),width=15,borderwidth=5)
button1.pack(side=LEFT, padx=5,pady=8)


app.mainloop()