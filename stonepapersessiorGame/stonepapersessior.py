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
    a=random.choice(['stone','paper','sessior'])
    var1.set(text1.upper())
    e1.update()
    var2.set(a.upper())
    e2.update()
    if text1==a:
        var3.set(str(int(var3.get())+0))
        var4.set(str(int(var4.get())+0))
        say("ohh! game is draw")
    elif (text1=='stone' and a=='sessior') or (text1=='paper' and a=='stone') or (text1=='sessior' and a=="paper"):
        var3.set(str(int(var3.get()) + 0))
        var4.set(str(int(var4.get()) + 1))
        say("you won the game")
    elif (text1=='sessior' and a=='stone') or (text1=='stone' and a=='paper') or (text1=='paper' and a=="sessior"):
        var3.set(str(int(var3.get()) + 1))
        var4.set(str(int(var4.get()) + 0))
        say("ohh! computer win the game")
from tkinter import *
root=Tk()
root.geometry('1366x761')
root.minsize(1376,780)
root.title("STONE PAPER SESSIOR  GAME")
pho=PhotoImage(file='sessior.png')
root.wm_iconphoto(False,pho)
#pho=PhotoImage(file='gunm.png')
def start(event):
    pass
Label(text="WELCOME IN STONE PAPER SESSIOR GAME",bg='orange',fg='blue',borderwidth=25,relief=SUNKEN,font='comicsansms 25 bold').pack(fill=X,padx=10,pady=10)
Label(text="CHOOSE YOUR CHOICE",bg='yellow',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(fill=X,padx=10,pady=10)
pho1=PhotoImage(file='stone.png')
b1=Button(text='stone',image=pho1,borderwidth=15,font='comicsansms 5 bold')
b1.pack(side=LEFT,padx=50,anchor='ne',pady=15,fill=X)
b1.bind('<Button-1>',game)
pho2=PhotoImage(file='paper.png')
b1=Button(text='paper',image=pho2,borderwidth=15,font='comicsansms 5 bold')
b1.pack(side=LEFT,padx=50,anchor='ne',pady=15,fill=X)
b1.bind('<Button-1>',game)
pho3=PhotoImage(file='sessior.png')
b1=Button(text='sessior',image=pho3,borderwidth=15,font='comicsansms 5 bold')
b1.pack(side=LEFT,padx=50,anchor='ne',pady=15,fill=X)
b1.bind('<Button-1>',game)
#pho4=PhotoImage(file='gun.png')
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
Button(text="COMPUTER SCORE",bg='green',command=cs,fg='red',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(pady=5)
e3=Entry(textvariable=var3,bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e3.pack(pady=5)
var4=StringVar()
var4.set("00")
Button(text="YOUR SCORE",bg='green',fg='red',command=ys,borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(pady=5,side=LEFT)
e4=Entry(textvariable=var4,bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e4.pack(pady=25,side=BOTTOM)
root.mainloop()
