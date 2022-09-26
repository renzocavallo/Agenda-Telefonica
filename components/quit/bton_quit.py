from tkinter import *

def bton_quit(root:Tk):
    
    bton = Button(
        root, 
        text="Salir",
        bg="black", 
        fg="white", 
        activebackground="azure2", 
        activeforeground="black",  
        command= root.quit
    )

    bton.place(x=240, y=465)
    
    return bton