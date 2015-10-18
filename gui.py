from Tkinter import*
import Tkinter as tk
import os

app=Tk()
app.title("Example")
app.geometry('200x200+200+200')
buttontext=StringVar()
Buttext=StringVar()
buttontext.set("fuck")
Buttext.set("this")

def helloCallBack(state):
	if state==1:
		buttontext.set("a")
		Buttext.set("b")
		state=0
	elif state==0:
		buttontext.set("b")
		Buttext.set("a")
		state=1

B = Button(app, textvariable =buttontext,command = helloCallBack(0))
A = Button(app, textvariable =Buttext, command = helloCallBack(1))

B.pack()
A.pack()
app.mainloop()