import pyautogui as pg
import os
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
root=Tk()
root.title("CONVERTOR")
root.geometry('750x200')
#root.maxsize(750,200)
root.minsize(750,200)
def convert():
    global l2, file1,l3,image
    try:
        file=askopenfilename()
        file=str(file)
        file1=list(file.split("/"))
        file=file.replace(f"/{file1[6]}","",1)
        l2=Label(text=file1[6],borderwidth=10,bg="grey",relief=SUNKEN,font="comicsansms 15 bold")
        l2.place(x=200,y=10)
        os.chdir(str(file))
    except:
        pass
    #root.quit()
def convert1():
    try:
        from PIL import Image,ImageTk
        text = var.get()
        image = Image.open(file1[6])
        image2=ImageTk.PhotoImage(image)
        l3=Label(image=image2,borderwidth=10)
        l3.place(x=500,y=300)
        # fileimage=ImageTkPhotoImage(image)
        os.chdir("C:\\Users\\Admin\\Downloads")
        image.save(f"{str(file1[6])[0:len(file1[6]) - 4]}.{text}")
        print("image converted")
        pg.alert("image converted".upper())
        l2.destroy()
        #l3.destroy()
        var.set("")
        e1.update()
    except Exception as e:
        print(e)
        pg.alert("IMAGE NOT CONVERTABLE IN YOUR GIVEN EXTENSION")
        l2.destroy()
        l3.destroy()
        var.set("")
        e1.update()
b1=Button(text="SELECT FILE",borderwidth=10,bg="grey",relief=SUNKEN,font="comicsansms 15 bold",command=convert)
b1.place(x=10,y=10)
b2=Button(text="CONVERT",borderwidth=10,bg="grey",relief=SUNKEN,font="comicsansms 15 bold",command=convert1)
b2.place(x=600,y=10)
l1=Label(text="WRITE EXTENSION INTO CONVERT IMAGE",borderwidth=10,bg="grey",relief=SUNKEN,font="comicsansms 15 bold",)
l1.place(x=10,y=100)
var=StringVar()
e1=Entry(textvariable=var,borderwidth=10,relief=SUNKEN,font="comicsansms 15 bold")
e1.place(x=480,y=100)
root.mainloop()
