#from ui.register.register import removeLast
from ui.layout.layout import layout 

def logging(root, history=[], username="", password=""):
    for widget in history:
        widget.grid_forget()
    layout(root)
