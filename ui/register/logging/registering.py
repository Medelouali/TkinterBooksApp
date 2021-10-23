from ui.layout.layout import layout


def registering(root, history=[], username="", email="", password=""):
    for widget in history:
        widget.grid_forget()
    layout(root)