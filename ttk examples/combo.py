#Combobox implementation of a dropdown selection
from tkinter import *
from tkinter.ttk import *

top = Tk()
countryvals = ['US', 'Mexico', 'Canadialand','1','2','3'] #List of values in drop down (will alow variable sizes and values for the drop down)
countryvar = StringVar() #Variable that will be saved to

country = Combobox(top, textvariable=countryvar, values=countryvals, state='readonly', height=3) #Readonly does not allow custom user input, height limits the box size and adds a scrollbar if needed
country.bind('<<ComboboxSelected>>') #Can add function to execute on selection, otherwise just updates textvariable
country.pack()
top.mainloop()
