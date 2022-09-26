from tkinter import *
from tkinter.ttk import Treeview
import util.view

def bton_edit(
    root:Tk, 
    name:Entry, 
    lastname:Entry, 
    phone:Entry, 
    email:Entry, 
    treeview:Treeview):
    
    def click_bton():

        if treeview.focus():
            
            item = treeview.focus()
            util.view.insert_entrys_item(
                name, 
                lastname, 
                phone, 
                email, 
                treeview, 
                item
            )      
    
    bton = Button(
        root, 
        text="Editar", 
        bg="blue", 
        fg="white", 
        activebackground="blue", 
        activeforeground="white",
        command= click_bton
    )

    bton.place(x= 0, y=70)
    
    return bton