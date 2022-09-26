from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import *
import util.view
import config.model_controller 

def bton_save(
    root:Tk,
    name:Entry, 
    lastname:Entry, 
    phone:Entry, 
    email:Entry, 
    treeview:Treeview):
    
    def click_bton():
        
        if config.model_controller.create_contact(
            name.get(), 
            lastname.get(), 
            phone.get(), 
            email.get()):
            
            contacts = config.model_controller.get_all_contacts()
            util.view.insert_treeview(treeview, contacts)
            showinfo(
                "Contacto Creado",
                "Se agregó : " + contacts[len(contacts)-1][1] + 
                " " + contacts[len(contacts)-1][2])
            util.view.refresh_entrys(name, lastname, phone, email)
        
        else: 
            
            showerror("Error", "Datos ingresados invalidos") 

    bton = Button(
        root, 
        text="Guardar Contacto",
        bg="green", 
        fg="white", 
        activebackground="green", 
        activeforeground="white", 
        command= click_bton
    )

    bton.place(x=0, y=0)

    return bton