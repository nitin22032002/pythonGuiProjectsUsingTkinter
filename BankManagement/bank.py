import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from guifunction import *
root=Tk()
currentdirectory=os.getcwd()
#currentdirectory=os.path.dirname(os.getcwdb())
root.title('ONLINE BANK')
root.minsize(660,360)
os.chdir(f'{currentdirectory}\\images required')
image=images('bank.jpg')
image1=images('green background.jpg')
image2=images('background2.png')
image3=images('background3.jpg')
image4=images('background4.jpg')
image5=images('background5.png')
image6=images('background6.jpg')
image7=images('background7.jpg')
image8=images('background8.jpg')
image9=images('background9.jpg')
root.wm_iconphoto(False,image)
def startup(event):
    text=event.widget.cget('text')
    deleted(*list2)
    if text=='NEW ACCOUNT':
        global list3,signbutton,imagebutton,gender,name,gardienname,address,dob,mobile,emailid,idname,idnumber,nominename
        root.maxsize(1366,760)
        root.geometry('1366x760')
        background3 = lableimage(image3,10)
        background3.pack()
        mainlable=lables("APPLICATION FORM FOR NEW ACCOUNT",10,20,'orange','green')
        mainlable.place(x=450,y=20)
        namelable=lable('NAME',1,20)
        namelable.place(x=20,y=90)
        gardiennamelable = lable('GARDIEN NAME', 1, 20)
        gardiennamelable.place(x=20, y=160)
        doblable = lable('DATE OF BIRTH', 1, 20)
        doblable.place(x=20, y=230)
        addresslable = lable('ADDRESS', 1, 20)
        addresslable.place(x=20, y=300)
        mobilelable = lable('MOBILE NUMBER', 1, 20)
        mobilelable.place(x=20, y=370)
        emailidlable = lable('Email ID', 1, 20)
        emailidlable.place(x=20, y=440)
        nominenamelable = lable('NOMINE NAME', 1, 20)
        nominenamelable.place(x=20, y=510)
        idnamelable = lable('ID PROOF NAME', 1, 20)
        idnamelable.place(x=20, y=580)
        idnumberlable = lable('ID PROOF NUMBER', 1, 20)
        idnumberlable.place(x=20, y=650)
        nameentry,name=entry(10,15)
        nameentry.place(x=120,y=85)
        gardiennameentry, gardienname = entry(10, 15)
        gardiennameentry.place(x=250, y=155)
        dobentry, dob = entry(10, 15)
        dobentry.place(x=255, y=225)
        addressentry, address = entry(10, 15)
        addressentry.place(x=170, y=295)
        mobileentry, mobile = entry(10, 15)
        mobileentry.place(x=270, y=365)
        emailidentry, emailid = entry(10, 15)
        emailidentry.place(x=160, y=435)
        nominenameentry, nominename = entry(10, 15)
        nominenameentry.place(x=250, y=505)
        idnameentry, idname = entry(10, 15)
        idnameentry.place(x=260, y=575)
        idnumberentry, idnumber = entry(10, 15)
        idnumberentry.place(x=300, y=645)
        submitbutton=buttons('SUBMIT',10,20,'grey','black',submit)
        submitbutton.place(x=1205,y=620)
        global imagebutton,signbutton
        imagebutton = buttons('UPLOAD PHOTO size 100x100', 10, 10, 'grey', 'black', photo)
        imagebutton.place(x=1100, y=110)
        signbutton = buttons('UPLOAD SIGN size 100x100', 10, 10, 'grey', 'black', photo)
        signbutton.place(x=1100, y=220)
        idname.set('AADHAR CARD')
        genderlable=lable('GENDER',10,15)
        genderlable.place(x=600,y=645)
        genderentry,gender=entry(10,15)
        genderentry.place(x=730,y=645)
        list3=[nameentry,genderentry,genderlable,namelable,gardiennameentry,dobentry,doblable,background3,mainlable,gardiennamelable,addressentry,addresslable,nominenameentry,nominenamelable,mobileentry,mobilelable,emailidentry,emailidlable,idnameentry,idnamelable,idnumberentry,idnumberlable,submitbutton]
    elif text=="DEPOSIT":
        global list7,depositaccount,depositdigitalpin,depositname,background6
        background6=lableimage(image6,10)
        background6.pack()
        depositaccountlable=lable("ACCOUNT NUMBER",5,20)
        depositaccountlable.place(x=130,y=140)
        depositdigitalpinlable = lable("DIGITAL PIN", 5, 20)
        depositdigitalpinlable.place(x=130, y=280)
        depositnamelable = lable("NAME", 5, 20)
        depositnamelable.place(x=130, y=420)
        depositaccountentry,depositaccount=entry(10,20)
        depositaccountentry.place(x=420,y=135)
        depositdigitalpinentry, depositdigitalpin = password(10, 20)
        depositdigitalpinentry.place(x=330, y=275)
        depositnameentry, depositname = entry(10, 20)
        depositnameentry.place(x=240, y=415)
        nextbutton3=buttons("NEXT",10,20,'grey','black',deposit)
        nextbutton3.place(x=720,y=460)
        list7=[depositaccountentry,depositaccountlable,depositdigitalpinentry,depositdigitalpinlable,depositnameentry,depositnamelable,nextbutton3]
    elif text=="WITHDRAW":
        global list9, withdrawpin, withdrawdigitalpin, withdrawname,withdrawcard,background7
        background7 = lableimage(image7, 10)
        background7.pack()
        withdrawcardlable=lable("CARD NUMBER",5,20)
        withdrawcardlable.place(x=130,y=150)
        withdrawpinlable = lable("SECURITY PIN", 5, 20)
        withdrawpinlable.place(x=130, y=250)
        withdrawdigitalpinlable = lable("DIGITAL PIN", 5, 20)
        withdrawdigitalpinlable.place(x=130, y=350)
        withdrawnamelable = lable("NAME", 5, 20)
        withdrawnamelable.place(x=130, y=450)
        withdrawcardentry,withdrawcard=entry(10,20)
        withdrawcardentry.place(x=370,y=145)
        withdrawpinentry, withdrawpin = password(10, 20)
        withdrawpinentry.place(x=350, y=245)
        withdrawdigitalpinentry, withdrawdigitalpin = password(10, 20)
        withdrawdigitalpinentry.place(x=390, y=345)
        withdrawnameentry, withdrawname = entry(10, 20)
        withdrawnameentry.place(x=240, y=445)
        nextbutton4 = buttons("NEXT", 10, 20, 'grey', 'black', withdraw)
        nextbutton4.place(x=720, y=460)
        list9 = [withdrawdigitalpinentry,withdrawcardentry,withdrawcardlable,withdrawdigitalpinlable,withdrawnameentry,withdrawnamelable,withdrawpinentry,withdrawpinlable,nextbutton4]
    elif text=="DIGITAL PASSBOOK":
        global list12, passbookpin, passbookdigitalpin, passbookname,passbookaccount,background8
        background8 = lableimage(image8, 10)
        background8.pack()
        passbookaccountlable=lable("ACCOUNT NUMBER",5,20)
        passbookaccountlable.place(x=130,y=120)
        passbookpinlable = lable("SECURITY PIN", 5, 20)
        passbookpinlable.place(x=130, y=220)
        passbookdigitalpinlable = lable("DIGITAL PIN/CVV", 5, 20)
        passbookdigitalpinlable.place(x=130, y=320)
        passbooknamelable = lable("NAME", 5, 20)
        passbooknamelable.place(x=130, y=420)
        passbookaccountentry,passbookaccount=entry(10,20)
        passbookaccountentry.place(x=420,y=115)
        passbookpinentry, passbookpin = password(10, 20)
        passbookpinentry.place(x=350, y=215)
        passbookdigitalpinentry, passbookdigitalpin = password(10, 20)
        passbookdigitalpinentry.place(x=390, y=315)
        passbooknameentry, passbookname = entry(10, 20)
        passbooknameentry.place(x=240, y=415)
        nextbutton6 = buttons("NEXT", 10, 20, 'grey', 'black', passbook)
        nextbutton6.place(x=720, y=460)
        list12=[nextbutton6,passbookaccountlable,passbookaccountentry,passbookpinentry,passbookpinlable,passbookdigitalpinentry,passbookdigitalpinlable,passbooknameentry,passbooknamelable]
    else:
        global list15,createaccount,createcvv,createdigitalpin,createcard,background9
        background9=lableimage(image9,10)
        background9.pack()
        createcardlable=lable("CARD NUMBER",5,25)
        createcardlable.place(x=130,y=100)
        createaccountlable=lable("ACCOUNT NUMBER",5,25)
        createaccountlable.place(x=130,y=200)
        createcvvlable=lable("CVV NUMBER",5,25)
        createcvvlable.place(x=130,y=300)
        createdigitalpinlable=lable("DIGITAL PIN",5,25)
        createdigitalpinlable.place(x=130,y=400)
        nextbutton9 = buttons("NEXT", 10, 20, 'grey', 'black',createpins)
        nextbutton9.place(x=723.5, y=457.5)
        createcardentry,createcard = entry(10,20)
        createcardentry.place(x=410, y=97)
        createaccountentry,createaccount = entry(10,20)
        createaccountentry.place(x=470, y=197)
        createcvventry,createcvv = password(10,20)
        createcvventry.place(x=400, y=297)
        createdigitalpinentry,createdigitalpin = password(10,20)
        createdigitalpinentry.place(x=370, y=397)
        list15=[createcardlable,createcvventry,nextbutton9,createcardentry,createaccountentry,createaccountlable,createcvvlable,createdigitalpinentry,createdigitalpinlable]
def createpins(event):
    global myuser
    tem=0
    os.chdir(f"{currentdirectory}")
    myuser=fetchdata("AccountNumber",createaccount.get())
    try:
        if(myuser==False and createaccount.get()!="" ):
            os.chdir(f"{currentdirectory}//client data//bank client data")
            with open("client detail", "r") as file1:
                codelist = file1.readlines()
            if f"{createaccount.get()}\n" in codelist and len(createaccount.get()) == 16:
                global varcode
                index = codelist.index(f"{createaccount.get()}\n")
                varcode = str(codelist[index + 1])
                os.chdir(str(currentdirectory))
                os.chdir(f"{currentdirectory}//client data//client personal data")
                with open(f"{int(str(varcode))}{createaccount.get()}", "r") as file2:
                    global mainlist, gmail
                    mainlist = file2.readlines()
                    checkpin = int(str(str(mainlist[17])[14:18]))
                    checkcardnumber = int(str(str(mainlist[20])[14:28]))
                    checkcvv=(str(str(mainlist[21])[13:16]))
                    gmail = str(mainlist[5])
                    gmail = gmail[12:len(gmail) - 1]
                    tem=1
            else:
                pg.alert("your enter account number not exist in bank system".upper())
                createaccount.set("")
        else:
            if(myuser==True or createaccount.get()==""):
                pg.alert("your enter account number not exist in bank system".upper())
                createaccount.set("")
            else:
                tem=1
                checkpin=myuser['digitalpin']
                checkcardnumber=myuser['cardnumber']
                checkcvv=myuser['cardcvvnumber']
                gmail=myuser["emailid"]
        if(tem==1):
            if str(checkpin) == str(createdigitalpin.get()):
                if str(checkcardnumber) == str(createcard.get()):
                    if str(checkcvv)==str(createcvv.get()):
                        global list16, createotp, randomotp
                        deleted(*list15)
                        import random
                        randomotp = random.randint(1000, 9999)
                        import pyttsx3 as px
                        px.speak("otp is send on your provided gmail")
                        import smtplib as sms
                        try:
                            message = MIMEText(f"YOUR OTP FOR VERIFICATION IS {randomotp}")
                            message['From'] = 'host@gmail.com'
                            message['To'] = str(gmail)
                            message['Subject'] = "ONLINE BANK VERIFICATION FOR CREATE PIN"
                            server = sms.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login('host@gmail.com', 'password')
                            textsend = message.as_string()
                            server.sendmail('host@gmail.com', str(gmail), textsend)
                            server.quit()
                        except:
                            createpins(event=1)
                        createotplable = lable("OTP", 10, 20)
                        createotplable.place(x=130, y=120)
                        createotpentry, createotp = password(10, 20)
                        createotpentry.place(x=250, y=120)
                        otpsubmitbutton = buttons("SUBMIT", 10, 20, 'grey', 'black', createotpsubmit)
                        otpsubmitbutton.place(x=600, y=115)
                        list16 = [otpsubmitbutton, createotpentry, createotplable]
                        os.chdir(str(currentdirectory))
                    else:
                        pg.alert("YOUR ENTER CVV IS INCORRECT")
                        createcvv.set("")
                else:
                    pg.alert("your enter card number is incorrect".upper())
                    createcard.set("")
            else:
                pg.alert("your enter digital pin is incorrect".upper())
                createdigitalpin.set("")
    except Exception as e:
        pg.alert('NO ACCOUNT IS OPEN YET IN ONLINE BANK')
        deleted(*list15)
        background9.destroy()
        frame1(event=1)
def createotpsubmit(event):
    if str(randomotp)==str(createotp.get()):
        global list17,createpin,createconfirmpin
        deleted(*list16)
        createpinlable = lable('SECURITY PIN', 10, 20)
        createpinlable.place(x=130, y=190)
        createpinentry, createpin = password(10, 15)
        createpinentry.place(x=400, y=195)
        createconfirmpinlable = lable('CONFIRM SECURITY PIN', 10, 20)
        createconfirmpinlable.place(x=130, y=330)
        createconfirmpinentry, createconfirmpin = password(10, 15)
        createconfirmpinentry.place(x=510, y=335)
        submitbutton5 = buttons("SUBMIT", 10, 20, "grey", 'black', finalcreatesubmit)
        submitbutton5.place(x=700, y=457.5)
        list17=[createpinentry,background9,createpinlable,createconfirmpinentry,createconfirmpinlable,submitbutton5]
    else:
        pg.alert("YOUR ENTER OTP IS INCORRECT")
def finalcreatesubmit(event):
    if createconfirmpin.get()!="" and createpin.get()!="" and len(createconfirmpin.get())==4 and createconfirmpin.get()==createpin.get():
        deleted(*list17)
        frame1(event=1)
        os.chdir(str(currentdirectory))
        if(myuser==False):
            os.chdir(f"{currentdirectory}//client data//client personal data")
            mainlist[10]=f"SECURIY PIN : {createpin.get()}\n"
            with open(f"{int(str(varcode))}{createaccount.get()}", "w") as file2:
                for item in mainlist:
                    file2.write(item)
            os.chdir(str(currentdirectory))
        else:
            update("securitypin", myuser["AccountNumber"],createpin.get())
            pg.alert("PIN update successfully")
    else:
        pg.alert("PLEASE MAKE VALID PIN")
def passbook(event):
    global myuser
    tem=0
    os.chdir(f"{currentdirectory}")
    myuser=fetchdata("AccountNumber",str(passbookaccount.get()))
    try:
        if(myuser==False and str(passbookaccount.get())!=""):
            os.chdir(f"{currentdirectory}//client data//bank client data")
            with open("client detail", "r") as file1:
                codelist = file1.readlines()
            if f"{passbookaccount.get()}\n" in codelist and len(passbookaccount.get()) == 16:
                global varcode
                index = codelist.index(f"{passbookaccount.get()}\n")
                varcode = str(codelist[index +1])
                os.chdir(str(currentdirectory))
                os.chdir(f"{currentdirectory}//client data//client personal data")
                with open(f"{int(str(varcode))}{passbookaccount.get()}", "r+") as file2:
                    global mainlist,gmail
                    mainlist = file2.readlines()
                    file2.write(f"{passbookname.get().upper()} CHECK TRANSACTION DETAIL ON {time.asctime(time.localtime(time.time()))}\n")
                    checkpin = int(str(str(mainlist[17])[14:18] + str(mainlist[21])[13:16]))
                    checkcardpin = int(str(str(mainlist[10])[14:18]))
                    gmail = str(mainlist[5])
                    gmail = gmail[12:len(gmail) - 1]
                    tem=1
            else:
                pg.alert("your enter account number not exist in bank system".upper())
                passbookaccount.set("")
        else:
            if(myuser==True or passbookaccount.get()==""):
                pg.alert("your enter account number not exist in bank system".upper())
                passbookaccount.set("")
            else:
                checkpin=myuser["digitalpin"]
                checkcvv=myuser["cardcvvnumber"]
                checkcardpin=myuser["securitypin"]
                gmail=myuser["emailid"]
                tem=1
        if(tem==1):
            if str(checkpin) == str(passbookdigitalpin.get()) or str(checkcvv) == str(passbookdigitalpin.get()):
                if str(checkcardpin) == str(passbookpin.get()):
                    global list13, passbookotp, randomotp
                    deleted(*list12)
                    import random
                    randomotp = random.randint(1000, 9999)
                    import pyttsx3 as px
                    px.speak("otp is send on your provided gmail")
                    import smtplib as sms
                    try:
                        message = MIMEText(f"YOUR OTP FOR VERIFICATION IS {randomotp}")
                        message['From'] = 'host@gmail.com'
                        message['To'] = str(gmail)
                        message['Subject'] = "ONLINE BANK VERIFICATION"
                        server = sms.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login('host@gmail.com', 'password')
                        textsend = message.as_string()
                        server.sendmail('host@gmail.com', str(gmail), textsend)
                        server.quit()
                    except:
                        passbook(event=1)
                    passbookotplable = lable("OTP", 10, 20)
                    passbookotplable.place(x=130, y=120)
                    passbookotpentry, passbookotp = password(10, 20)
                    passbookotpentry.place(x=250, y=120)
                    otpsubmitbutton = buttons("SUBMIT", 10, 20, 'grey', 'black', passbookotpsubmit)
                    otpsubmitbutton.place(x=600, y=115)
                    list13 = [otpsubmitbutton, passbookotpentry, passbookotplable]
                    os.chdir(str(currentdirectory))
                else:
                    pg.alert("your enter security pin is incorrect".upper())
                    passbookpin.set("")
            else:
                pg.alert("your enter digital pin is incorrect".upper())
                passbookdigitalpin.set("")
    except Exception as e:
        print(e)
        pg.alert("NO ACCOUNT IS OPEN YET IN ONLINE BANK")
        deleted(*list12)
        background8.destroy()
        frame1(event=1)
def passbookotpsubmit(event):
    if str(randomotp) == passbookotp.get():
        global list14
        if(myuser==False):
            tran=list(mainlist[24:len(mainlist)])
            transaction=f"\t\tTRANSACTION DETAILS\n{mainlist[12]}\n"
        else:
            tran=showpassbook(myuser["AccountNumber"])
            insertdata(myuser["AccountNumber"],str(passbookname.get()))
            transaction=f"\t\tTRANSACTION DETAILS\n{myuser['currentbalance']} Rs\n"
            tran.insert(0,[1,'Name',"Date and Time","\tDeposit","Withdraw",'\tCurrentBalance    ',"Status"])
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        # create a cell
        #pdf.cell(200, 10, txt="TRANSACTION STATEMENT",
                # ln=1, align='C')
        for item in tran:
            item=("\t".join(item[1:]))+"\n"
            transaction=transaction+item
            lis=[]
            lis.append(item)
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=item,
                 ln=len(lis), align='C')
        pdf.output("file.pdf")
        mail(transaction[1:len(transaction)],str(gmail),'BANK STATEMENT')
        os.remove(f"{currentdirectory}\\file.pdf")
        deleted(*list13)
        root.maxsize(1200,660)
        root.minsize(1200,660)
        root.geometry("923x660")
        showlable = lables(transaction, 30, 19, "grey", "black")
        showlable.place(x=10,y=10)
        nextbutton7 = buttons('NEXT', 20, 20, 'grey', 'black', passbooksubmit)
        nextbutton7.place(x=1205, y=620)
        list14 = [background8,showlable,nextbutton7]
    else:
        pg.alert("YOUR ENTER OTP IS INCORRECT")
def passbooksubmit(event):
    deleted(*list14)
    frame1(event=1)
def withdraw(event):
    global myuser
    tem=0
    os.chdir(f"{currentdirectory}")
    myuser = fetchdata("cardnumber", str(withdrawcard.get()))
    try:
        if(myuser==False and withdrawcard.get()!=""):
            os.chdir(f"{currentdirectory}//client data//bank client data")
            with open("client detail", "r") as file1:
                codelist = file1.readlines()
            if f"{withdrawcard.get()}\n" in codelist and len(withdrawcard.get())==14:
                global varcode,varaccount
                index = codelist.index(f"{withdrawcard.get()}\n")
                varcode = str(codelist[index - 1])
                varaccount = str(codelist[index - 2])
                os.chdir(str(currentdirectory))
                os.chdir(f"{currentdirectory}//client data//client personal data")
                with open(f"{int(str(varcode))}0{int(str(varaccount))}", "r") as file2:
                    global mainlist
                    mainlist = file2.readlines()
                    checkpin = int(str(str(mainlist[17])[14:18]+str(mainlist[21])[13:16]))
                    checkcardpin = int(str(str(mainlist[10])[14:18]))
                    gmail=str(mainlist[5])
                    gmail=gmail[12:len(gmail)-1]
                    tem=1
            else:
                pg.alert("your enter card number not exist in bank system".upper())
                withdrawcard.set("")
        else:
            if(myuser==True or withdrawcard.get()==""):
                pg.alert("your enter card number not exist in bank system".upper())
                withdrawcard.set("")
            else:
                checkpin = myuser["digitalpin"]
                checkcardpin = myuser["securitypin"]
                gmail = myuser["emailid"]
                tem=1
        if(tem==1):
                if str(checkpin) == str(withdrawdigitalpin.get()) and withdrawname.get()!="":
                    if str(checkcardpin)==str(withdrawpin.get()) :
                        global list10,withdrawotp,randomotp
                        deleted(*list9)
                        import random
                        randomotp=random.randint(1000,9999)
                        import pyttsx3 as px
                        px.speak("otp is send on your provided gmail")
                        import smtplib as sms
                        try:
                            message=MIMEText(f"YOUR OTP FOR VERIFICATION IS {randomotp}")
                            message['From']='host@gmail.com'
                            message['To']=str(gmail)
                            message['Subject']="ONLINE BANK VERIFICATION"
                            server = sms.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login('host@gmail.com', 'password')
                            textsend=message.as_string()
                            server.sendmail('host@gmail.com', str(gmail),textsend)
                            server.quit()
                        except:
                            withdraw()
                        withdrawotplable=lable("OTP",10,20)
                        withdrawotplable.place(x=130,y=120)
                        withdrawotpentry,withdrawotp=password(10,20)
                        withdrawotpentry.place(x=250,y=120)
                        otpsubmitbutton=buttons("SUBMIT",10,20,'grey','black',otpsubmit)
                        otpsubmitbutton.place(x=600,y=115)
                        list10 = [otpsubmitbutton, withdrawotpentry, withdrawotplable]
                        os.chdir(str(currentdirectory))
                    else:
                        pg.alert("your enter security pin is incorrect".upper())
                        root.quit()
                else:
                    pg.alert("your enter digital pin + ccv is incorrect or name place is empty".upper())
                    depositdigitalpin.set("")
    except:
        pg.alert("NO ACCOUNT IS OPEN YET IN ONLINE BANK")
        deleted(*list9)
        background7.destroy()
        frame1(event=1)
def otpsubmit(event):
    if str(randomotp)==withdrawotp.get():
        global list11, currentamount,withdrawcash
        deleted(*list10)
        if(myuser==False):
            currentamount = str(mainlist[12])
            currentcashlable = lables(
                f"YOUR CURRENT ACCOUNT BALANCE IS {str(currentamount[17:len(currentamount)-1])}", 10, 20, 'grey',
                'black')
        else:
            currentamount = myuser["currentbalance"]
            currentcashlable = lables(
                f"YOUR CURRENT ACCOUNT BALANCE IS {currentamount} Rs", 10, 20, 'grey',
                'black')
        currentcashlable.place(x=100, y=50)
        withdrawcashlable = lable("AMOUNT IN RUPEES WITHDRAW", 5, 25)
        withdrawcashlable.place(x=80, y=150)
        withdrawcashentry, withdrawcash = password(10, 20)
        withdrawcashentry.place(x=500, y=220)
        nextbutton5 = buttons("NEXT", 10, 20, 'grey', 'black', finalwithdraw)
        nextbutton5.place(x=720, y=460)
        list11=[background7,currentcashlable,withdrawcashlable,withdrawcashentry,nextbutton5]
    else:
        pg.alert("YOUR ENTER OTP IS INCORRECT")
def finalwithdraw(event):
    if(myuser==False):
        os.chdir(f"{currentdirectory}//client data//client personal data")
        amt=int(str(currentamount[17:len(currentamount) - 3]))
    else:
        amt=int(myuser["currentbalance"])
    if withdrawcash.get()!="" and withdrawcash.get().isnumeric() and int(withdrawcash.get())>0 and int(withdrawcash.get())<amt:
        import pyttsx3 as px
        px.speak(" your transaction is success ful")
        deleted(*list11)
        currentamount1 = amt - int(withdrawcash.get())
        if(myuser==False):
            mainlist[12] = f"CURRENT AMOUNT : {currentamount1} RS\n"
            mainlist.append(f"{withdrawname.get().upper()} WITHDRAW {withdrawcash.get()} RS on {time.asctime(time.localtime(time.time()))}\n")
            with open(f"{int(str(varcode))}0{int(str(varaccount))}", "w") as file2:
                for item in mainlist:
                    file2.write(item)
        else:
            withdrawdata(myuser["cardnumber"],str(withdrawcash.get()) ,withdrawname.get().upper())
        frame1(event=1)
    else:
        pg.alert("ENTER VALID AMOUNT")
        withdrawcash.set("")
    os.chdir(str(currentdirectory))
def deposit(event):
    tem=0
    os.chdir(f"{currentdirectory}")
    global myuser
    myuser=fetchdata("AccountNumber",depositaccount.get())
    try:
        if(myuser==False and depositaccount.get()!=""):
            os.chdir(f"{currentdirectory}//client data//bank client data")
            with open("client detail","r") as file1:
                codelist=file1.readlines()
            if f"{depositaccount.get()}\n" in codelist and len(depositaccount.get())==16 and depositname.get()!="":
                global varcode
                index=codelist.index(f"{depositaccount.get()}\n")
                varcode=str(codelist[index+1])
                os.chdir(str(currentdirectory))
                os.chdir(f"{currentdirectory}//client data//client personal data")
                with open(f"{int(str(varcode))}{depositaccount.get()}","r") as file2:
                    global mainlist
                    mainlist=file2.readlines()
                    checkpin=int(str(str(mainlist[17])[14:18]))
                    tem=1
            else:
                pg.alert("your enter account number not exist in bank system or name field is empty".upper())
                depositaccount.set("")
        else:
            if(myuser==False or depositaccount.get()=="" or depositname.get()==""):
                pg.alert("your enter account number not exist in bank system or name field is empty".upper())
                depositaccount.set("")
            else:
                checkpin=myuser["digitalpin"]
                tem=1
        if(tem==1):
                if str(checkpin)==str(depositdigitalpin.get()):
                    global list8,depositcash,currentamount
                    deleted(*list7)
                    if(myuser==False):
                        currentamount=str(mainlist[12])
                        currentcashlable=lables(f"YOUR CURRENT ACCOUNT BALANCE IS {str(currentamount[17:len(currentamount)-1])}",10,20,'grey','black')
                    else:
                        currentamount=str(myuser["currentbalance"])
                        currentcashlable=lables(f"YOUR CURRENT ACCOUNT BALANCE IS {currentamount} Rs",10,20,'grey','black')
                    currentcashlable.place(x=130,y=120)
                    depositcashlable = lable("AMOUNT IN RUPEES", 5, 25)
                    depositcashlable.place(x=130, y=230)
                    depositcashentry, depositcash = entry(10, 20)
                    depositcashentry.place(x=490, y=225)
                    nextbutton4 = buttons("NEXT", 10, 20, 'grey', 'black', finaldeposit)
                    nextbutton4.place(x=720, y=460)
                    list8=[currentcashlable,depositcashentry,depositcashlable,background6]
                    os.chdir(str(currentdirectory))
                else:
                    pg.alert("your enter digital pin is incorrect".upper())
                    depositdigitalpin.set("")
    except:
        pg.alert("NO ACCOUNT IS OPEN YET IN ONLINE BANK")
        deleted(*list7)
        background6.destroy()
        frame1(event=1)
def finaldeposit(event):
    if(myuser==False):
        os.chdir(f"{currentdirectory}//client data//client personal data")
        currentamount1 = int(str(currentamount[17:len(currentamount)-3])) + int(depositcash.get())
    if depositcash.get()!="" and depositcash.get().isnumeric() and int(depositcash.get())>0:
        import pyttsx3 as px
        px.speak(" your transaction is success ful")
        deleted(*list8)
        if(myuser==False):
            mainlist[12] = f"CURRENT AMOUNT : {currentamount1} RS\n"
            mainlist.append(f"{depositname.get().upper()} DEPOSIT {depositcash.get()} RS on {time.asctime(time.localtime(time.time()))}\n")
            with open(f"{int(str(varcode))}{depositaccount.get()}", "w") as file2:
                for item in mainlist:
                        file2.write(str(item))
        else:
            depositdata(myuser["AccountNumber"],int(depositcash.get()),depositname.get().upper())
        frame1(event=1)
    else:
        pg.alert("ENTER VALID AMOUNT")
        depositcash.set("")
    os.chdir(str(currentdirectory))
def submita():
    global list4,pin,confirmpin,cash
    deleted(*list3)
    try:
        deleted(*[signsuccesslable, imagesuccesslable])
    except:
        signbutton.destroy()
        imagebutton.destroy()
    root.geometry('1366x760')
    root.maxsize(1366, 760)
    root.minsize(1366, 760)
    background4 = lableimage(image4, 10)
    background4.pack()
    mainlable2 = lables("MAKE SECURITY PIN OF ATM CARD", 10, 25, 'yellow', 'blue')
    mainlable2.place(x=390, y=20)
    cashlable = lable('INITIAL AMOUNT DEPOSIT', 10, 20)
    cashlable.place(x=30, y=250)
    cashentry,cash=entry(10,15)
    cashentry.place(x=447,y=255)
    pinlable = lable('SECURITY PIN', 10, 20)
    pinlable.place(x=30, y=390)
    pinentry, pin = password(10, 15)
    pinentry.place(x=300, y=395)
    confirmpinlable = lable('CONFIRM SECURITY PIN', 10, 20)
    confirmpinlable.place(x=30, y=530)
    confirmpinentry, confirmpin = password(10, 15)
    confirmpinentry.place(x=410, y=535)
    submitbutton2=buttons("SUBMIT",10,20,"grey",'black',finalsubmit)
    submitbutton2.place(x=550,y=620)
    list4=[cashlable,cashentry,mainlable2,background4,pinentry,pinlable,confirmpinlable,confirmpinentry,submitbutton2]
def finalsubmit(event):
    global timeopening
    try:
        import time as t
        import pyautogui as pg
        timeopening = t.asctime(t.localtime(t.time()))
        if cash.get() != "" and int(cash.get()) >= 500:
            if pin.get().isnumeric() and len(pin.get()) == 4:
                if pin.get() == confirmpin.get():
                    import pyttsx3
                    deleted(*list4)
                    pyttsx3.speak("your account is create success fully")
                    finalframe()
                else:
                    pg.alert("YOUR PIN AND CONFIRM PIN NOT MATCH")
                    pin.set("")
                    confirmpin.set("")
            else:
                pg.alert("YOUR PIN SHOULD CONTAIN 4 DIGIT NUMERIC CHARACTER ONLY")
                pin.set("")
                confirmpin.set("")
        else:
            pg.alert("INITIAL DEPOSIT AMOUNT SHOULD BE GREATER THEN 500 RS")
            cash.set("00")
    except:
        pass
def finalframe():
    global list6,accountnumber,cvvnumber,cardnumber,digitalpin,customerid,validdate,expiredate
    background5=lableimage(image5,10)
    background5.pack()
    from random import randint as rt,choice as ch
    accountnumber=f"0 5 4 5 1 0 {ch(['4','2'])} 0 0 0 0 {ch(['0','1'])} {rt(0,9)} {rt(0,9) } {rt(0,9)} {rt(0,9)}"
    accountnumberlable=lables(f"YOUR ACCOUNT NUMBER IS {accountnumber} ",10,15,'grey','black')
    accountnumberlable.place(x=50,y=30)
    accountnumber=accountnumber.replace(" ","")
    ifsccodelable=lables("IFSC CODE OF BANK IS N I T I 0 0 0 2 2 0 3",10,15,'grey','black')
    ifsccodelable.place(x=50,y=130)
    customerid=f"{rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)}"
    customeridlable=lables(f"YOUR CUSTOMER ID IS {customerid}",10,15,'grey','black')
    customeridlable.place(x=50,y=230)
    customerid=customerid.replace(" ","")
    digitalpin=f"{rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)}"
    digitalpinlable=lables(f"YOUR DIGITAL PIN IS {digitalpin} ",10,15,'grey','black')
    digitalpinlable.place(x=50,y=330)
    digitalpin=digitalpin.replace(" ","")
    cardnumber=f"{rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)} {rt(0,9)}"
    cardnumberlable=lables(f"YOUR ATM CARD NUMBER IS {cardnumber}",10,15,'grey','black')
    cardnumberlable.place(x=50,y=430)
    cardnumber=cardnumber.replace(" ","")
    cvvnumber=f"{rt(0,9)} {rt(0,9)} {rt(0,9)}"
    cvvnumberlable=lables(f"YOUR ATM CVV NUMBER IS {cvvnumber}",10,15,'grey','black')
    cvvnumberlable.place(x=50,y=530)
    cvvnumber=cvvnumber.replace(" ","")
    a=list(time.asctime(time.localtime(time.time())).split(' '))
    validdate=f"{rt(1,12)}/{a[4]}"
    validdatelable=lables(f"CARD VALID {validdate}",10,15,'grey','black')
    validdatelable.place(x=50,y=630)
    expiredate=f"{rt(1,12)}/{int(str(a[4]))+5}"
    expiredatelable=lables(f"CARD EXPIRE {expiredate}",10,15,'grey','black')
    expiredatelable.place(x=450,y=632)
    nextbutton2=buttons("NEXT",10,20,'grey','black',closeofnewaccount)
    nextbutton2.place(x=1200,y=580)
    list6 = [background5, accountnumberlable, ifsccodelable, cvvnumberlable, cardnumberlable, customeridlable,
             expiredatelable, validdatelable, digitalpinlable, nextbutton2]
    sendmailbank()
    #global list6
    list6=[background5,accountnumberlable,ifsccodelable,cvvnumberlable,cardnumberlable,customeridlable,expiredatelable,validdatelable,digitalpinlable,nextbutton2]
def closeofnewaccount(event):
    from random import randint as rt,choice as ch
    deleted(*list6)
    frame1(event=1)
    os.chdir(currentdirectory)
    clientcode=f"{rt(0,9)}{rt(0,9)}{rt(0,9)}{rt(0,9)}"
    if(not setuser()):
        try:
            os.mkdir(f"{os.getcwd()}//client data")
            os.mkdir(f"{os.getcwd()}//client data//client personal data")
            os.mkdir(f"{os.getcwd()}//client data//client photo")
            os.mkdir(f"{os.getcwd()}//client data//bank client data")
        except:
            pass
        os.chdir(f"{currentdirectory}//client data//client photo")
        photoimage.save(f"{accountnumber}.jpg")
        signimage.save(f"{accountnumber}{clientcode}.jpg")
        os.chdir(currentdirectory)
        os.chdir(f"{os.getcwd()}//client data//bank client data")
        with open("client detail","a") as file1:
            file1.write(f"{accountnumber}\n")
            file1.write(f"{client0code}\n")
            file1.write(f"{cardnumber}\n")
        os.chdir(currentdirectory)
        os.chdir(f"{os.getcwd()}//client data//client personal data")
        with open(f"{clientcode}{accountnumber}","w") as file2:
            file2.write(f"NAME : {name.get()}\n")
            file2.write(f"GARDIEN NAME : {gardienname.get()}\n")
            file2.write(f"DATE OF BIRTH : {dob.get()}\n")
            file2.write(f"GENDER : {gender.get()}\n")
            file2.write(f"MOBILE NUMBER : {mobile.get()}\n")
            file2.write(f"E MAIL ID : {emailid.get()}\n")
            file2.write(f"ADDRESS : {address.get()}\n")
            file2.write(f"NOMINE NAME : {nominename.get()}\n")
            file2.write(f"ID PROOF NAME : {idname.get()}\n")
            file2.write(f"ID PROOF NUMBER : {idnumber.get()}\n")
            file2.write(f"SECURIY PIN : {pin.get()}\n")
            file2.write(f"INTIAL AMOUNT : {cash.get()} RS\n")
            file2.write(f"CURRENT AMOUNT : {cash.get()} RS\n")
            file2.write(f"ACCOUNT NUMBER : {accountnumber}\n")
            file2.write(f"IFSC CODE OF BANK : N I T I 0 0 0 2 2 0 3\n")
            file2.write(f"CUSTOMER ID: {customerid}\n")
            file2.write(f"CLIENT ID : {clientcode}\n")
            file2.write(f"DIGITAL PIN : {digitalpin}\n")
            file2.write(f"VALID DATE : {validdate}\n")
            file2.write(f"EXPIRE DATE : {expiredate}\n")
            file2.write(f"CARD NUMBER : {cardnumber}\n")
            file2.write(f"CVV NUMBER : {cvvnumber}\n")
            file2.write(f"DATE OF OPENING ACCOUNT : {timeopening}\n")
            file2.write(f"\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS\n")
            file2.write(f"INITIAL AMOUNT DEPOSIT {cash.get()} ON {timeopening}\n")
        os.chdir(currentdirectory)
    else:
        createaccountuser(str(clientcode),name.get(),gender.get(),dob.get(),mobile.get(),emailid.get(),gardienname.get(),nominename.get(),address.get(),f"{name.get()}.jpg",idname.get(),idnumber.get(),str(timeopening),str(cash.get()),str(pin.get()),accountnumber,cardnumber,customerid,digitalpin,"N I T I 0 0 0 2 2 0 3",expiredate,validdate,cvvnumber)
def sendmailbank():
    import time
    import smtplib as sms
    try:
        os.chdir(str(currentdirectory))
        text=f"ONLINE BANK\n HI {name.get().upper()} WLECOME IN ONLINE BANK YOUR DETAIL GIVEN BELOW:\nACCOUNT NUMBER : {accountnumber}\nCUSTOMER ID : {customerid}\nCARD NUMBER : {cardnumber}\nCVV NUMBER : {cvvnumber}\nDIGITAL PIN : {digitalpin}\nIFSC CODE : N I T I 0 0 0 2 2 0 3\nVALID DATE : {validdate}\t\tEXPIRE DATE : {expiredate}\n THANKYOU FOR JOIN ONLINE BANK\n{time.asctime(time.localtime(time.time()))}"
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        # create a cell
        pdf.cell(200, 10, txt="YOUR BANK DETAILS",
                 ln=1, align='C')
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=text,
                     ln=2, align='C')
        pdf.output("file.pdf")
        mail(text,str(emailid.get()),"WELCOME IN ONLINE BANK YOUR BANK DETAILS")
        os.remove(f"{currentdirectory}\\file.pdf")
    except Exception as e:
        print(e)
        sendmailbank()
def submit(event):
    import pyautogui as pg
    date=list(dob.get().split("/"))
    if gender.get() !='' and name.get() != "" and gardienname.get() != "" and address.get() != "" and dob.get() != "" and emailid.get() != "" and nominename.get() != "" and mobile.get()!="" and idname.get() != "" and idnumber.get()!="":
        if len(mobile.get())==10 and (gender.get()=="male" or gender.get()=="female")and mobile.get().isnumeric() and len(idnumber.get())==12 and idnumber.get().isnumeric() and (emailid.get()[len(emailid.get())-10:len(emailid.get())+1]=='@gmail.com' or emailid.get()[len(emailid.get())-10:len(emailid.get())+1]=='@GMAIL.COM') :
            try:
                if int(date[0])<32 and int(date[1])<13 and 2010 >int(date[2])>1950 and date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
                    submita()
                else:
                    pg.alert("PLEASE ENTER VALID DATE OF BIRTH")
                    dob.set("")
                    #dobentry.update()
            except:
                pg.alert("PLEASE ENTER VALID DATE OF BIRTH")
                dob.set("")
                #fslable3.update()
        else:
            pg.alert("PLEASE ENTER VALID MOBILE NUMBER OR EMAIL ID OR ID NUMBER OR VALID GENDER")
    else:
        pg.alert("PLEASE FILL COMPLETE DETAIL")
def photo(event):
    from PIL import Image
    global photoimage,signimage,signsuccesslable,imagesuccesslable
    text=event.widget.cget('text')
    if text=='UPLOAD PHOTO size 100x100':
        deleted(*[imagebutton])
        a = askopenfilename()
        a = str(a)
        b = list(a.split("/"))
        d = a.replace(f"/{b[len(b) - 1]}", "", 1)
        try:
            os.chdir(d)
            photoimage = Image.open(b[len(b) - 1])
            imagesuccesslable = lables('YOUR IMAGE UPLOADED', 10, 10, 'grey', 'black')
            imagesuccesslable.place(x=1100, y=110)
        except:
            imagesuccesslable = lables('YOUR IMAGE NOT UPLOADED', 10, 10, 'grey', 'black')
            imagesuccesslable.place(x=1100, y=110)
            root.quit()
    else:
        deleted(*[signbutton])
        a=askopenfilename()
        a = str(a)
        b = list(a.split("/"))
        d=a.replace(f"/{b[len(b)-1]}","",1)
        try:
            os.chdir(d)
            signimage = Image.open(b[len(b)-1])
            signsuccesslable = lables('YOUR SIGN UPLOADED', 10, 10, 'grey', 'black')
            signsuccesslable.place(x=1100, y=220)
        except:
            signsuccesslable = lables('YOUR SIGN NOT UPLOADED', 10, 10, 'grey', 'black')
            signsuccesslable.place(x=1100, y=220)
            root.quit()
def frame1(event):
    global list2
    deleted(*list1)
    root.maxsize(850,540)
    root.minsize(850,540)
    background2=lableimage(image2,10)
    background2.pack()
    button1=buttons('NEW ACCOUNT',10,20,'grey','black',startup)
    button1.place(x=530,y=50)
    button2 = buttons('DEPOSIT', 10, 20, 'grey', 'black', startup)
    button2.place(x=530, y=150)
    button3 = buttons('WITHDRAW', 10, 20, 'grey', 'black', startup)
    button3.place(x=530, y=250)
    button4 = buttons('DIGITAL PASSBOOK', 10, 20, 'grey', 'black', startup)
    button4.place(x=510, y=350)
    button5 = buttons('CREATE PIN', 10, 20, 'grey', 'black', startup)
    button5.place(x=530, y=450)
    list2=[background2,button1,button2,button3,button4,button5]
def welcomewindow(event):
    global list1
    root.resizable(0,0)
    root.geometry('660x360')
    root.maxsize(660, 360)
    root.minsize(660, 360)
    background1 =lableimage(image1,10)
    background1.pack()
    text1=lables('WELCOME IN ONLINE BANK',10,25,'orange','green')
    text1.place(x=90,y=150)
    button1=buttons('NEXT',10,20,'green','black',frame1)
    button1.place(x=534,y=277)
    list1=[background1,text1,button1]
welcomewindow(event=1)
root.mainloop()