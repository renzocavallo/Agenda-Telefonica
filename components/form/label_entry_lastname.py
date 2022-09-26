from tkinter import *

def label_and_entry_lastname(root:Tk):
    
    lastname = Label(root, text="Apellido :")
    lastname.place(x=50, y=60)
    entry_lastname = Entry(root)
    entry_lastname.place(x=110, y=60)
    
    return lastname, entry_lastname