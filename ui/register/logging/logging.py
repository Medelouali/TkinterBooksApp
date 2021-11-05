#from ui.register.register import removeLast
from ui.layout.layout import layout 
from ui.logic.widget import deleteWidgets

def logging(root, history=[], username="", password=""):
    deleteWidgets(history)    
    layout(root)
