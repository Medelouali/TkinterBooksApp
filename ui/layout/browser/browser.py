from tkinter import *
from ui.layout.browser.books.books import books
from ui.layout.browser.authors.authors import authors
from ui.layout.browser.copies.copies import copies
from ui.layout.browser.editors.editors import editors

def browser(root, page="editors"):
    if(page=="books"):
        return books(root)        
    if(page=="authors"):
        return authors(root)
    if(page=="copies"):
        return copies(root)
    return editors(root)