from pydoc import TextRepr
from tkinter import *
from . import treeview

def view_contacts(root:Tk):

    view_c = LabelFrame(root, text="AGENDA :")
    view_c.place(y= 210, width=500, height=250)

    tree = treeview.treeview(view_c)

    return view_c, tree