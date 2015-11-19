# Simple notebook example
from Tkinter import *
from ttk import *

root = Tk() # create a top-level window

master = Frame(root, name='master') # create Frame in "root"
master.pack(fill=BOTH) # fill both sides of the parent

root.title('EZ') # title for top-level window
# quit if the window is deleted
root.protocol("WM_DELETE_WINDOW", master.quit)

nb = Notebook(master, name='nb') # create Notebook in "master"
nb.pack(fill=BOTH, padx=2, pady=3) # fill "master" but pad sides

# create each Notebook tab in a Frame
master_foo = Frame(nb, name='master-foo')
Label(master_foo, text="this is foo").pack(side=LEFT)
# Button to quit app on right
btn = Button(master_foo, text="foo", command=master.quit)
btn.pack(side=RIGHT)
nb.add(master_foo, text="foo") # add tab to Notebook

# repeat for each tab
master_bar = Frame(master, name='master-bar')
Label(master_bar, text="this is bar").pack(side=LEFT)
btn = Button(master_bar, text="bar", command=master.quit)
btn.pack(side=RIGHT)
nb.add(master_bar, text="bar")

# start the app
if __name__ == "__main__":
    master.mainloop() # call master's Frame.mainloop() method.
    #root.destroy() # if mainloop quits, destroy window