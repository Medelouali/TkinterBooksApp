from tkinter import *
from ui.layout.browser.browser import browser

def layout(rt, reg={}):
    currentPage="visitors"
    labels={
        "width": 20,
        "height": 2
    }
    def switchPage(page):
        currentPage=page
        browser(frame, currentPage)
    
    frame=LabelFrame(rt, text="You Are A Reader", pady=1)
    frame.grid(row=0, column=0, columnspan=3)

    reader=Button(frame, text="Readers", command=lambda: switchPage("readers"), 
        width=labels["width"], height=labels["height"])
    reader.grid(row=0, column=0, padx= 5)

    authors=Button(frame, text="Authors", command=lambda: switchPage("authors"), 
        width=labels["width"], height=labels["height"])
    authors.grid(row=0, column=1, padx= 5)

    visitors=Button(frame, text="Visitors", command=lambda: switchPage("visitors"), 
        width=labels["width"], height=labels["height"])
    visitors.grid(row=0, column=2, padx= 5)

    #the correspondant page should be displayed, this for setting the default page
    browser(frame, currentPage)

    getInTouch=Button(frame, text="Get In Touch", width=labels["width"]*2, height=1)
    getInTouch.grid(row=2, column=0, columnspan=3)
