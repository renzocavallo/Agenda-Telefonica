from tkinter import *
from tkinter import ttk
import util.view
import config.model_controller

def bton_query(root:Tk, name:Entry, treeview:ttk.Treeview):
    
    def click_bton():
        
        contacts_search = config.model_controller.get_contact_by_name(name.get())
        util.view.refresh_insert_treeview(treeview, contacts_search)
        name.delete(0, END)                                        
    
    bton= Button(
        root, 
        text="Buscar", 
        bg="purple", 
        fg="white", 
        activebackground="purple", 
        activeforeground="white", 
        command= click_bton
    )

    bton.place(x=405, y=5)

    return bton