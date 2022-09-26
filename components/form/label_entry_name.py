from tkinter import *

def label_and_entry_name(root:Tk):
    
    name = Label(root, text="Nombre :")
    name.place(x=50, y=30)
    entry_name = Entry(root)
    entry_name.place(x=110, y=30)
    
    return name, entry_name