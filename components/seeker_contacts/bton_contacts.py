from tkinter import *
from tkinter import ttk
import util.view
import config.model_controller

def bton_contacts(root:ttk.LabelFrame, treeview:ttk.Treeview):
    
    def click_bton():
        
        contacts = config.model_controller.get_all_contacts()
        util.view.refresh_insert_treeview(treeview, contacts)
    
    bton = Button(
        root, 
        text="Contactos", 
        bg="purple", 
        fg="white", 
        activebackground="purple", 
        activeforeground="white", 
        command= click_bton
    )

    bton.place(x=20, y=5)
    
    return bton