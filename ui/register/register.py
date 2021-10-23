from tkinter import *
from threading import Event, Thread
from ui.register.logging.logging import logging
from ui.register.logging.registering import registering

def register(fr, last=[], err='', page="log", lastPacked=False):
    errMassage=""
    if(page=="signUp"):
        #
        uiAttr={
            "font": ('Helvetica bold',10),
            "width": 40,
            "pady": 5
        }
        def validate():
            print(nam.get(), ema.get(), pas.get())
        nam=StringVar() 
        ema=StringVar() 
        pas=StringVar()

        username=Label(fr, text="Username", width=50, font=uiAttr["font"])
        username.grid(row=0, column=0)
        usernameE=Entry(fr, width=uiAttr["width"], textvariable=nam)
        usernameE.grid(row=1, column=0, pady=uiAttr["pady"])
        #just for testing
        usernameE.insert(0, "John")

        email=Label(fr, text="Email", font=uiAttr["font"])
        email.grid(row=2, column=0)
        emailE=Entry(fr, width=uiAttr["width"], textvariable=ema)
        emailE.grid(row=3, column=0, pady=uiAttr["pady"])

        password=Label(fr, text="Password", font=uiAttr["font"])
        password.grid(row=4, column=0)
        passwordE=Entry(fr, show="*", width=uiAttr["width"], textvariable=pas)
        passwordE.grid(row=5, column=0, pady=uiAttr["pady"])

        signUp=Button(fr, text="Create Account", 
            command=lambda: registering([signIn , *widgets], nam.get(), ema.get(), pas.get()))
        signUp.grid(row=6, column=0, padx=40, pady=20)
        #
        widgets=[ username, usernameE, email, emailE, password, passwordE, signUp]
        signIn = Button(fr, text="Already Have Account?", command=lambda : commander(fr, [*widgets, signIn], err, 'signIn'))
        signIn.grid(row=7, column=0, padx=40, pady=20)

    elif(page=="signIn"):
        #
        uiAttr={
            "font": ('Helvetica bold',10),
            "width": 40,
            "pady": 5
        }
        def validator(hist, name, password):
            errMassage="Something went wrong"
            return
            #logging(hist, name, password)
        nam=StringVar() 
        ema=StringVar() 
        pas=StringVar()

        username=Label(fr, text="Username", width=50, font=uiAttr["font"])
        username.grid(row=0, column=0)
        usernameE=Entry(fr, width=uiAttr["width"], textvariable=nam)
        usernameE.grid(row=1, column=0, pady=uiAttr["pady"])

        password=Label(fr, text="Password", font=uiAttr["font"])
        password.grid(row=2, column=0)
        passwordE=Entry(fr, show="*", width=uiAttr["width"], textvariable=pas)
        passwordE.grid(row=3, column=0, pady=uiAttr["pady"])
        #logging prototype logging(historyWidgets, name, password)
        logIn=Button(fr, text="Log In", 
            command=lambda: validator([ signUp, *widgets], nam.get(), pas.get()))
        logIn.grid(row=4, column=0, padx=40, pady=20)
        #
        widgets=[ username, usernameE, password, passwordE, logIn]
        signUp = Button(fr, text="Don't Have An Account?", 
                        command=lambda : commander(fr, [signUp, *widgets ], err, 'signUp'))
        signUp.grid(row=5, column=0, padx=40, pady=20)
    else:
        signIn=Button(fr, text="Sign In", command=lambda: commander(fr, [signIn, signUp], err, 'signIn'))
        signIn.grid(row=0, column=0, padx=40, pady=20)
        signUp=Button(fr, text="Sign Up", command=lambda: commander(fr, [signUp, signIn], err, 'signUp'))
        signUp.grid(row=1, column=0, padx=40, pady=20)
    if(errMassage):
        lab=Label(fr, text=errMassage).grid(row=20, column=0, columnspan=W+E)

def commander(fr, last, err='', page="log", lastPacked=False):
    removeLast(last, lastPacked)
    register(fr, last, err, page, lastPacked)

#Clearing out the frame
def removeLast(last, lastPacked=False):
    for widget in last:
        if(lastPacked):
            widget.pack_forget()
        else:
            widget.grid_forget()
