from ui.layout.layout import layout
from ui.logic.widget import deleteWidgets


def registering(root, history=[], username="", email="", password=""):
    deleteWidgets(history)
    layout(root)