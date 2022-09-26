from tkinter import *
import components.form.index as index_f
import components.buttons_pad.index as index_k
import components.seeker_contacts.index as index_s
import components.treeview.index as index_t
import components.quit.bton_quit as bton_quit
import config.model_controller

app = Tk()

app.title("Agenda Telefónica")
app.geometry("500x500")
app.config(bg="azure2")

contacts = config.model_controller.get_all_contacts()

form, entry_name, entry_lastname, entry_phone, entry_email  = index_f.form_contact(app)

treeview = index_t.view_contacts(app)[1]

index_k.keypad(
    app, 
    treeview, 
    entry_name, 
    entry_lastname, 
    entry_phone, 
    entry_email
)

index_s.seeker(app, treeview)

for i in range(len(contacts)):
    
    treeview.insert(
        "", 
        "end", 
        values=(
            contacts[i][0],
            contacts[i][1],
            contacts[i][2], 
            contacts[i][3], 
            contacts[i][4]
        )
    )

bton_quit.bton_quit(app)

app.mainloop()