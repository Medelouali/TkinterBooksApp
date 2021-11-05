from tkinter import *
from threading import Event, Thread
from ui.register.logging.logging import logging
from ui.register.logging.registering import registering
from ui.logic.widget import widgets, deleteWidgets
import tkinter.font as tkFont

def register(fr, last=[], err='', page="log"):
    fontStyle = tkFont.Font(family = "Lucida Grande", size = 15)
    smallFont = tkFont.Font(family = "Lucida Grande", size = 10)

    errMassage=""
    if(page=="signUp"):
        #
        uiAttr={
            "font": ('Helvetica bold',10),
            "width": 40,
            "pady": 5
        }
        
        nam=StringVar() 
        ema=StringVar() 
        pas=StringVar()

        username=Label(fr, text="Username", width=50, font=smallFont)
        username.grid(row=0, column=0)
        usernameE=Entry(fr, width=uiAttr["width"], textvariable=nam, font=smallFont)
        usernameE.grid(row=1, column=0, pady=uiAttr["pady"])
        #just for testing
        usernameE.insert(0, "John")

        email=Label(fr, text="Email", font=smallFont)
        email.grid(row=2, column=0)
        emailE=Entry(fr, width=uiAttr["width"], textvariable=ema, font=smallFont)
        emailE.grid(row=3, column=0, pady=uiAttr["pady"])

        password=Label(fr, text="Password", font=smallFont)
        password.grid(row=4, column=0)
        passwordE=Entry(fr, show="*", width=uiAttr["width"], textvariable=pas)
        passwordE.grid(row=5, column=0, pady=uiAttr["pady"])

        #doo some validation later on
        signUp=Button(fr, text="Create Account", font=smallFont,
            command=lambda: registering(fr, widgets([signIn , *widgets_t]), nam.get(), ema.get(), pas.get()))
        signUp.grid(row=6, column=0, padx=40, pady=20)
        #
        widgets_t=[ username, usernameE, email, emailE, password, passwordE, signUp]
        signIn = Button(fr, text="Already Have Account?", font=smallFont,
            command=lambda : commander(fr, widgets([*widgets_t, signIn]), err, 'signIn'))
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

        username=Label(fr, text="Username", width=50, font=smallFont)
        username.grid(row=0, column=0)
        usernameE=Entry(fr, width=uiAttr["width"], textvariable=nam, font=smallFont)
        usernameE.grid(row=1, column=0, pady=uiAttr["pady"])

        password=Label(fr, text="Password", font=smallFont)
        password.grid(row=2, column=0)
        passwordE=Entry(fr, show="*", width=uiAttr["width"], textvariable=pas)
        passwordE.grid(row=3, column=0, pady=uiAttr["pady"])
        #logging prototype logging(historyWidgets, name, password)
        #doo some validation later on
        logIn=Button(fr, text="Log In", 
            command=lambda: logging(fr, widgets([ signUp, *widgets_t]), nam.get(), pas.get()))
        logIn.grid(row=4, column=0, padx=40, pady=20)
        #
        widgets_t=[ username, usernameE, password, passwordE, logIn]
        signUp = Button(fr, text="Don't Have An Account?", font=smallFont,
                        command=lambda : commander(fr, widgets([signUp, *widgets_t ]), err, 'signUp'))
        signUp.grid(row=5, column=0, padx=40, pady=20)
    elif(page=='newPassword'):
        frame=LabelFrame(fr, text="New Password", pady=1, font=fontStyle)
        frame.grid(row=0, column=0, columnspan=2)
        email=Label(frame, text="Please make sure you enter a strong password.", font=smallFont)
        email.grid(row=1, column=0, padx= 5)

        code=Label(frame, text="Password: ", font=smallFont)
        code.grid(row=2, column=0, padx= 5)

        codeValue=Entry(frame, show="*", width=60)
        codeValue.grid(row=2, column=1, pady=1)

        codeC=Label(frame, text="Confirm: ", font=smallFont)
        codeC.grid(row=3, column=0, padx= 5)

        codeConfirm=Entry(frame, show="*", width=60)
        codeConfirm.grid(row=3, column=1, pady=1)

        widgets_t=[frame, email, code, codeValue, codeC, codeConfirm]
        submit=Button(frame, text="Log In", padx=1, pady=2, font=smallFont,
            command=lambda: logging(fr, widgets([ submit, *widgets_t]), '', ''))
        submit.grid(row=4, column=0, padx= 5)
    elif(page=='forgot'):
        frame=LabelFrame(fr, text="Resetting The Password", pady=1, font=fontStyle)
        frame.grid(row=0, column=0, columnspan=3)
        email=Label(frame,text="Please check out your emails a code has been send to you.", font=smallFont)
        email.grid(row=1, column=0, padx= 5)

        code=Label(frame, text= "Code: ", width=60, font=smallFont)
        code.grid(row=2, column=0, padx= 5)

        codeValue=Entry(frame, show="*", width=50)
        codeValue.grid(row=3, column=0, pady=1)

        widgets_t=[frame, email, code, codeValue]
        submit=Button(frame, text="New Password", font=smallFont, 
            command=lambda: commander(fr, widgets([submit, *widgets_t]), err, 'newPassword'))
        submit.grid(row=4, column=0, padx= 5)
    else:
        signIn=Button(fr, text="Sign In", font=smallFont, 
            command=lambda: commander(fr, widgets([signIn, signUp, forgotPassword]), err, 'signIn'))
        signIn.grid(row=0, column=0, padx=40, pady=20)
        signUp=Button(fr, text="Sign Up", font=smallFont,
            command=lambda: commander(fr, widgets([signUp, signIn, forgotPassword]), err, 'signUp'))
        signUp.grid(row=1, column=0, padx=40, pady=20)

        forgotPassword=Button(fr, text="Forgot Password", font=smallFont, borderwidth=0, fg='blue',
            command=lambda: commander(fr, widgets([signUp, signIn, forgotPassword]), err, 'forgot'))
        forgotPassword.grid(row=2, column=0, padx=40, pady=20)
    if(errMassage):
        lab=Label(fr, text=errMassage).grid(row=20, column=0, columnspan=W+E)

def commander(fr, last, err='', page="log", lastPacked=False):
    deleteWidgets(last)
    register(fr, last, err, page)
