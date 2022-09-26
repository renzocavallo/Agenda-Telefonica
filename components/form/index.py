from tkinter import *
from tkinter import ttk
from . import label_entry_name
from . import label_entry_lastname
from . import label_entry_phone
from . import label_entry_email

def form_contact(root:Tk):

    form = ttk.LabelFrame(root, text="DATOS DE CONTACTO :")
    form.place(width=250, height=180)
    
    entry_name = label_entry_name.label_and_entry_name(form)[1]
    entry_lastname = label_entry_lastname.label_and_entry_lastname(form)[1]
    entry_phone = label_entry_phone.label_and_entry_phone(form)[1]
    entry_email = label_entry_email.label_and_entry_email(form)[1]

    return(
        form,
        entry_name,
        entry_lastname,
        entry_phone,
        entry_email
    )
    