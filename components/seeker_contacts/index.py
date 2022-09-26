from tkinter import *
from tkinter import ttk
from . import bton_contacts
from . import label_entry_query
from . import bton_query

def seeker(root:Tk, treeview:ttk.Treeview):

    seeker_c = LabelFrame(root)
    seeker_c.place(y=170, width= 500, height=40)

    bton_contacts.bton_contacts(seeker_c, treeview)
    entry_query = label_entry_query.label_and_entry_query(seeker_c)[1]
    bton_query.bton_query(seeker_c, entry_query, treeview)

    return seeker_c