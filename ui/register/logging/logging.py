from ui.logic.secure.hashing import verify_password
from ui.database.query import query
from ui.logic.widget import deleteWidgets
from ui.layout.layout import layout
import ui.register.register as reg

def logging(root, history=[], email="", password=""):
    if(not email or not password):
        return reg.register(root, last=history, err="Email or password cannot be empty!!", page='signIn') 
    res=query(f'SELECT * FROM users WHERE email="{email}"', doesReturn=True)
    if(res):
        isValid=verify_password(res[0][2], password)
        if(isValid):
            deleteWidgets(history)    
            return layout(root)
    reg.register(root, last=history, err="Wrong email or password!!", page='signIn')            
