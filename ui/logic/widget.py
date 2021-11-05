
def widget(widget_t, packed=False):
    return {
        'widget': widget_t,
        'packed': packed
    }

def deleteWidget(widget_t):
    if(widget_t['packed']):
        widget_t['widget'].pack_forget()
    else:
        widget_t['widget'].grid_forget()

def deleteWidgets(widgets_t):
    for wid in widgets_t:
        deleteWidget(wid)

def widgets(array=[], packed=False):
    list_t=[]
    for item in array:
        list_t.append(widget(item, packed))
    return list_t
