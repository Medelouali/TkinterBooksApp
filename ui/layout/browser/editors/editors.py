from tkinter import *
#just for testing purposes...

testList=[
    {'manager': 'El Ouali Med', 'location': "Marrakesh City", 'stars': 3, 'phone': '+212690238923', 'gmail': 'readWithUsCamus@gmail.com', 'websiteUrl': 'wwww.camusbooks.com'},
    {'manager': 'El Ouali Med', 'location': "Marrakesh City", 'stars': 3, 'phone': '+212690238923', 'gmail': 'readWithUsCamus@gmail.com', 'websiteUrl': 'wwww.camusbooks.com'},
    ]

def editors(root):
    widgets=[]
    for i, boo in enumerate(testList):
        widgets+=editor(root, index=i+1, manager=boo['manager'], location=boo['location'], stars=boo['stars'],
        phone=boo['phone'], gmail=boo['gmail'], websiteUrl=boo['websiteUrl'])
    return widgets



def editor(root, index=2, manager='', location='', stars=0, phone='', gmail='', websiteUrl=''):
    style={
        'padx': 20, 
        'pady': 1,
        'width': 90
    }
    frame=LabelFrame(root, padx=style['padx'],pady=style['pady'], width=style['width'])
    frame.grid(row=index, column=0, columnspan=4)

    man=Label(frame, text=f'Manager: {manager}')
    man.grid(row=0, column=0)

    loc=Label(frame, text=f'Country/City: {location}')
    loc.grid(row=0, column=1)

    pho=Label(frame, text=f'Phone: {phone}')
    pho.grid(row=1, column=0)

    gma=Label(frame, text=f'Gmail: {gmail}')
    gma.grid(row=2, column=0, columnspan=2)
    
    web=Label(frame, text=f'Visit Us On: {websiteUrl}')
    web.grid(row=3, column=1)

    sta=Label(frame, text=f'Stars: {stars}')
    sta.grid(row=4, column=0, columnspan=2)

    return [man, loc, pho, gma, web, sta, frame]
