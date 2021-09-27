def images(name):
    from PIL import Image, ImageTk
    imagee=Image.open(name)
    imagee=ImageTk.PhotoImage(imagee)
    return imagee
def deleted(*args):
    for item in args:
        item.destroy()
def lables(text,bw,fs,bg,fg):
    l=Label(text=text,borderwidth=bw,font=f"comicsansms {fs} bold",relief=SUNKEN,bg=bg,fg=fg)
    return l
def lable(text,bw,fs):
    l=Label(text=text,borderwidth=bw,font=f"comicsansms {fs} bold",relief=SUNKEN)
    return l
def lableimage(image,bw):
    l=Label(image=image,borderwidth=bw,relief=SUNKEN)
    return l
def buttons(text,bw,fs,bg,fg,command):
    l=Button(text=text,borderwidth=bw,font=f"comicsansms {fs} bold",relief=SUNKEN,bg=bg,fg=fg)
    l.bind('<Button-1>',command)
    return l
def button(text,bw,fs,command):
    l=Button(text=text,borderwidth=bw,font=f"comicsansms {fs} bold",relief=SUNKEN)
    l.bind('<Button-1>', command)
    return l
def entry(bw,fs):
    b=StringVar()
    l=Entry(textvariable=b,borderwidth=bw,font=f"comicsansms {fs} bold",relief=SUNKEN)
    return l,b
def password(bw,fs):
    b=StringVar()
    l=Entry(textvariable=b,borderwidth=bw,show="*",font=f"comicsansms {fs} bold",relief=SUNKEN)
    return l,b
def mail(text,reciver,subject):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    mail_content =str(text)
    sender_address = '**********************'
    sender_pass = '****************'
    receiver_address = str(reciver)
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = str(subject)
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'file.pdf'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-s_name,  tream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
def setuser():
    try:
        try:bank.execute("CREATE DATABASE bank")
        except:return 1
        try:bank.execute("CREATE TABLE bank.accountdetails(userid int PRIMARY KEY,username VARCHAR(45) NOT NULL,gender VARCHAR(20) NOT NULL,dateofbirth varchar(45) NOT NULL,mobilenumber VARCHAR (45) NOT NULL,emailid varchar(45) NOT NULL,gardianname VARCHAR(45) NOT NULL,nominename varchar(45) NOT NULL ,address varchar(45) NOT NULL,photo Varchar(45) NOT NULL,idproofname varchar(45) NOT NULL,idproof varchar(45) NOT NULL,dateofopeningaccount varchar(45) NOT NULL,initialamount VARCHAR(45) NOT NULL,currentbalance varchar(45) NOT NULL ,securitypin varchar (45) NOT NULL,AccountNumber varchar(45) NOT NULL,cardnumber varchar(45) NOT NULL ,customerid varchar(45) NOT NULL,digitalpin varchar (45) NOT NULL,ifsccode varchar(45) NOT NULL,cardexpirydate varchar(45) NOT NULL,cardvaliddate varchar(45) NOT NULL ,cardcvvnumber varchar(45) NOT NULL )")
        except Exception as e:
            print(e)
            return 2
        banksqlconnect.commit()
        return True
    except:
        return False
def createaccountuser(userid, username, gender, dateofbirth, mobilenumber, emailid, gardianname,nominename ,address, photo, idproofname, idproof, dateofopeningaccount, initialamount,securitypin, AccountNumber,cardnumber,customerid, digitalpin, ifsccode,cardexpirydate,cardvaliddate,cardcvvnumber):
    try:
        val=(userid, username, gender, dateofbirth, mobilenumber, emailid, gardianname, nominename,address, photo, idproofname, idproof, dateofopeningaccount, initialamount,initialamount,securitypin, AccountNumber, cardnumber,customerid, digitalpin, ifsccode,cardexpirydate,cardvaliddate,cardcvvnumber)
        qu=f'INSERT into bank.accountdetails  (userid, username, gender, dateofbirth, mobilenumber, emailid, gardianname,nominename ,address, photo, idproofname, idproof, dateofopeningaccount, initialamount, currentbalance ,securitypin, AccountNumber, cardnumber,customerid, digitalpin, ifsccode,cardexpirydate,cardvaliddate,cardcvvnumber) values{val}'
        bank.execute(qu)
        banksqlconnect.commit()
        qy=f"CREATE TABLE bank.{AccountNumber}(transactionnumber int NOT NULL ,username varchar(45) NOT NULL ,dateoftransaction varchar(70) PRIMARY KEY ,deposit varchar(45),withdraw varchar(45),currentbalance varchar(45) NOT NULL,status varchar(45) NOT NULL)"
        bank.execute(qy)
        t=str(time.asctime(time.localtime(time.time())))
        val=(1,username,t,initialamount,"0",initialamount,"Account open")
        r=f"insert into bank.{AccountNumber} (transactionnumber,username,dateoftransaction,deposit,withdraw,currentbalance,status) values{val}"
        bank.execute(r)
        banksqlconnect.commit()
        return True
    except Exception as e:
        print(e)
        return False
def deleteaccount(accountnumber,cardnumber,securitypip,digitalpin,emailid):
    try:
        bank.execute('DELETE FROM bank.accountdetails where(AccountNumber=%s && cardnumber=%s && securitypin=%s && digitalpin=%s && emailid=%s)',(accountnumber,cardnumber,securitypip,digitalpin,emailid))
        a=f"DROP TABLE bank.{accountnumber}"
        bank.execute(a)
        banksqlconnect.commit()
        return True
    except Exception as e:
        print(e)
        return False
def current(a):
    try:
        t = f"select currentbalance from bank.accountdetails where {a}={a}"
        bank.execute(t)
        return list(bank)[0][0]
    except:
        return False
def fetchdata(a,b):
    try:
        t=f"select * from bank.accountdetails where({a}={b})"
        bank.execute(t)
        data=list(bank)
        l=("userid", "username", "gender", "dateofbirth", "mobilenumber", "emailid", "gardianname","nominename" ,"address", "photo", "idproofname", "idproof", "dateofopeningaccount", "initialamount","currentbalance", "securitypin", "AccountNumber", "cardnumber", "customerid", "digitalpin", "ifsccode","cardexpirydate","cardvaliddate","cardcvvnumber")
        data=dict(zip(l,data[0]))
        return data
    except Exception as e:
        return str(e)
def showpassbook(accountnumber):
    try:
        a=current(accountnumber)
        a=f"select * from bank.{accountnumber}"
        bank.execute(a)
        return list(bank)
    except:
        return False
def depositdata(accountnumber,balance,username):
    try:
        a=int(current(accountnumber))
        t=str(time.asctime(time.localtime(time.time())))
        b=(a+int(balance))
        a=(random.randint(120,20000),username,t,balance,"0",str(b),"Deposit")
        a=f"insert into bank.{accountnumber.lower()} (transactionnumber,username,dateoftransaction,deposit,withdraw,currentbalance,status) values{a} "
        bank.execute(a)
        banksqlconnect.commit()
        a = f"UPDATE `bank`.`accountdetails` SET `currentbalance` = {str(b)} WHERE (`AccountNumber` = {accountnumber})"
        bank.execute(a)
        banksqlconnect.commit()
        return True
    except:
        return False
def withdrawdata(cardnumber,balance,username):
    try:
        a=f"select AccountNumber from bank.accountdetails where cardnumber={cardnumber}"
        bank.execute(a)
        accountnumber=list(bank)[0][0]
        t = str(time.asctime(time.localtime(time.time())))
        a=int(current(accountnumber))
        b = (a - int(balance))
        a = (random.randint(120,20000), username, t, "0", balance, str(b),"Withdraw")
        a = f"insert into bank.{accountnumber.lower()} (transactionnumber,username,dateoftransaction,deposit,withdraw,currentbalance,status) values{a} "
        bank.execute(a)
        banksqlconnect.commit()
        a = f"UPDATE `bank`.`accountdetails` SET `currentbalance` = {str(b)} WHERE (`AccountNumber` = {accountnumber})"
        bank.execute(a)
        banksqlconnect.commit()
        return True
    except:
        return False
def insertdata(account,username):
    a = int(current(account))
    t = str(time.asctime(time.localtime(time.time())))
    a = (random.randint(120, 20000), username, t, "0", "0", a, 'PassBook Check')
    a = f"insert into bank.{account.lower()} (transactionnumber,username,dateoftransaction,deposit,withdraw,currentbalance,status) values{a} "
    bank.execute(a)
    banksqlconnect.commit()
def update(a,accountnumber,value):
    try:
        a = f"UPDATE `bank`.`accountdetails` SET `{a}` = {str(value)} WHERE (`AccountNumber` = {accountnumber})"
        bank.execute(a)
        banksqlconnect.commit()
        return True
    except Exception as e:
        print(e)
        return False
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import time
import random
import pyautogui as pg
try:
    import mysql.connector as sql
    banksqlconnect=sql.connect(
        host="localhost",
        user='root',
        password='******************',
        port=3306,
    )
    bank=banksqlconnect.cursor()
except:pass
