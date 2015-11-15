from Tkinter import *
import search_database

def selection(event):
    select=event.widget.curselection()
    value=event.widget.get(select[0])
    print (value)
    return

def list_test():
    root = Tk()
    li=search_database.search_db("st_id,st_name","Stats",'')
    liBox=Listbox(root)

    for i in li:
        liBox.insert(0,i[1])

    liBox.pack()

    liBox.bind('<Double-Button-1>', selection)

    root.mainloop()

    return


list_test()
