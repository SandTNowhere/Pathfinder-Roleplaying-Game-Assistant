from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)


namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)
classlbl = ttk.Label(content, text="Class")
cclass = ttk.Entry(content)
racelbl = ttk.Label(content, text="Race")
race = ttk.Entry(content)
strlbl = ttk.Label(content, text="Strength")
str = ttk.Entry(content)
dexlbl = ttk.Label(content, text="Dexterity")
dex = ttk.Entry(content)
vitlbl = ttk.Label(content, text="Vitality")
vit = ttk.Entry(content)
intlbl = ttk.Label(content, text="Intelligence")
int = ttk.Entry(content)

quit = ttk.Button(content, text="Quit", command=frame.quit)

content.grid(column=0, row=0, sticky=(N, S, E, W))
namelbl.grid(column=1, row=2, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=1, row=3, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
classlbl.grid(column=1, row=4, columnspan=2, sticky=(N, W), padx=5)
cclass.grid(column=1, row=5, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
racelbl.grid(column=1, row=6, columnspan=2, sticky=(N, W), padx=5)
race.grid(column=1, row=7, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
strlbl.grid(column=3, row=2, columnspan=2, sticky=(N, W), padx=5)
str.grid(column=3, row=3, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
dexlbl.grid(column=3, row=4, columnspan=2, sticky=(N, W), padx=5)
dex.grid(column=3, row=5, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
vitlbl.grid(column=3, row=6, columnspan=2, sticky=(N, W), padx=5)
vit.grid(column=3, row=7, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
intlbl.grid(column=3, row=8, columnspan=2, sticky=(N, W), padx=5)
int.grid(column=3, row=9, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

quit.grid(column=5, row=14)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()