from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Sign up page")

Name=StringVar()
Email=StringVar()
Phone= IntVar()
c=StringVar()
var1=StringVar()
var2=StringVar()


def database():
    name1=Name.get()
    email=Email.get()
    phone=Phone.get()
    country=c.get()
    passwd=var1.get()
    cpasswd=var2.get()
    conn = sqlite3.connect('Signup.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Email TEXT,Phone TEXT,Country TEXT,Programming TEXT)')
    cursor.execute('INSERT INTO Student (Name,Email,Phone,Country,Passwd,cpasswd) VALUE(?,?,?,?,?,?)',(name1,email,phone,country,passwd,cpasswd))
    conn.commit()


    
label_0 = Label(root, text="Sign up page",width=20,font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvar=Name)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Phone no",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
Phone=IntVar()

entry_3 = Entry(root, textvar=Phone)
entry_3.place(x=240,y=230)


label_4 = Label(root, text="Country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1  = ['Canada','India','USA','UK','Nepal','Russia'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select your country')
droplist.place(x=235,y=280)

var1 = StringVar() 

label_5 = Label(root, text="Confirm Password",width=20,font=("bold", 10))
label_5.place(x=80,y=370)

entry_5 = Entry(root, textvar=var1,show='*')
entry_5.place(x=240,y=370)

var2 = StringVar()

label_6 = Label(root, text="Password",width=20,font=("bold", 10))
label_6.place(x=70,y=330)

entry_6 = Entry(root, textvar=var2,show='*')
entry_6.place(x=240,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=420)

root.mainloop()
