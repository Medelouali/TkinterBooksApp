from tkinter import *
import tkinter.font as tkFont
from ui.layout.browser.browser import browser
from ui.logic.widget import deleteWidgets, widgets

lastWidgets=[]
currentPage="books"

def layout(rt, user=(), history=[]):
    deleteWidgets(history)
    fontStyle = tkFont.Font(family = "Lucida Grande", size = 15)
    smallFont = tkFont.Font(family = "Lucida Grande", size = 10)

    global currentPage
    global lastWidgets
    labels={
        "width": 20,
        "height": 1
    }

    def switchPage(page, collect=[]):
        global currentPage
        global lastWidgets
        deleteWidgets(collect)
        currentPage=page
        lastWidgets=browser(frame, page)

    frame=LabelFrame(rt, text=f"Hello {user[0]}", pady=1, font=fontStyle)
    frame.grid(row=0, column=0, columnspan=3)

    books=Button(frame, text="Books", command=lambda: switchPage("books", lastWidgets), font=smallFont,
        width=labels["width"], height=labels["height"])
    books.grid(row=0, column=0, padx= 5)

    authors=Button(frame, text="Authors", command=lambda: switchPage("authors", lastWidgets), 
        font=smallFont, width=labels["width"], height=labels["height"])
    authors.grid(row=0, column=1, padx= 5)

    copies=Button(frame, text="Copies", command=lambda: switchPage("copies", lastWidgets), font=smallFont,
        width=labels["width"], height=labels["height"])
    copies.grid(row=0, column=2, padx= 5)

    editors=Button(frame, text="Editors", command=lambda: switchPage("editors", lastWidgets), 
        font=smallFont, width=labels["width"], height=labels["height"])
    editors.grid(row=0, column=3, padx= 5)

    childFrame=LabelFrame(frame, pady=1, font=fontStyle)
    childFrame.grid(row=1, column=0, columnspan=3)

    #the correspondant page should be displayed, this for setting the default page
    lastWidgets=browser(childFrame, currentPage)

    widgets_t=[frame, childFrame,books, authors, copies, editors]
    getInTouch=Button(frame, text="Get In Touch", width=labels["width"]*2, height=1, font=smallFont,
        command=lambda: contactUs(rt, user, hist=widgets([*widgets_t, getInTouch]) + [ *lastWidgets ]))
    getInTouch.grid(row=100, column=0, columnspan=4)


def contactUs(rt, user_t, hist=[]):
    deleteWidgets(hist)
    fontStyle = tkFont.Font(family = "Lucida Grande", size = 15)
    smallFont = tkFont.Font(family = "Lucida Grande", size = 10)
    justFont = tkFont.Font(family = "Lucida Grande")

    frame=LabelFrame(rt, text="Contacting Us Via Email", font=fontStyle, pady=1)
    frame.grid(row=0, column=0, columnspan=3) 

    fr=LabelFrame(frame, pady=1)
    fr.grid(row=1, column=0, columnspan=3) 

    notice=Label(fr, text=f"Please {user_t[0]} be specific and precise in your messages to get the proper response", padx=10)
    notice.grid(row=0, column=0)

    messageLabel=Label(frame, text="Message", font=smallFont)
    messageLabel.grid(row=3, column=0)

    ent=Entry(frame, width=70, font=justFont)
    ent.grid(row=4, column=0, pady=4)
    #

    send=Button(frame, text="Send", padx=3, width=10, font=smallFont)
    send.grid(row=5, column=0)
    widgets_t=[frame, notice, fr, messageLabel, ent, send]
    goBack=Button(fr, text="Go Home", command=lambda: layout(rt, user_t, history=widgets([*widgets_t, goBack])),
        font=smallFont)
    goBack.grid(row=0, column=1)