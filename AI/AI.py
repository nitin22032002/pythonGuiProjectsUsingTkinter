import pyttsx3 as px
import gtts as gt
import webbrowser as wb
import speech_recognition as sr
import wikipedia as  wk
import time as t
import os
import pyautogui as pag
def reco():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listneing............")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("recorginise.............")
            global command
            command=r.recognize_google(audio,language='en-in')
            print(f"you say {command}")
            try:
                say(f"you  say {command}")
            except:
                px.speak(f"you  say {command}")

        except:
            print("please say again..............")
            try:
                say("say again")
            except:
                px.speak("say  again")
            reco()
        return command
px.speak("say code")
code=reco()
f=open("codeai","r")
ccode=f.readlines()
f.close()
if f"{code}\n"==ccode[0]:
    b=int(ccode[1])
    name=ccode[2]
    username=ccode[3]
else:
    px.speak("which ,a i, you,want, male, or, female")
    genderai=reco()
    if genderai =="mail":
        b=0
    elif genderai=="female":
        b=1
    else:
        import random

        b=random.randint(0,1)
def say(text):
    engine=px.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[b].id)
    engine.say(text)
    engine.runAndWait()
def wish(name):
    time=t.asctime(t.localtime(t.time()))
    timelist=list(time)
    global cutime
    cutime=int(timelist[11]+timelist[12])
    if 0< cutime<12:
        say(f"good morning {name} sir")
        print(f"good morning {name}")
    elif 12<=cutime<17:
        say(f"good afternoon {name} sir")
        print(f"good afternoon {name} sir")
    elif 17<=cutime<20:
        say(f"good evening {name} sir")
        print(f"good evening {name} sir")
    else:
        say(f"good night {name} sir")
        print(f"good night {name} sir")
def email(to,content):
    file = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    os.startfile(file)
    t.sleep(5)
    pag.click(1150, 130)
    t.sleep(7)
    pag.click(20, 180)
    t.sleep(10)
    pag.write(to)
    t.sleep(2)
    pag.click(1150, 500)
    pag.write(content)
    t.sleep(7)
    pag.click(860, 700)
def opensite(site):
    gen=list(site.split(" "))
    try:
        say(f"now {gen[1]} is opening..............")
        wb.open(f"{gen[1]}.com")
        print(f"now {gen[1]} is opening.............." )
    except:
        say("this site not exist try again")
        print("this site not exist try again")
        help=reco()
if f"{code}\n"!=ccode[0]:
    say("preffer name to me  please")
    name=reco()
    say("what's your name sir")
    username=reco()
    say(f"say me secret code to save in data {username}")
    code=reco()
    f=open("codeai","w")
    f.write(f"{code}\n")
    f.write(f"{b}\n")
    f.write(f"{name}\n")
    f.write(f"{username}")
    f.close()
wish(username)
sh=open("shedule","r")
shed=sh.readlines()
sh.close()
time = t.asctime(t.localtime(t.time()))
time = list(time.split(" "))
if 6==cutime or cutime<7:
    index=0
elif 7==cutime or cutime<8:
    index=1
elif 8==cutime or cutime<11:
    index=2
elif 11==cutime or cutime<13:
    index=3
elif 13==cutime or cutime<17:
    index=4
elif 17==cutime or cutime<18:
    index=1
elif 18==cutime or cutime<19:
    index=4
elif 19==cutime or cutime<23:
    index=5
else:
    index=6
print(f"it is your {shed[index]}")
say(f"it is you {shed[index]}")
try:
    f=open("choice1","r")
    shl=open("choice2","r")
    var1=shl.readlines()
    shl.close()
    a=f.readlines()
    if a[0]==str(time[2]) and var1[0]=="yes":
        s=open("compliment","r")
        import random
        i=random.randint(0,326)
        sl=s.readlines()
        pl=sl[i]
        say(f"your today compiment is {pl}")
        print(f'your today compliment is {pl}')
        f=open("choice1","w")
        if time[1] in ["apr","jun","sept","nov"] :
            if str(time[2])=="30":
                f.write("1")
            else:
                f.write(str(int(time[2])+1))
        else:
            if str(time[2])=="31":
                f.write("1")
            else:
                f.write(str(int(time[2])+1))
        f.close()
        s.close()
except Exception as e:
    print(e)
while True:
    say("how can i help you")
    help=reco()
    help = str(help)
    if help=="what's your name":
        say(f"i am {name}")
    elif help[0:9]=="translate":
        say("you want to write or speak text")
        a=pag.confirm("select choice",buttons=['write','speak'])
        if a=="write":
            ino=input("write text here >>>>")
            from eng_hindi import eth
            say("your text is translating")
            print(f"your english text is {ino}\n its translation in hindi is {eth(ino)}")
            say(f"your english text is {ino}")
            say("your text is translated")
        elif a=="speak":
            say("say the text to me")
            ino=reco()
            from eng_hindi import eth
            say("your text is translating")
            print(f"your english text is {ino} \nits translation in hindi is {eth(ino)}")
            say(f"your english text is {ino}")
            say("your text is translated")
    elif help[0:6]=="record":
            say("your recording is start after 2 second")
            t.sleep(2)
            audio=reco()
            audio=gt.gTTS(str(audio))
            say("your recording is completed")
            say(f"your audio")
            import playsound
            playsound.playsound(audio)
            say("say name to me to save audio")
            namea=reco()
            audio.save(f"{namea}.mp3")
            say("your audio is saved")
    elif help=="what can you do for me":
        print("i will do for you many things like open any site,app , send email , got time ,date , any thing search...........")
        say("i will do for you many things like open any site,app , send email , got time ,date , any thing search")
    elif "Wikipedia"==help[0:9]:
        say("google is opening")
        file = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        os.startfile(file)
        t.sleep(3)
        pag.write(help)
        say(f"{help} is opening....")
        pag.keyDown("enter")
        t.sleep(3)
        pag.click(650, 600)
        say("yes i got result")
    elif help=="time":
        say("current time is")
        time = t.asctime(t.localtime(t.time()))
        time = list(time.split(" "))
        timet=time[4]
        print(timet)
        say(timet)
    elif help=="date":
        say("today date is")
        timed=f"{time[3]}  {time[1]}  {time[5]}  day  {time[0]}"
        print(timed)
        say(timed)
    elif help=="date time":
        time = t.asctime(t.localtime(t.time()))
        time = list(time.split(" "))
        timedt=f"today date is  {time[3]}  {time[1]}  {time[5]}  day  {time[0]}  current time is {time[4]} "
        print(timedt)
        say(timedt)
    elif help=="give compliment":
        f=open("compliment","r")
        listc=f.readlines()
        import random
        f.close()
        while True:
            i=random.randint(0,326)
            print(listc[i])
            say(listc[i])
            say("you want more compliment")
            cho=reco()
            if str(cho)=="yes":
                continue
            else:
                break
        say("you want set daily compliment")
        cho1=reco()
        f=open("choice2","w")
        s=open("choice1","w")
        if str(cho1) == "yes":
            f.write("yes")
            s.write(str(time[2]))
        else:
            f.write("no")
        f.close()
        s.close()
    elif help=="make folder":
        say("say the folder name to me")
        filename1=reco()
        say("your folder is creating now")
        os.mkdir(f'C:\\Users\\Admin\\PycharmProjects\\{filename1}')
        say("your folder is created")
    elif help=="open code":
        say("i find two code editor in your system which one you want pycharm or v s code")
        var2=reco()
        if str(var2)=="pycharm":
            say("pycharm is opening")
            os.startfile('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64')
        else:
            say("v s code is opening ")
            os.startfile('C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code')
    elif help =="play music":
        say("say me name of music")
        music=reco()
        say("this music not in your system ")
        print("i searching it online...............")
        say("i searching it online")
        say("google is opening")
        file= 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        os.startfile(file)
        t.sleep(7)
        pag.write(f"play {str(music)} song")
        pag.keyDown("enter")
        t.sleep(3)
        pag.click(650,510)
        say("music is play now")
    elif help=="send email":
        try:
            say("write gmail i d whom you want to send")
            to=input(">>>>")
            say("what you want to send")
            content=reco()
            say("email is sending")
            print("email is sending..............")
            email(to,content)
            print("email success fully send")
            pag.click(1350,10)
            say("email success fully send")
        except Exception as e:
            print(e)
            print("email sending failed")
            say("email sending failed")
    elif help[0:8]=="shutdown":
        pag.alert("you system is shutdown")
        say("system is shutdown")
        t.sleep(1)
        pag.click(10, 760)
        t.sleep(1)
        pag.click(10, 700)
        t.sleep(1)
        pag.click(10, 630)
    elif help=="check status":
        tg=open("status","r")
        status=tg.readlines()
        tg.close()
        say("status is checking......")
        print("status is checking......")
        if f"{time[2]} {time[1]}\n":
            al=f"{time[2]} {time[1]}\n"
            say(f"today is {status[status.index(al) - 1]}")
            print(f"today is {status[status.index(al) - 1]}")
        else:
            print("today is nothing no birthday no anniversery")
            say("today is nothing no birthday no anniversery")
    elif help[0:7]=="restart":
        pag.alert("you system is restart")
        say("system is restart")
        t.sleep(1)
        pag.click(10, 760)
        t.sleep(1)
        pag.click(10, 700)
        t.sleep(1)
        pag.click(10, 670)
    elif help[0:5]=="sleep":
        pag.alert("you system is sleep")
        say("system is sleep")
        t.sleep(1)
        pag.click(10, 760)
        t.sleep(1)
        pag.click(10, 700)
        t.sleep(1)
        pag.click(10, 630)
    elif help in  ['open calculator', 'open calendar', 'open PowerPoint', 'open WordPad', 'open Excel', 'open Microsoft store', 'open setting','open settings',
                      'open file explorer']:
        item1=help[5:len(help)+1]
        print(f"now {item1} is opening................")
        say(f"now {item1} is opening................")
        pag.click(100, 768)
        t.sleep(2)
        pag.write(item1)
        pag.keyDown("enter")
    elif help=="make a note":
        say("your note maker open")
        os.startfile('C:\\Users\\Admin\\PycharmProjects\\gui project\\notes maker\\notes without console.pyw')
        say("write your note here")
    elif help=="open games":
        say("there is three game which one you want to play")
        import pyautogui as pg
        ch=pg.confirm("name of game", buttons=['snake water gun', 'guess the number', 'stone paper sessior'])
        if ch=='snake water gun':
            po='gui project\\snakewatergun\\snakewatergun.py'
        elif ch=='stone paper sessior':
            po='gui project\\stonepapersessior\\stonepapersessior.py'
        else:
            po='gui project\\guessthenumber\\guessthenumber.py'
        say("your games open")
        os.startfile(f'C:\\Users\\Admin\\PycharmProjects\\{po}')
        say("play games here")
    elif help=="open file":
        say("say the file name to me")
        var3=reco()
        lists=["c:\\","C:\\client","C:\\client\\healthproject",'C:\\Users\\Admin','C:\\Users\\Admin\\Pictures','C:\\Users\\Admin\\PycharmProjects','C:\\Users\\Admin\\PycharmProjects\\AI','C:\\Users\\Admin\PycharmProjects\\normal','C:\\Users\\Admin\\Documents','C:\\Users\\Admin\\Downloads']
        for item2 in lists:
            try:
                os.startfile(f'{item2}\\{var3}')
                say(f"{var3} is opening")
                break
            except:
                pass
        else:
            print(f"{var3} not exist in your system")
            say(f"{var3} not exist in your system")
    elif help=="set alarm":
        print(f"now alarm clock is opening................")
        say(f"now alarm clock is opening................")
        pag.click(100, 768)
        t.sleep(2)
        pag.write('alarms & clock')
        pag.keyDown("enter")
        t.sleep(3)
        say("set your alarm")
    elif help=="take a screenshot":
        say("now screen short is taken")
        img=pag.grab()
        say("now screen short is show to you")
        img.show()
        t.sleep(5)
        pag.click(1350, 10)
        say("name to save screen shot")
        var4=reco()
        img.save(f"{str(var4)}.jpg")
    elif help[0:5]=="close":
        say(f"{help[6:len(help)+1]} is closing")
        pag.click(1350,10)
    elif help[0:8]=="minimise":
        say(f"{help[6:len(help) + 1]} is minimise")
        pag.click(1270,0)
    elif help[0:6]=="short":
        say(f"{help[6:len(help) + 1]} is short")
        pag.click(1170,0)
    elif help=="click photo":
        print(f"now camera is opening................")
        say(f"now camera is opening................")
        pag.click(100, 768)
        t.sleep(2)
        pag.write('camera')
        pag.keyDown("enter")
        t.sleep(3)
        say("your photo is click in 5 second")
        t.sleep(5)
        pag.click(1340,395)
        t.sleep(2)
        pag.click(1350, 10)
        say("your photo is clicked")
    elif help=="start video recording":
        print(f"now camera is opening................")
        say(f"now camera is opening................")
        pag.click(100, 768)
        t.sleep(2)
        pag.write('camera')
        pag.keyDown("enter")
        t.sleep(3)
        say("your video recording is start in 5 second")
        t.sleep(5)
        pag.click(1358,310)
        t.sleep(3)
        pag.click(1340, 395)
        pag.confirm("you want to stop recording",buttons=["stop"])
        pag.click(1340, 395)
        t.sleep(2)
        pag.click(1350, 10)
        say("your video is recorded")
    elif help[0:4]=="wait":
        say("for how much time in second")
        ti=int(reco())
        say(f"ok sir i wait for {ti} second")
        pag.countdown(ti)
        say("sir sleeping time up")
    else:
        if "open" == help[0:4] and len(list(help))==2:
            if help[5:11]=="google":
                say("google is opening")
                file = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(file)
            else:
                opensite(help)
        else:
            say(f"now {help} is searching online")
            say("now google is opening")
            file = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(file)
            t.sleep(5)
            pag.write(help)
            pag.keyDown("enter")
            t.sleep(3)
            pag.click(650, 610)
            say("i got the result")
    say("any other help sir")
    choice=reco()
    if choice=="no":
        break
    else:
        continue
say(f"thankyou {username} sir for use me ")
import pyautogui as pg
pg.alert(f"thankyou {username} sir for use me")
