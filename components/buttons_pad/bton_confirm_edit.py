from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import *
import util.view
import config.model_controller

def bton_confirm_edit(
    root:Tk, 
    name:Entry, 
    lastname:Entry, 
    phone:Entry, 
    email:Entry, 
    treeview:Treeview):
    
    def click_bton():
        
        if treeview.focus():

            contacts = config.model_controller.get_all_contacts()
            item = treeview.focus()
            id = treeview.item(item)["values"][0]
            
            if config.model_controller.edit_contact(
                name.get(), 
                lastname.get(), 
                phone.get(), 
                email.get(), 
                id):

                if askyesno(
                    "Editar Contacto: ", 
                    "Desea confirmar lo siguiente ? " + 
                    "\n" + name.get() + 
                    "\n" + lastname.get() + 
                    "\n" + phone.get()+
                    "\n" + email.get()):

                    showinfo("Si", "Contacto editado")
                    contacts.clear()
                    contacts = config.model_controller.get_all_contacts()
                    util.view.refresh_insert_treeview(treeview, contacts)
                    util.view.refresh_entrys(name, lastname, phone, email)
        
                else:

                    showinfo("Editar Contacto", "El contacto no se editó")
                    util.view.refresh_entrys(name, lastname, phone, email)

            else:
                showerror("Error", "Datos ingresados invalidos")
                util.view.refresh_entrys(name, lastname, phone, email)     

    bton = Button(
        root, 
        text="Confirmar Edición", 
        bg="darkgreen", 
        fg="white", 
        activebackground="darkgreen", 
        activeforeground="white", 
        command= click_bton
    )
    
    bton.place(x=115, y= 0)

    return bton