from tkinter import *


#just for testing purposes...

test=[
    { 'birthday': "12/22/2007", 'quote': "Life Is Worth Living", 'name': 'J.K.Rowling', 'place': 'New York', 'branch': 'Science Fiction', 'stars': 5},
    { 'birthday': "12/22/2007", 'quote': "Life Is Worth Living", 'name': 'J.K.Rowling', 'place': 'New York', 'branch': 'Science Fiction', 'stars': 5},
    ]

def authors(root):
    widgets=[]
    for i, boo in enumerate(test):
        widgets+=author(root, index=i+1, name=boo['name'], birthday=boo['birthday'], place=boo['place'], 
            branch=boo['branch'], stars=boo['stars'], quote=boo['quote'])
    return widgets

def author(root, index=2, name='', birthday='', place='', branch='', stars=0, quote=''):
    style={
        'padx': 20, 
        'pady': 1,
        'width': 90
    }
    frame=LabelFrame(root, padx=style['padx'],pady=style['pady'], width=style['width'])
    frame.grid(row=index, column=0, columnspan=4)

    nam=Label(frame, text=f'Author: {name}')
    nam.grid(row=0, column=0)

    pla=Label(frame, text=f'City/Country: {place}')
    pla.grid(row=0, column=1)

    bra=Label(frame, text=f'Branch: {branch}')
    bra.grid(row=1, column=0)

    sta=Label(frame, text=f'Stars: {stars}')
    sta.grid(row=2, column=0, columnspan=2)
    
    quo=Label(frame, text=f'Favorate Quote: {quote}')
    quo.grid(row=3, column=0, columnspan=2)

    bir=Label(frame, text=f'Birthday: {birthday}')
    bir.grid(row=4, column=0, columnspan=2)

    return [nam, pla, bra, sta, quo, bir, frame]
