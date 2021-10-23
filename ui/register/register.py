from tkinter import *

def register(fr, last=[], err='', page="log", lastPacked=False):
    if(page=="signUp"):
        form_t=form(fr)
        widgets=form_t[0]
        print(form_t[1])
        signUp = Button(fr, text="Sign In", command=lambda : commander(fr, [signUp, *widgets ], err, 'signIn'))
        signUp.grid(row=7, column=0, padx=40, pady=20)

    elif(page=="signIn"):
        signIn = Button(fr, text="Sign Up", command=lambda: commander(fr, [signIn], err, 'signUp'))
        signIn.grid(row=1, column=1, padx=40, pady=20)
    else:
        signIn=Button(fr, text="Sign In", command=lambda: commander(fr, [signIn, signUp], err, 'signIn'))
        signIn.grid(row=0, column=0, padx=40, pady=20)
        signUp=Button(fr, text="Sign Up", command=lambda: commander(fr, [signUp, signIn], err, 'signUp'))
        signUp.grid(row=1, column=0, padx=40, pady=20)
    if(err):
        lab=Label(fr, text=err).grid(row=2, column=0, columnspan=W+E)
    return {}

def commander(fr, last, err='', page="log", lastPacked=False):
    removeLast(last, lastPacked)
    register(fr, last, err, page, lastPacked)

#Clearing out the frame
def removeLast(last, lastPacked):
    for widget in last:
        if(lastPacked):
            widget.pack_forget()
        else:
            widget.grid_forget()

def form(fr):
    values={
        "username": "",
        "email": "",
        "password": ""
    }
    uiAttr={
        "font": ('Helvetica bold',10),
        "width": 40,
        "pady": 5
    }

    def setValue(key, var):
        values[key]=var.get()
        print(values)

    nam=StringVar() 
    ema=StringVar() 
    pas=StringVar()

    nam.trace("w", lambda name, index, mode, nam=nam: setValue("username", nam))
    ema.trace("w", lambda name, index, mode, ema=ema: setValue("email", ema))
    pas.trace("w", lambda name, index, mode, pas=pas: setValue("password", pas))

    username=Label(fr, text="Username", width=50, font=uiAttr["font"])
    username.grid(row=0, column=0)
    usernameE=Entry(fr, width=uiAttr["width"], textvariable=nam)
    usernameE.grid(row=1, column=0, pady=uiAttr["pady"])

    email=Label(fr, text="Email", font=uiAttr["font"])
    email.grid(row=2, column=0)
    emailE=Entry(fr, width=uiAttr["width"], textvariable=ema)
    emailE.grid(row=3, column=0, pady=uiAttr["pady"])

    password=Label(fr, text="Password", font=uiAttr["font"])
    password.grid(row=4, column=0)
    passwordE=Entry(fr, width=uiAttr["width"], textvariable=pas)
    passwordE.grid(row=5, column=0, pady=uiAttr["pady"])

    signUp=Button(fr, text="Create Account")
    signUp.grid(row=6, column=0, padx=40, pady=20)
    return ([ username, usernameE, email, emailE, password, passwordE, signUp], values)