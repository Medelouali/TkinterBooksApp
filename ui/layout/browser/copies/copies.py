from tkinter import *


#just for testing purposes...

testList=[
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling', 'editionYear': '2007', 'editionHouse': 'RabatBooks'},
    { 'title': "Harry Poter", 'date': "12/22/2007", 'description': "Lovely book u ll ever read", 'writtenBy': 'J.K.Rowling', 'editionYear': '2007', 'editionHouse': 'RabatBooks'},
    ]

def copies(root):
    widgets=[]
    for i, boo in enumerate(testList):
        widgets+=copy(root, index=i+1, title=boo['title'], date=boo['date'], writtenBy=boo['writtenBy'], 
        description=boo['description'], editionHouse=boo['editionHouse'], editionYear=boo['editionYear'])
    return widgets



def copy(root, index=2, title='', date='', description='', writtenBy='', editionYear='', editionHouse=''):
    style={
        'padx': 20, 
        'pady': 1,
        'width': 90
    }
    frame=LabelFrame(root, padx=style['padx'],pady=style['pady'], width=style['width'])
    frame.grid(row=index, column=0, columnspan=4)

    tit=Label(frame, text=f'Copy Title: {title}')
    tit.grid(row=0, column=0)

    dat=Label(frame, text=f'Copy Date: {date}')
    dat.grid(row=0, column=1)

    wri=Label(frame, text=f'Copy Original Writer: {writtenBy}')
    wri.grid(row=1, column=0)

    des=Label(frame, text=f'Copy Description: {description}')
    des.grid(row=2, column=0, columnspan=2)
    
    edY=Label(frame, text=f'Copy Ed Year: {editionYear}')
    edY.grid(row=3, column=1)

    edH=Label(frame, text=f'Copy Ed House: {editionHouse}')
    edH.grid(row=4, column=0, columnspan=2)

    return [tit, dat, wri, des, edH, edY, frame]
