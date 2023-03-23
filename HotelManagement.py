import re
from sqlite3 import Cursor
from tkinter import *
import tkinter.font as tkFont
import sqlite3
import random
import datetime as dt
import time as t
from matplotlib import pyplot as plt
from PIL import Image, ImageTk

##------------------SQL DATABASE ------------##

con = sqlite3.connect("Hotel.db")
cur: Cursor = con.cursor()

### To store the data ALL TIME
cur.execute('CREATE TABLE  IF NOT EXISTS HOTEL1(CustomerId INTEGER,TableNum INTEGER,Amount_Table INTEGER)')

window = Tk()
window.title("Hotel Management")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

##------------------------- FRAMES -----------------##

frame1 = Frame(window, width=500, height=450, bg='light blue')
frame1.place(relwidth=.5)

label_hotel_name = Label(frame1, text="Hotel Mini Punjab", bg='#c2fc03', width=30, height=2,
                         font=('Retro', 22, 'italic'), justify='center')
label_hotel_name.place(rely=0, relx=0.1)

frame2 = Frame(window, width=500, height=450, bg='pink')
frame2.place(rely=.5, relwidth=.5)

frame3 = Frame(window, width=1000, height=1000, bg='green')
frame3.place(relx=.5)


# --------------------------Functions-----------------#

def New_Change():
    text_table.set(random.randint(1, 5))
    textran.set(random.randint(100, 1000008))
    text_order.set("")
    cur.execute('INSERT INTO HOTEL1 VALUES(?,?,?)', (textran.get(), text_table.get(), total_amount_table.get()))
    total_amount_table.set(0)
    label_entering_total_value.config(text="0")


def set_Table():
    print(text_table.set(text_table.get()))


def label_set(dish):
    text_order.set(text_order.get() + "\n" + dish)


def Analysis_acc_to_Table_Amount():
    cur.execute("SELECT TableNum FROM HOTEL1 ")
    table_number = list(cur.fetchall())
    print(table_number)
    cur.execute("SELECT Amount_Table FROM HOTEL1")
    amount = list(cur.fetchall())
    print(amount)
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
    plt.title("Scatterd Graph for Hotel", fontdict=font1, loc='center')
    plt.xlabel("Amount Paid for that Table", fontdict=font2, loc='center')
    plt.ylabel("Table Numbers", fontdict=font2, loc='center')

    ##Subplots = Number of the rows in the graph plot(if we need to create  different  number plots)
    ## plt.subplot(rows,columns,)

    plt.scatter(amount, table_number, c='purple', marker='o')
    plt.show()


def total_Bill():
    order = text_order.get()
    regex = '\d+'
    global match
    match = re.findall(regex, order)
    print(match)
    sum = 0
    for i in range(0, len(match)):
        sum += int(match[i])
    print(sum)
    label_entering_total_value.config(text=sum)
    total_amount_table.set(sum)


def Customer_Id():
    print(textran.set(textran.get()))


def ctime():
    time_str = t.strftime('%H:%M:%S %p')
    label_time_current.config(text=time_str)
    label_time_current.after(1000, ctime)


## Adding time to the frame---------------------------------

date = dt.datetime.now()
label_time = Label(frame3, text=f"{date:%A,%B,%d,%Y}", font=('Retro', 22, 'bold'))
label_time.place(rely=0.15)
label_time_current = Label(frame3, font=('Retro', 22, 'bold'))
label_time_current.place(rely=0.15, relx=0.45)

##------------ DropDown For Menu ---------------##

menu = StringVar()
menu.set("Select Any Dish")
text_order = StringVar()
helv36 = tkFont.Font(family='Helvetica', size=28)

drop = OptionMenu(window, menu, "Panner Tikka         Rs.235", "Paneer Masala          Rs.180",
                  "Veg.Kolhapuri            Rs.245",
                  "Malai Kofta         Rs.175", "Lassi          Rs.105", "Dhanshaak            Rs.335",
                  "Makai Roti         Rs.20", "Roti            Rs.15", command=label_set)
drop.place(relx=0.1, rely=.170)

drop.config(font=helv36)

label_Menu_display = Label(frame1, text='Menu', font=('Retro', 28, 'bold'), bg='orange', fg='black')
label_Menu_display.place(rely=0.3)

##---------------------TEXTBOX -------------------##


label_text_BOX = Label(frame3, textvariable=text_order, bd=2, width=90, height=27, relief=RIDGE, anchor='nw',
                       font=('Courier', 8, 'bold'))
label_text_BOX.place(rely=0.2, relx=0.075)

##------------ DropDown For Payment Mode---------------##

paymode = StringVar()
paymode.set("Select Payment Mode")
drop_Payment_mode = OptionMenu(frame3, paymode, *['Cash', 'UPI', 'Credit//Debit Card', 'Net Banking', 'Digital Wallet'])
drop_Payment_mode.place(rely=0.65, relx=0.55)
drop_Payment_mode.config(font=('Retro', 10, 'bold'))

label_payment_mode = Label(frame3, text="Payment Mode", font=('Retro', 22, 'bold'))
label_payment_mode.place(rely=0.65, relx=0.32)

##--------------------------- DropDown For Table Number -----------------##


text_table = IntVar()
text_table.set(random.randint(1, 5))

label_random_table_num = Label(frame3, textvariable=text_table, font=('Retro', 22, 'bold'), width=15, height=1)
label_random_table_num.place(relx=0.3, rely=0.1)
label_table = Label(frame3, text='Table No.', font=('Retro', 22, 'bold'), bg='orange')
label_table.place(rely=0.1)

##------------- Customer ID ----------------##
textran = IntVar()
textran.set(random.randint(100, 100000))

label_customer_id = Label(frame3, text='Customer Id', font=('Retro', 22, 'bold'), bg='orange', fg='black')
label_customer_id.place(rely=0)

label_entering_customer_id = Label(frame3, textvariable=textran, font=('Retro', 22, 'bold'), width=15, height=1)
label_entering_customer_id.place(relx=0.3)

##----------------TOTAL----------------##

total_amount_table = IntVar()

label_entering_total_value = Label(frame3, font=('Retro', 22, 'bold'), width=8, height=1)
label_entering_total_value.place(rely=0.65, relx=0.16)

##-------------------Buttons------------------##
photo = Image.open('C:\\Users\\jinesh satish\\OneDrive\\Pictures\\btn_img.png')
photo = photo.resize((135, 50), Image.LANCZOS)
img = ImageTk.PhotoImage(photo)

btn_total = Button(frame3, text='Total', font=('Retro 22 bold'), image=img, compound='center', command=total_Bill)
btn_total.place(rely=0.65, relx=0.018)

btn_add = Button(frame3, image=img, text='Add', font=('Retro', 22, 'bold'), compound='center')
btn_add.place(rely=0.72, relx=0.018)

btn_close = Button(frame3, image=img, text='Close', font=('Retro', 22, 'bold'), compound='center',
                   command=window.destroy)
btn_close.place(rely=0.72, relx=0.4)

btn_new = Button(frame2, image=img, text='New', font=('Retro', 22, 'bold'), compound='center', command=New_Change)
btn_new.place(rely=0.2, relx=0.1)

btn_analysis = Button(frame2, image=img, text='Analysis', font=('Retro', 22, 'bold'), compound='center',
                      command=Analysis_acc_to_Table_Amount)
btn_analysis.place(rely=0.4, relx=0.1)

cur.execute('INSERT INTO HOTEL1 VALUES(?,?,?)', (textran.get(), text_table.get(), total_amount_table.get()))
con.commit()
ctime()
window.mainloop()
cur.execute('SELECT * FROM HOTEL1 ')
print(cur.fetchall())
