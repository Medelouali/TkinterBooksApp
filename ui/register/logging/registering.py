from ui.layout.layout import layout
from ui.logic.widget import deleteWidgets
from ui.database.query import query
from ui.logic.secure.hashing import hash_password
import ui.register.register as reg

def registering(root, history=[], username="", email="", password=""):
    res=query(f'SELECT * FROM users WHERE email="{email}"', doesReturn=True)
    if(res):
        return reg.register(root, last=history, err="This email is already taken!!", page='signUp')
    query(f"INSERT INTO users values('{username}', '{email}', '{hash_password(password)}')")
    deleteWidgets(history)
    layout(root, user=query(f'SELECT * FROM users WHERE email="{email}"', doesReturn=True)[0])