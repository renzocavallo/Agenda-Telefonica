from tkinter import *
from tkinter import ttk
from . import bton_save
from . import bton_delete
from . import bton_edit
from . import bton_confirm_edit

def keypad(
    root:Tk,
    treeview:ttk.Treeview, 
    name:Entry, 
    lastname:Entry, 
    phone:Entry, 
    email:Entry
    ):

    buttons = ttk.LabelFrame(root)
    buttons.place(x=250, width=250, height=180)

    b_save = bton_save.bton_save(
        buttons, 
        name, 
        lastname, 
        phone, 
        email,
        treeview
    
    )
    b_delete = bton_delete.bton_delete(buttons, treeview)

    b_edit = bton_edit.bton_edit(
        buttons, 
        name, 
        lastname, 
        phone, 
        email, 
        treeview
    )

    b_confirm_edit = bton_confirm_edit.bton_confirm_edit(
        buttons,
        name, 
        lastname, 
        phone, 
        email, 
        treeview
    )

    return(
        buttons,
        b_save,
        b_delete,
        b_edit,
        b_confirm_edit
    )