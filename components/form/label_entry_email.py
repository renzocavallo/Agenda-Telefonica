from email.policy import default
from tkinter import *

def label_and_entry_email(root:Tk):
    
    email = Label(root, text="Email :")
    email.place(x=50, y=120)
    entry_email = Entry(root)
    entry_email.place(x=110, y=120)
    
    return email, entry_email