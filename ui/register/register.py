from tkinter import *

def register(fr, last, err='', page="log", lastPacked=False):
    if(page=="signUp"):
        global signUpT
        signUpT = Button(fr, text="Sign In", command=lambda : commander(fr, signUpT, err, 'signIn'))
        signUpT.grid(row=0, column=1, padx=40, pady=20)
    elif(page=="signIn"):
        signInT = Button(fr, text="Sign Up", command=lambda: commander(fr, signInT, err, 'signUp'))
        signInT.grid(row=1, column=1, padx=40, pady=20)
    else:
        signIn=Button(fr, text="Sign In", command=lambda: commander(fr, last, err, 'signIn'))
        signIn.grid(row=0, column=0, padx=40, pady=20)
        signUp=Button(fr, text="Sign Up", command=lambda: commander(fr, last, err, 'signUp'))
        signUp.grid(row=1, column=0, padx=40, pady=20)
    if(err):
        lab=Label(fr, text=err).grid(row=2, column=0, columnspan=W+E)
    return {}

def commander(fr, last, err='', page="log", lastPacked=False):
    register(fr, signUpT, err, 'signIn')
    if(lastPacked):
        last.pack_forget()
    else:
        last.grid_forget()