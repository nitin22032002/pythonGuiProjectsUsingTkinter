import smtplib as smss
import pyttsx3 as px
def say(text):
    engine=px.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
import pyautogui as pag
import os
a=os.getcwd()
import random
import time as t
os.chdir(f'{os.getcwd()}\\gym data')
try:
    with open("code of client", 'r') as f:
        list1 = f.readlines()
except:
    list1=[]
def email():
    global code ,codef,fflable2,ffentry2,ffsubbutton,list1
    try:
        with open("code of client", 'r') as f:
            list1 = f.readlines()
    except:
        pass
    os.chdir(a)
    try:
        gmail=list1[list1.index(f"{useridf.get()}\n")+2]
        code = random.randint(1000, 9999)
        server = smss.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('gym@gmail.com', 'password')
        server.sendmail('gym@gmail.com',gmail, f'HI {useridf.get()} YOUR OTP OF VERIFICATION TO GOT PASSWORD IS {code}')
        say("otp is sended to verify you on your provided gmail i d please enter otp")
        fflable2 = Label(text="ENTER OTP", font="comicsansms 20 bold")
        fflable2.place(x=40, y=390)
        codef = StringVar()
        ffentry2 = Entry(textvariable=codef, font="comicsansms 15 bold", borderwidth=10,
                         relief=SUNKEN)
        ffentry2.place(x=230, y=387)
        ffsubbutton = Button(text="SUBMIT", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                             command=sub)
        ffsubbutton.place(x=500, y=380)
    except:
        pg.alert("YOUR ENTER USER ID IS INVALID")
        useridf.set('')
def ffback():
    ffbackbutton.destroy()
    ffheader1.destroy()
    fflable1.destroy()
    ffentry1.destroy()
    ffnextbutton.destroy()
    try:
        fflable2.destroy()
        ffentry2.destroy()
        ffsubbutton.destroy()
        fflablecode.destroy()
    except:
        pass
    flogin()
def sub():
    global fflablecode
    if  code==int(codef.get()):
        say("your otp is verified")
        say("your password is"+list1[list1.index(f"{useridf.get()}\n")+1])
        fflablecode=Label(text="YOUR PASSWORD IS "+list1[list1.index(f"{useridf.get()}\n")+1], font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN)
        fflablecode.place(x=30,y=600)
    else:
        say("your provided opt is invalid please enter valid otp")
        pg.alert("YOUR ENTER OTP IS INCORRECT")
        codef.set('')
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as sms
root=Tk()
root.title("NITIN HEALTH CLUB")
root.geometry('1366x756')
os.chdir(a)
os.chdir(f'{os.getcwd()}\\images')
photo1=Image.open("gym (2).jpg")
photo1=ImageTk.PhotoImage(photo1)
root.wm_iconphoto(False,photo1)
photo2=Image.open('gym.jpg')
photo2=ImageTk.PhotoImage(photo2)
os.chdir(a)
def start():
    global slable1,slable2,slable3,slable4,loginbutton,signupbutton
    os.chdir(f'{os.getcwd()}\\images')
    gymimage = Image.open("back.jpg")
    gymimage = ImageTk.PhotoImage(gymimage)
    os.chdir(a)
    headerhigh = Label(image=gymimage)
    headerhigh.place(x=10, y=10)
    slable1 = Label(image=photo1, borderwidth=10, relief=SUNKEN)
    slable1.place(x=465, y=10)
    slable2= Label(text="NITIN HEALTH CLUB\n\nADDRESS-VIJAY NAGAR\n ROAD NUMBER 4 \nMUMBAI(754009)", borderwidth=20,
               relief=SUNKEN, font="comicsansms 25 bold", bg="orange")
    slable2.place(x=10, y=10)
    slable3 = Label(text="HELP AND SUPPORT\n\nCONTACT NUMBER-7000450160\n\nEmail-GNIT2203@GMAIL.COM", borderwidth=20,
               relief=SUNKEN, font="comicsansms 20 bold", bg="orange")
    slable3.place(x=900, y=10)
    slable4=Label(image=photo2, borderwidth=10, relief=SUNKEN)
    slable4.place(x=200, y=480)
    loginbutton = Button(text="LOG IN", bg="yellow", fg="green", borderwidth=20, font="comicsansms 30 bold", relief=SUNKEN,
                command=login)
    loginbutton.place(x=330, y=330)
    signupbutton = Button(text="SIGN UP", bg="yellow", fg="green", borderwidth=20, font="comicsansms 30 bold", relief=SUNKEN,
                command=signup)
    signupbutton.place(x=730, y=330)
def fsignup():
    global fsheader,fslable1,fslable2,fslable3,fslable4,fslable5,fslable6,fsentry1,fsentry2,fsentry3,fsentry4,fsentry5,fsentry6,fsradiolable,fsradio1,fsradio2,fsradio3,fsradio4,fsradio5,fsradio6,fssubmitbutton,fsbackbutton,username,parentname,address,dob,mobileno,profession,useremail
    fsheader = Label(text="WELCOME IN NITIN HEALTH CLUB", borderwidth=20,
               relief=SUNKEN, font="comicsansms 30 bold", bg="orange")
    fsheader.place(x=350, y=10)
    fslable1 = Label(text="NAME", font="comicsansms 20 bold")
    fslable1.place(x=20, y=123)
    username=StringVar()
    fsentry1= Entry(textvariable=username, font="comicsansms 15 bold", borderwidth=10,
               relief=SUNKEN)
    fsentry1.place(x=120, y=120)
    fslable2= Label(text="FATHER\MOTHER NAME", font="comicsansms 20 bold")
    fslable2.place(x=20, y=203)
    parentname= StringVar()
    fsentry2= Entry(textvariable=parentname, font="comicsansms 15 bold", borderwidth=10,
               relief=SUNKEN)
    fsentry2.place(x=360, y=200)
    fslable3= Label(text="DATE OF BIRTH (DD/MM/YYYY)", font="comicsansms 20 bold")
    fslable3.place(x=20, y=283)
    dob= StringVar()
    fsentry3= Entry(textvariable=dob, font="comicsansms 15 bold", borderwidth=10,
                relief=SUNKEN)
    fsentry3.place(x=440, y=280)
    fslable4= Label(text="E Mail ID", font="comicsansms 20 bold")
    fslable4.place(x=20, y=363)
    useremail= StringVar()
    fsentry4= Entry(textvariable=useremail, font="comicsansms 15 bold", borderwidth=10,
                relief=SUNKEN)
    fsentry4.place(x=150, y=360)
    fslable5= Label(text="MOBILE NUMBER", font="comicsansms 20 bold")
    fslable5.place(x=20, y=443)
    mobileno= StringVar()
    fsentry5= Entry(textvariable=mobileno, font="comicsansms 15 bold", borderwidth=10,
                relief=SUNKEN)
    fsentry5.place(x=270, y=440)
    fslable6 = Label(text="PERMANENT ADDRESS", font="comicsansms 20 bold")
    fslable6.place(x=20, y=523)
    address= StringVar()
    fsentry6= Entry(textvariable=address, font="comicsansms 15 bold", borderwidth=10,
                relief=SUNKEN)
    fsentry6.place(x=350, y=520)
    fsradiolable= Label(text="PROFESSION", font="comicsansms 20 bold")
    fsradiolable.place(x=20, y=603)
    profession= StringVar()
    fsradio1= Radiobutton(variable=profession, text="STUDENT", value='STUDENT', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    fsradio1.place(x=220, y=600)
    fsradio2= Radiobutton(variable=profession, text="TEACHER", value='TEACHER', font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    fsradio2.place(x=370, y=600)
    fsradio3= Radiobutton(variable=profession, text="ENGINEAR", value='ENGINEAR', font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    fsradio3.place(x=520, y=600)
    fsradio4= Radiobutton(variable=profession, text="DOCTOR", value='DOCTOR', font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    fsradio4.place(x=680, y=600)
    fsradio5= Radiobutton(variable=profession, text="BUSSINESS MAN", value='BUSSINESS MAN', font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    fsradio5.place(x=820, y=600)
    fsradio6 = Radiobutton(variable=profession, text="OTHER", value='OTHER', font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    fsradio6.place(x=1040, y=600)
    fsbackbutton= Button(text="BACK", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,command=fsback)
    fsbackbutton.place(x=10, y=10)
    fssubmitbutton = Button(text="SUBMIT", font="comicsansms 20 bold", borderwidth=25, bg="grey", relief=SUNKEN,command=fssubmit)
    fssubmitbutton.place(x=1150, y=10)
def flogin():
    global flheader1, fllable1, fllable2, flheader2,flentry1, flentry2,flsubmitbutton, flbackbutton, useridl,passwordl,forgotpasswordbutton
    flheader1 = Label(text="WELCOME IN NITIN HEALTH CLUB", borderwidth=20,
                     relief=SUNKEN, font="comicsansms 30 bold", bg="orange")
    flheader1.place(x=350, y=10)
    os.chdir(f'{os.getcwd()}\\images')
    flheader2 = Label(image=photo2, borderwidth=10, relief=SUNKEN)
    flheader2.place(x=210, y=100)
    fllable1 = Label(text="USER ID", font="comicsansms 20 bold")
    fllable1.place(x=40, y=360)
    useridl = StringVar()
    flentry1 = Entry(textvariable=useridl, font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    flentry1.place(x=170, y=357)
    fllable2 = Label(text="PASSWORD", font="comicsansms 20 bold")
    fllable2.place(x=40, y=463)
    passwordl = StringVar()
    flentry2 = Entry(textvariable=passwordl, show='*', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    flentry2.place(x=230, y=460)
    flbackbutton = Button(text="BACK", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                           command=flback)
    flbackbutton.place(x=10, y=10)
    flsubmitbutton = Button(text="SUBMIT", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                             command=flsubmit)
    flsubmitbutton.place(x=300, y=590)
    forgotpasswordbutton = Button(text="FORGOT PASSWORD", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                            command=forgotpassword)
    forgotpasswordbutton.place(x=850, y=590)
    os.chdir(a)
def fssecondsignup():
    global fssheader,fsslable1,fssentry1,fsslable2,fssentry2,fsslable3,fssentry3,fssradiolable,fssradio1,fssradio2,fssradio3,fssradio4,fssradio5,fssradio6,fssbackbutton,fsssubmitbutton,userid,password,confirmpassword,modeofpayment
    os.chdir(f'{os.getcwd()}\\images')
    fssheader = Label(image=photo2, borderwidth=10, relief=SUNKEN)
    fssheader.place(x=210, y=10)
    fsslable1= Label(text="USER ID", font="comicsansms 20 bold")
    fsslable1.place(x=40, y=283)
    userid= StringVar()
    fssentry1= Entry(textvariable=userid, font="comicsansms 15 bold", borderwidth=10,
               relief=SUNKEN)
    fssentry1.place(x=170, y=280)
    fsslable2= Label(text="PASSWORD", font="comicsansms 20 bold")
    fsslable2.place(x=40, y=363)
    password= StringVar()
    fssentry2= Entry(textvariable=password, show='*', font="comicsansms 15 bold", borderwidth=10,
               relief=SUNKEN)
    fssentry2.place(x=230, y=360)
    fsslable3 = Label(text="CONFIRM PASSWORD", font="comicsansms 20 bold")
    fsslable3.place(x=40, y=443)
    confirmpassword = StringVar()
    fssentry3= Entry(textvariable=confirmpassword, show="*", font="comicsansms 15 bold", borderwidth=10,
               relief=SUNKEN)
    fssentry3.place(x=360, y=440)
    fssradiolable = Label(text="MODE OF PAYMENT", font="comicsansms 20 bold")
    fssradiolable.place(x=40, y=523)
    modeofpayment = StringVar()
    fssradio1= Radiobutton(variable=modeofpayment, text="CASH", value='CASH', font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    fssradio1.place(x=320, y=520)
    fssradio2 = Radiobutton(variable=modeofpayment, text="CARD", value='CARD', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    fssradio2.place(x=430, y=520)
    fssradio3 = Radiobutton(variable=modeofpayment, text="UPI", value='UPI', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    fssradio3.place(x=540, y=520)
    fssradio4 = Radiobutton(variable=modeofpayment, text="CHEQUE", value='CHEQUE', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    fssradio4.place(x=630, y=520)
    fssradio5= Radiobutton(variable=modeofpayment, text="PAYTM", value='PAYTM', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    fssradio5.place(x=770, y=520)
    fssradio6 = Radiobutton(variable=modeofpayment, text="GOOGLE PAY", value='GOOGLE PAY', font="comicsansms 15 bold", borderwidth=10,
                      relief=SUNKEN)
    fssradio6.place(x=900, y=520)
    fssbackbutton = Button(text="BACK", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                           command=fssback)
    fssbackbutton.place(x=10, y=10)
    fsssubmitbutton = Button(text="SUBMIT", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                             command=fsssubmit)
    fsssubmitbutton.place(x=700, y=610)
    os.chdir(a)
def fforgot():
    global useridf,ffheader1,fflable1,ffentry1,ffnextbutton,ffbackbutton
    os.chdir(f'{os.getcwd()}\\images')
    ffheader1 = Label(image=photo2, borderwidth=10, relief=SUNKEN)
    ffheader1.place(x=210, y=10)
    fflable1 = Label(text="USER ID", font="comicsansms 20 bold")
    fflable1.place(x=40, y=260)
    useridf = StringVar()
    ffentry1 = Entry(textvariable=useridf, font="comicsansms 15 bold", borderwidth=10,
                     relief=SUNKEN)
    ffentry1.place(x=170, y=257)
    ffnextbutton = Button(text="NEXT", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                             command=email)
    ffnextbutton.place(x=500, y=260)
    ffbackbutton = Button(text="back", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                          command=ffback)
    ffbackbutton.place(x=10, y=10)
    os.chdir(a)
def delstart():
    slable1.destroy()
    slable2.destroy()
    slable3.destroy()
    slable4.destroy()
    loginbutton.destroy()
    signupbutton.destroy()
def delfsignup():
    fsheader.destroy()
    fslable1.destroy()
    fsentry1.destroy()
    fslable2.destroy()
    fsentry2.destroy()
    fslable3.destroy()
    fsentry3.destroy()
    fslable4.destroy()
    fsentry4.destroy()
    fslable5.destroy()
    fsentry5.destroy()
    fslable6.destroy()
    fsentry6.destroy()
    fsradiolable.destroy()
    fsradio1.destroy()
    fsradio2.destroy()
    fsradio3.destroy()
    fsradio4.destroy()
    fsradio5.destroy()
    fsradio6.destroy()
    fssubmitbutton.destroy()
    fsbackbutton.destroy()
def delfssecondsignup():
    fssheader.destroy()
    fsslable1.destroy()
    fssentry1.destroy()
    fsslable2.destroy()
    fssentry2.destroy()
    fsslable3.destroy()
    fssentry3.destroy()
    fssradiolable.destroy()
    fssradio1.destroy()
    fssradio2.destroy()
    fssradio3.destroy()
    fssradio4.destroy()
    fssradio5.destroy()
    fssradio6.destroy()
    fsssubmitbutton.destroy()
    fssbackbutton.destroy()
def delflogin():
    flheader1.destroy()
    flheader2.destroy()
    fllable1.destroy()
    flentry1.destroy()
    fllable2.destroy()
    flentry2.destroy()
    flbackbutton.destroy()
    flsubmitbutton.destroy()
    forgotpasswordbutton.destroy()
def signup():
    delstart()
    fsignup()
def login():
    delstart()
    flogin()
def fsback():
    delfsignup()
    start()
import pyautogui as pg
def fssubmit():
    date=list(dob.get().split("/"))
    if username.get() != "" and parentname.get() != "" and address.get() != "" and dob.get() != "" and useremail.get() != "" and profession.get() != "" and mobileno.get()!="":
        if len(mobileno.get())==10 and mobileno.get().isnumeric() and (useremail.get()[len(useremail.get())-10:len(useremail.get())+1]=='@gmail.com' or useremail.get()[len(useremail.get())-10:len(useremail.get())+1]=='@GMAIL.COM') :
            try:
                if int(date[0])<32 and int(date[1])<13 and 2010 >int(date[2])>1950 and date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
                    delfsignup()
                    fssecondsignup()
                else:
                    pg.alert("PLEASE ENTER VALID DATE OF BIRTH")
                    dob.set("")
                    fslable3.update()
            except:
                pg.alert("PLEASE ENTER VALID DATE OF BIRTH")
                dob.set("")
                fslable3.update()
        else:
            pg.alert("PLEASE ENTER VALID MOBILE NUMBER OR EMAIL ID")
    else:
        pg.alert("PLEASE FILL COMPLETE DETAIL")
def fssback():
    delfssecondsignup()
    fsignup()
def fsssubmit():
    time=t.asctime(t.localtime(t.time()))
    if f"{userid.get()}\n" not in list1 and userid.get()!="" and password.get()!='':
        if password.get()==confirmpassword.get():
            say("thankyou for join nitin health club")
            say("please login and fill other detail")
            delfssecondsignup()
            start()
            os.chdir(f'{os.getcwd()}\\gym data')
            with open("code of client","a") as f:
                f.write(f"{userid.get()}\n")
                f.write(f"{password.get()}\n")
                f.write(f"{useremail.get()}\n")
            os.chdir(a)
            os.chdir(f'{os.getcwd()}\\client data')
            with open(userid.get()+password.get(),"a") as var1:
                var1.write("PERSONAL DETAILS\n")
                var1.write(f"USER ID - {userid.get()}\n")
                var1.write(f"DATE AND TIME OF REGISTERATION -{time.upper()}\n")
                var1.write(f"NAME- {username.get().upper()}\n")
                var1.write(f"PARENT NAME - {parentname.get().upper()}\n")
                var1.write(f"DATE OF BIRTH - {dob.get().upper()}\n")
                var1.write(f"MOBILE NUMBER - {mobileno.get().upper()}\n")
                var1.write(f"E MAIL ID - {useremail.get().upper()}\n")
                var1.write(f"ADDRESS - {address.get().upper()}\n")
                var1.write(f"PROFESSION - {profession.get().upper()}\n")
                var1.write(f"MODE OF PAYMENT - {modeofpayment.get().upper()}")
                os.chdir(a)
        else:
            pg.alert("YOUR PASSWORD AND CONFIRM PASSWORD NOT MATCH")
            password.set("")
            fssentry2.update()
            confirmpassword.set("")
            fssentry3.update()
    else:
        pg.alert("THIS USER ID ALREADY EXIST")
        userid.set("")
        fssentry1.update()
def flback():
    delflogin()
    start()
def forgotpassword():
    delflogin()
    fforgot()
def flrback():
    resultlable.destroy()
    resultlable2.destroy()
    resultlable3.destroy()
    flrbackbutton.destroy()
    flogin()
def flsubmit():
    try:
        os.chdir(f'{os.getcwd()}\\gym data')
        with open("code of client", 'r') as f:
            list1 = f.readlines()
    except:
        pass
    os.chdir(a)
    global flsheader, flslable1, flsentry1, flslable2, flsentry2, flslable3, flsentry3, flssubmitbutton, flsbackbutton,result,height,weight,whatyouwant
    if f"{useridl.get()}\n" in list1 and f"{passwordl.get()}\n"==list1[(list1.index(useridl.get()+"\n"))+1]:
        delflogin()
        os.chdir(f'{os.getcwd()}\\client data')
        with open(useridl.get() + passwordl.get(), "r") as f:
            li = f.readlines()
        os.chdir(a)
        if len(li) == 11:
            os.chdir(f'{os.getcwd()}\\images')
            flsheader = Label(image=photo2, borderwidth=10, relief=SUNKEN)
            flsheader.place(x=210, y=10)
            flslable1 = Label(text="WEIGHT", font="comicsansms 20 bold")
            flslable1.place(x=40, y=283)
            weight = StringVar()
            flsentry1 = Entry(textvariable=weight, font="comicsansms 15 bold", borderwidth=10,
                              relief=SUNKEN)
            flsentry1.place(x=170, y=280)
            flslable2 = Label(text="HEIGHT", font="comicsansms 20 bold")
            flslable2.place(x=40, y=363)
            height = StringVar()
            flsentry2 = Entry(textvariable=height, font="comicsansms 15 bold", borderwidth=10,
                              relief=SUNKEN)
            flsentry2.place(x=230, y=360)
            flslable3 = Label(text="WHAT YOU WANT", font="comicsansms 20 bold")
            flslable3.place(x=40, y=443)
            whatyouwant = StringVar()
            flsentry3 = Entry(textvariable=whatyouwant, font="comicsansms 15 bold", borderwidth=10,
                              relief=SUNKEN)
            flsentry3.place(x=360, y=440)
            flsbackbutton = Button(text="BACK", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                                   command=flsback)
            flsbackbutton.place(x=10, y=10)
            flssubmitbutton = Button(text="SUBMIT", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                                     command=flssubmit)
            flssubmitbutton.place(x=700, y=610)
            os.chdir(a)
        else:
            flssubmit()
    else:
        pg.alert("ENTER VALID USER ID OR PASSWORD")
        useridl.set('')
        flentry1.update()
        passwordl.set('')
        flentry2.update()
def flsback():
    delfslogin()
    flogin()
def delfslogin():
    flsheader.destroy()
    flslable1.destroy()
    flsentry1.destroy()
    flslable2.destroy()
    flsentry2.destroy()
    flslable3.destroy()
    flsentry3.destroy()
    flssubmitbutton.destroy()
    flsbackbutton.destroy()
def flssubmit():
    global resultlable, flrbackbutton,li,resultlable2,resultlable3
    os.chdir(f'{os.getcwd()}\\client data')
    with open(useridl.get() + passwordl.get(), "r") as f:
        li = f.readlines()
    if len(li) == 11:
        with open(useridl.get() + passwordl.get(), "a") as var1:
            var1.write("\n\nPHYSICAL DETAIL\n")
            var1.write(f"HEIGHT -{height.get()}\n")
            var1.write(f"WEIGHT -{weight.get()}\n")
            var1.write(f"WHAT YOU WANT -{whatyouwant.get().upper()}\n")
            delfslogin()
    with open(useridl.get() + passwordl.get(), "r") as f:
        try:
            result1 = int(f.readline())
            result = f.read()
        except:
            with open(useridl.get() + passwordl.get(), "r") as f:
                result=f.read()
    os.chdir(a)
    try:
        with open(str(result1),"r") as f:
            result1=f.read()
    except:
        result1="YET GYM MANAGMENT NOT      \n DECIDE YOUR CHART"
    os.chdir(f'{os.getcwd()}\\gym data')
    with open("gymshedule","r") as f:
        result2=f.read()
    resultlable=Label(text=result,borderwidth=10,relief=SUNKEN,font="comicsansms 20 bold",bg="orange",fg="blue")
    resultlable.place(x=10,y=10)
    resultlable2= Label(text=result1, borderwidth=10, relief=SUNKEN, font="comicsansms 20 bold", bg="orange", fg="blue")
    resultlable2.place(x=890, y=10)
    resultlable3 = Label(text=result2, borderwidth=10, relief=SUNKEN, font="comicsansms 20 bold", bg="orange",
                         fg="blue")
    resultlable3.place(x=10, y=570)
    flrbackbutton = Button(text="BACK", font="comicsansms 15 bold", borderwidth=20, bg='grey', relief=SUNKEN,
                              command=flrback)
    flrbackbutton.place(x=1250,y=610)
    os.chdir(a)
start()
root.mainloop()