def say(text):
    engine=px.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
from tkinter import *
import pyttsx3 as px
import random
number= random.randint(0, 100)
import time
from PIL import ImageTk,Image
def run():
    guess = int(var1.get())
    if number<guess:
        v=Label(text=f"YOUR NUMBER {guess} IS GREATER THEN GIVEN NUMBER ", bg='yellow', fg='green', borderwidth=5, relief=SUNKEN,
                font='comicsansms 15 bold')
        v.pack(side=TOP,anchor='sw')
        var3.set(int(var3.get())+1)
        e3.update()
        say(f"YOUR NUMBER {guess} IS GREATER THEN GIVEN NUMBER")
        var1.set("")
        e1.update()
        time.sleep(1)
        v.destroy()
    elif number>guess:
        v=Label(text=f"YOUR NUMBER {guess} IS LESS THEN GIVEN NUMBER ", bg='yellow', fg='green', borderwidth=5, relief=SUNKEN,
                font='comicsansms 15 bold')
        v.pack(side=TOP,anchor='sw')
        var3.set(int(var3.get()) + 1)
        e3.update()
        say(f"YOUR NUMBER {guess} IS LESS THEN GIVEN NUMBER")
        var1.set("")
        e1.update()
        time.sleep(1)
        v.destroy()
    else:
        var2.set("10")
        e2.update()
        v = Label(text=f"YOUR GUESS IS CORRECT YOU WIN ", bg='yellow', fg='green', borderwidth=5, relief=SUNKEN,
                  font='comicsansms 15 bold')
        v.pack(side=TOP,anchor='sw')
        say(f"YOU GUESS IS CORRECT YOU WIN")
        time.sleep(1)
        v.destroy()
        var1.set("")
        e1.update()
        if int(var2.get())<int(var3.get()):
            v = Label(text=f"WINNER OF GAME IS COMPUTER  ", bg='yellow', fg='green', borderwidth=5, relief=SUNKEN,
                      font='comicsansms 15 bold')
            v.pack(side=TOP, anchor='sw')
            say("winner of game is computer")
            time.sleep(1)
            v.destroy()
        elif int(var2.get())==int(var3.get()):
            v = Label(text=f"GAME IS TIE ", bg='yellow', fg='green', borderwidth=5, relief=SUNKEN,
                      font='comicsansms 15 bold')
            v.pack(side=TOP, anchor='sw')
            say('game is tie between you and computer')
            time.sleep(1)
            v.destroy()
        else:
            v = Label(text=f"YOU WIN THE GAME ", bg='yellow', fg='green', borderwidth=5, relief=SUNKEN,
                      font='comicsansms 15 bold')
            v.pack(side=TOP, anchor='sw')
            say("you win the game")
            time.sleep(1)
            v.destroy()
        say("now game is end")
        root.quit()
root=Tk()
root.geometry('910x700')
root.minsize(910,700)
pho=Image.open('brain.jpg')
pho=ImageTk.PhotoImage(pho)
root.title("GUESS THE NUMBER GAME")
root.wm_iconphoto(False,pho)
Label(text="WELCOME IN GUESS THE NUMBER GAME",bg='orange',fg='blue',borderwidth=25,relief=SUNKEN,font='comicsansms 25 bold').pack(fill=X,padx=10,pady=10)
Label(text="IF YOUR GUESS IS CORRECT THEN YOU GOT 10 POINT ELSE COMPUTER GOT 1 POINT".upper(),bg='yellow',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(fill=X,padx=10,pady=10)
Label(text="ENTER NUMBER TO GUESS",bg='yellow',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(anchor='ne',side=LEFT,padx=30,pady=20)
var1=StringVar()
e1=Entry(textvariable=var1,bg='green',fg='orange',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e1.pack(pady=22,padx=30)
b1=Button(text="CHECK MY GUESS",bg='grey',fg='red',command=run,borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(anchor='nw',side=LEFT,padx=10,pady=10)
Label(text="YOUR SCORE",bg='orange',fg='green',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(anchor='se',side=TOP,padx=30,pady=20)
var2=StringVar()
var2.set("00")
e2=Entry(textvariable=var2,bg='purple',fg='black',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e2.pack(anchor='se',side=TOP,pady=22,padx=30)
Label(text="COMPUTER SCORE",bg='yellow',fg='blue',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold').pack(anchor='se',side=TOP,padx=30,pady=20)
var3=StringVar()
var3.set("00")
e3=Entry(textvariable=var3,bg='purple',fg='black',borderwidth=15,relief=SUNKEN,font='comicsansms 15 bold')
e3.pack(anchor='se',side=TOP,pady=22,padx=30)




root.mainloop()
