from tkinter import *

def browser(root, page="visitors"):
    if(page=="readers"):
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)
    elif(page=="authors"):
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)
    else:
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)