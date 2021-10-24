from tkinter import *

def browser(root, page="editors"):
    if(page=="books"):
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)
    elif(page=="authors"):
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)
    elif(page=="copies"):
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)
    else:
        label=Label(root, text=f"This is the {page} page")
        label.grid(row=1, column=0)