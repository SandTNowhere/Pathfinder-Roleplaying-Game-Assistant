from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)

name = ttk.Entry(content, width=30)
namelbl = ttk.Label(content, text="Name")
align = ttk.Entry(content, width=10)
alignlbl = ttk.Label(content, text="Alignment")
player = ttk.Entry(content, width=30)
playerlbl = ttk.Label(content, text="Player")
level = ttk.Entry(content, width=41)
levellbl = ttk.Label(content, text="Character Level")
deity = ttk.Entry(content, width=15)
deitylbl = ttk.Label(content, text="Deity")
homeland = ttk.Entry(content, width=14)
homelandlbl = ttk.Label(content, text="Homeland")
race = ttk.Entry(content, width=22)
racelbl = ttk.Label(content, text="Race")
size = ttk.Entry(content, width=5)
sizelbl = ttk.Label(content, text="Size")
gender = ttk.Entry(content, width=6)
genderlbl = ttk.Label(content, text="Gender")
age = ttk.Entry(content, width=4)
agelbl = ttk.Label(content, text="Age")

quit = ttk.Button(content, text="Quit", command=frame.quit)



content.grid(column=0, row=0)
name.grid(column=1, row=2, columnspan=3)
namelbl.grid(column=1, row=3, sticky=(N, W))
align.grid(column=4, row=2, columnspan=1)
alignlbl.grid(column=4, row=3, sticky=(N, W))
player.grid(column=5, row=2, columnspan=3)
playerlbl.grid(column=5, row=3, sticky=(N,W))
level.grid(column=1, row=4, columnspan=4)
levellbl.grid(column=1, row=5, sticky=(N,W))
deity.grid(column=5, row=4)
deitylbl.grid(column=5, row=5, sticky=(N,W))
homeland.grid(column=6, row=4)
homelandlbl.grid(column=6, row=5, sticky=(N,W))
race.grid(column=1, row=7,columnspan=2)
racelbl.grid(column=1, row=8, sticky=(N,W))
size.grid(column=3, row=7, sticky=(W))
sizelbl.grid(column=3, row=8, sticky=(N,W))
gender.grid(column=4, row=7, sticky=(W))
genderlbl.grid(column=4, row=8, sticky=(N,W))
age.grid(column=5, row=7, stick=(W))
agelbl.grid(column=5, row=8, sticky=(N,W))

quit.grid(column=8, row=14)


root.mainloop()
