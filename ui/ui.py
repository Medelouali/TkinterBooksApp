from tkinter import *
import ui.register.register as reg

def ui():
    root = Tk()
    root.title("Book Your Book")
    root.geometry("850x450")
    frame=LabelFrame(root, padx=40, pady=20)
    frame.pack()
    reg.register(frame)
    root.mainloop()