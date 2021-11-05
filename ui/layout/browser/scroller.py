from tkinter import *
from tkinter import ttk
from ui.logic.widget import widget, widgets

def scroller(root):
    # Create A Main Frame
    root_t=LabelFrame(root, width=400, padx=2, pady=1)
    root_t.grid(row=1, column=0, columnspan=4)
    main_frame = Frame(root_t)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)
    second_frame.pack()

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    return widgets([second_frame, main_frame, my_canvas, my_scrollbar], packed=True) + [ widget(root_t) ]

