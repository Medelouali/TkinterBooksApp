from tkinter import *
from ui.layout.layout import layout
from ui.register.register import register

def ui():
    root = Tk()
    root.title("Book Your Book")
    root.geometry("650x350")
    frame=LabelFrame(root, padx=40, pady=20)
    frame.pack()
    reg=register(frame, [ frame ], lastPacked=True)
    layout(root, reg)
    root.mainloop()