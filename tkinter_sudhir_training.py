# Project done by : Sudhir Lalloo ( May 2020)
from tkinter import *

window = Tk()
window.config(bg = 'lightblue')
window.title("Hello Python Friends")

label1 = Label(window,text = "Greetings Python Members",bg= 'green',fg = 'white')
window.geometry('500x500')

def do():
    name = name_entry.get()
    contact = contact_entry.get()
    address = address_entry.get()

    window2 = Tk()

    sdl1 = Label(window2,text = "Name:"+name)
    sdl1.pack()
    sdl2 = Label(window2,text = "Contact No:"+contact)
    sdl2.pack()
    sdl3 = Label(window2,text = "Address:"+address)
    sdl3.pack()
    window.destroy()
    window2.mainloop()


label1.pack()

label2 = Label(window,text = "WELCOME TO PYTHON CLUB",bg='brown',fg="yellow",font=('arial',20,'bold'))
label2.pack()

name_label = Label(window,text = "Name")
name_label.pack(anchor='w')

name_entry = Entry(window)
name_entry.pack(anchor='w')

contact_label = Label(window,text = "Contact")
contact_label.pack(anchor='w')

contact_entry = Entry(window)
contact_entry.pack(anchor='w')

address_label = Label(window,text = "Address")
address_label.pack(anchor='w')

address_entry = Entry(window)
address_entry.pack(anchor='w')

Button1 = Button(window,text = "fetch this info",command = do)
Button1.pack()

window.mainloop()


