from tkinter import *
from tkinter import ttk

def treeview(root:Tk):
    
    style = ttk.Style()
    style.theme_use("clam")
    
    treeview = ttk.Treeview(root)
    treeview["columns"] = ("col1", "col2", "col3", "col4", "col5")
    treeview.column("#0", width=0, minwidth=0)
    treeview.column("col1", width=60, minwidth=60)
    treeview.heading("col1", text="Id")
    treeview.column("col2", width=60, minwidth=60)
    treeview.heading("col2", text="Nombre")
    treeview.column("col3", width=80, minwidth=60)
    treeview.heading("col3", text="Apellido")
    treeview.column("col4", width=130, minwidth=80)
    treeview.heading("col4", text="Telefono")
    treeview.column("col5",width=130, minwidth=80)
    treeview.heading("col5", text="Email")
    treeview.place(x= 20, y=0)
    
    return treeview