from tkinter import *
from ui.layout.browser.scroller import scroller
from ui.logic.widget import widgets
#just for testing purposes...

testList=[
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    ]

def books(root):
    widgets=scroller(root)
    for i, boo in enumerate(testList):
        widgets+=book(widgets[0]['widget'], index=i+1, title=boo['title'], date=boo['date'], writtenBy=boo['writtenBy'], 
        description=boo['description'])
    return widgets

def book(root, index=2, title='', date='', description='', writtenBy=''):
    style={
        'padx': 20, 
        'pady': 1,
        'width': 70
    }
    frame=LabelFrame(root, padx=style['padx'],pady=style['pady'])
    frame.grid(row=index, column=0, columnspan=4)

    tit=Label(frame, text=title, width=style['width'])
    tit.grid(row=0, column=0)

    dat=Label(frame, text=date)
    dat.grid(row=0, column=1)

    wri=Label(frame, text=writtenBy)
    wri.grid(row=1, column=0)

    des=Label(frame, text=description)
    des.grid(row=2, column=0, columnspan=2)
    
    return widgets([tit, dat, wri, des, frame])

