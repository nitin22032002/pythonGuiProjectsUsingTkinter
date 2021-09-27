import pyttsx3 as px
import speech_recognition as sr
def reco():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        say("listneing............")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            global command
            command=r.recognize_google(audio,language='en-in')
            try:
                say(f"you  say {command}")
            except:
                px.speak(f"you  say {command}")

        except:
            try:
                say("say again")
            except:
                px.speak("say  again")
            reco()
        return command
def say(text):
    engine=px.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
from tkinter import *
from PIL import ImageTk,Image
import pyautogui as pg
root=Tk()
def closenote():
    lable4.destroy()
    button12.destroy()
    entrynote.delete(1.0,END)
    searchnote.set("")
    entry1.update()
def search():
    global lable4,button12
    try:
        lable4.destroy()
        button12.destroy()
    except:
        pass
    with open('NOTES',"r") as f:
        a=f.readlines()
    if searchnote.get()+"\n" in a:
        say("your note")
        index=a.index(searchnote.get()+"\n")
        with open("NOTES","r") as f:
            number=int(str(a[index-1]))
            b = ""
            try:
                index2=a.index(str(number+1)+"\n")
                #print(index2)
                c=a[index+1:index2-1]
                #print(c)
                for item in c:
                    b=b+item
                #print("try")
                #print(b)
            except Exception as e:
                f.readline()
                f.readline()
                b=f.read()
               # print("except",e,type(number))
        lable4=Label(text=b,borderwidth=10,font="comicsansms 12 bold",relief=SUNKEN,bg='grey')
        lable4.place(x=470,y=90)
        entrynote.insert(1.0,b)
        if len(c) > 10:
            lable4.destroy()
            f="NOTE IS TO LARGE SO SEE IN TEXT AREA"
            lable4 = Label(text=f, borderwidth=10, font="comicsansms 12 bold", relief=SUNKEN, bg='grey')
            lable4.place(x=470, y=90)
        else:
            pass
        button12=Button(text="CLOSE NOTE",borderwidth=10,command=closenote,font="comicsansms 15 bold",relief=SUNKEN,bg='grey')
        button12.place(x=470,y=500)
        searchnote.set('')
        entry1.update()
    else:
        lable4 = Label(text=f"NO SUCH NOTE NAME {searchnote.get()} IS SAVE IN YOUR NOTES", borderwidth=12, font="comicsansms 10 bold", relief=SUNKEN, bg='grey')
        lable4.place(x=470, y=90)
        button12 = Button(text="CLOSE WARNING", borderwidth=10, command=closenote, font="comicsansms 15 bold",
                          relief=SUNKEN, bg='grey')
        button12.place(x=470, y=500)
        say(f"NO SUCH NOTE NAME {searchnote.get()} IS SAVE IN YOUR NOTES")
        searchnote.set('')
        entry1.update()
def savenote():
    global entry2,lable1,button3
    lable1=Label(text="GIVE NAME TO THIS NOTE",borderwidth=10,font="comicsansms 15 bold",bg='orange',relief=SUNKEN)
    lable1.place(x=30,y=570)
    name=StringVar()
    entry2=Entry(textvariable=name,borderwidth=10,font="comicsansms 15 bold",relief=SUNKEN)
    entry2.place(x=320,y=570)
    button3=Button(text='SAVE',borderwidth=10,command=save,font="comicsansms 15 bold",bg='yellow',relief=SUNKEN)
    button3.place(x=90,y=620)
def speak():
    a=reco()
    import  pyautogui as pg
    pg.sleep(3)
    pg.write(a)
def save():
    file = open("NOTES", "a")
    try:
        with open('NOTES',"r") as f:
            a=f.readlines()
        a.reverse()
        item = int(str(a[0]))
    except:
        item=1
        file.write(str(item)+"\n")
    file.write(entry2.get()+"\n")
    file.write(entrynote.get(1.0,END))
    file.write(str(item)+"\n")
    file.write(str(item+1)+"\n")
    file.close()
    entrynote.delete(1.0,END)
    entry2.destroy()
    lable1.destroy()
    button3.destroy()
    say("your note save successfully")
root.geometry('890x680')
root.maxsize(1000,690)
root.minsize(1000,690)
root.title("MAKE NOTES")
image=Image.open("blank.jpg")
image=ImageTk.PhotoImage(image)
root.wm_iconphoto(False,image)
lable=Label(text="WRITE NOTES IN NITIN NOTES MAKER",borderwidth=10,font="comicsansms 20 bold",bg='orange',relief=SUNKEN)
lable.place(x=0,y=10)
searchnote=StringVar()
entry1=Entry(textvariable=searchnote,borderwidth=10,font="comicsansms 20 bold",relief=SUNKEN)
entry1.place(x=540,y=10)
button1=Button(text="SEARCH",borderwidth=10,command=search,relief=SUNKEN,font="comicsansms 15 bold",bg='yellow')
button1.place(x=860,y=10)
mainentry=StringVar()
entrynote=Text(borderwidth=10,width=50,background='white',cursor='heart')
entrynote.place(x=10,y=70)
button2=Button(text="SAVE NOTE",borderwidth=10,command=savenote,relief=SUNKEN,font="comicsansms 15 bold",bg='yellow')
button2.place(x=10,y=500)
button3=Button(text="SPEAK",borderwidth=10,command=speak,relief=SUNKEN,font="comicsansms 15 bold",bg='yellow')
button3.place(x=200,y=500)


root.mainloop()