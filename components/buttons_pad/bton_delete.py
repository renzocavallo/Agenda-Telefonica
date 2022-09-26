from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import *
import config.model_controller

def bton_delete(root:Tk, treeview:Treeview):
    
    def click_bton():
        
        if treeview.focus():
            
            contacts = config.model_controller.get_all_contacts()
            item = treeview.focus()
        
            if askyesno(
                "Eliminar Contacto: ", 
                "Desea eliminar: " + treeview.item(item)["values"][1] + 
                " " + treeview.item(item)["values"][2] +"?"):

                showinfo("Si", "Contacto eliminado")

                config.model_controller.delete_contact(treeview.item(item)["values"][0])
                count = 0
            
                for i in range(len(contacts)):
                
                    if contacts[i][0] != treeview.item(item)["values"][0]:
                        count += 1

                    else:
                        
                        break
        
                contacts.pop(count)
                treeview.delete(item)
    
    bton = Button(
        root, 
        text="Eliminar", 
        bg="red", 
        fg="white", 
        activebackground="red", 
        activeforeground="white", 
        command= click_bton
    )

    bton.place(x=0, y=35)

    return bton