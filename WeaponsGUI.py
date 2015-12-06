from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
content.grid(    column=0, row=0)


name = ttk.Entry(content, width=45)
namelbl = ttk.Label(content, text="Character Name", background='black', foreground='white')
name.grid(       column=1, row=2, columnspan=3)
namelbl.grid(    column=1, row=3, sticky=(N, W))

root.mainloop()
