from tkinter import *

def label_and_entry_phone(root:Tk):
    
    phone = Label(root, text="Telefono :")
    phone.place(x=50, y=90)
    entry_phone = Entry(root)
    entry_phone.place(x=110, y=90)
    
    return phone, entry_phone