# List box example for multiple selections

from Tkinter import *
import Tkinter

root = Tk()
frame = Frame(root)
frame.pack()

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected items: %s'%[w.get(int(i)) for i in w.curselection()]
lb = Listbox(frame, name='lb', selectmode=MULTIPLE)

for item in ["one", "two", "three", "four"]:
    lb.insert(END, item)

lb.bind('<<ListboxSelect>>', onselect)
lb.pack()

root.mainloop()