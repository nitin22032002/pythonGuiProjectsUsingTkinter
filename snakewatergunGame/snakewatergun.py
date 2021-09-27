import pyttsx3 as px
import random
def ys():
    global var4
    global var3
    ae=int(var4.get())
    ar=int(var3.get())
    say(f"your score is {ae} point")
    if ae>ar:
        say("now you are lead's computer")
    elif ae==ar:
        say("now game is tie!")
    else:
        say("now computer lead's you")
def cs():
    global var4
    global var3
    ae=int(var4.get())
    ar=int(var3.get())
    say(f"computer score is {ar} point")
    if ae>ar:
        say("now you are lead's computer")
    elif ae==ar:
        say("now game is tie!")
    else:
        say("now computer lead's you")
def say(text):
    engine=px.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
def game(event):
    global var1
    global var2
    text1=str(event.widget.cget('text'))
    a=random.choice(['snake','water','gun'])
    var1.set(text1.upper())
    e1.update()
    var2.set(a.upper())
    e2.update()
    if text1==a:
        var3.set(str(int(var3.get())+0))
        var4.set(str(int(var4.get())+0))
        say("ohh! game is draw")
    elif (text1=='gun' and a=='snake') or (text1=='water' and a=='gun') or (text1=='snake' and a=="water"):
        var3.set(str(int(var3.get()) + 0))
        var4.set(str(int(var4.get()) + 1))
        say("you won the game")
    elif (text1=='snake' and a=='gun') or (text1=='gun' and a=='water') or (text1=='water' and a=="snake"):
        var3.set(str(int(var3.get()) + 1))
        var4.set(str(int(var4.get()) + 0))
        say("ohh! computer win the game")
from tkinter import *
root=Tk()
import os
root.geometry('1366x761')
root.minsize(1376,780)
root.title("SNAKE  WATER  GUN  GAME")
#os.chdir('C:\\Users\\Admin\\PycharmProjects\\snakewatergun\\snakewatergun.txtimages')
pho=PhotoImage(file='gun.png')
root.wm_iconphoto(False,pho)
Label(text="WELCOME IN SNAKE WATER GUN GAME",bg='orange',fg='blue',borderwidth=25,relief=SUNKEN,font='comicsansms 25 bold').pack(fill=X,padx=10,pady=10)
Label(text="CHOOSE YOUR CHOICE",bg='yellow',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(fill=X,padx=10,pady=10)
pho1=PhotoImage(file='gun1.png')
b1=Button(text='gun',image=pho1,borderwidth=15,font='comicsansms 5 bold')
b1.pack(side=LEFT,padx=50,anchor='ne',pady=15,fill=X)
b1.bind('<Button-1>',game)
pho2=PhotoImage(file='water.png')
b1=Button(text='water',image=pho2,borderwidth=15,font='comicsansms 5 bold')
b1.pack(side=LEFT,padx=50,anchor='ne',pady=15,fill=X)
b1.bind('<Button-1>',game)
pho3=PhotoImage(file='snake1.png')
b1=Button(text='snake',image=pho3,borderwidth=15,font='comicsansms 5 bold')
b1.pack(side=LEFT,padx=50,anchor='ne',pady=15,fill=X)
b1.bind('<Button-1>',game)
pho4=PhotoImage(file='gun.png')
#Label(image=pho3).pack()
var1=StringVar()
Label(text="YOUR CHOOSE",bg='green',fg='red',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(pady=5)
e1=Entry(textvariable=var1,bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e1.pack(pady=5)
var2=StringVar()
Label(text="COMPUTER CHOOSE",bg='green',fg='red',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(pady=5)
e2=Entry(textvariable=var2,bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e2.pack(pady=5)
var3=StringVar()
var3.set("00")
Button(text="COMPUTER SCORE",bg='green',fg='red',command=cs,borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(pady=5)
e3=Entry(textvariable=var3,bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e3.pack(pady=5)
var4=StringVar()
var4.set("00")
Button(text="YOUR SCORE",bg='green',fg='red',command=ys,borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(pady=5,side=LEFT)
e4=Entry(textvariable=var4,bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e4.pack(pady=25,side=BOTTOM)
root.mainloop()
