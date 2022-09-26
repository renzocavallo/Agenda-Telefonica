from tkinter import *

def label_and_entry_query(root:Tk):
    
    query = Label(root, text="Nombre de Conctacto:")
    query.place(x=130, y=10)
    entry_query = Entry(root)
    entry_query.place(x=260, y=10)
    
    return query, entry_query