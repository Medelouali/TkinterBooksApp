from tkinter import *

#just for testing purposes...

testList=[
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling'},
    ]

def books(root):
    widgets=[]
    for i, boo in enumerate(testList):
        widgets+=book(root, index=i+1, title=boo['title'], date=boo['date'], writtenBy=boo['writtenBy'], 
        description=boo['description'])
    return widgets

def book(root, index=2, title='', date='', description='', writtenBy=''):
    style={
        'padx': 20, 
        'pady': 1
    }
    frame=LabelFrame(root, padx=style['padx'],pady=style['pady'])
    frame.grid(row=index, column=0, columnspan=4)

    tit=Label(frame, text=title)
    tit.grid(row=0, column=0)

    dat=Label(frame, text=date)
    dat.grid(row=0, column=1)

    wri=Label(frame, text=writtenBy)
    wri.grid(row=1, column=0)

    des=Label(frame, text=description)
    des.grid(row=2, column=0, columnspan=2)
    
    return [tit, dat, wri, des, frame]

