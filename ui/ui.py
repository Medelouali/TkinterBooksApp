from tkinter import *
from ui.layout.layout import layout
from ui.register.register import register
from ui.logic.widget import widget

def ui():
    root = Tk()
    root.title("Book Your Book")
    root.geometry("850x450")
    frame=LabelFrame(root, padx=40, pady=20)
    frame.pack()
    register(frame, [ widget(frame, True) ])
    #layout(root, reg)
    root.mainloop()