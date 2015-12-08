from tkinter import *
from tkinter import ttk
import search_database
from search_database import search_db

class PathfinderGUI(ttk.Frame):
    def __init__(self, name='pathfindergui'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('NoWhere Pathfinder Assistant')
        Panel = Frame(self, name='char')
        Panel.pack(side=TOP, fill=BOTH, expand=Y)

        character =ttk.Notebook(Panel, name='character')

        character.enable_traversal()
        character.pack(fill=BOTH, expand=Y, padx=2, pady=3)
        self._create_information_tab(character)
        
    def _create_information_tab(self, character):
            content = ttk.Frame(character, padding=(3,3,12,12))
            content.grid(column=0, row=0)

            """varaible declarations for comboboxes"""
            alignmentvar=''
            racevar=''
            sizevar=''
            lang1=''
            lang2=''
            lang3=''
            lang4=''
            lang5=''
            lang6=''

            
            """ basic character information declaration """
            name = ttk.Entry(content, width=47)
            namelbl = ttk.Label(content, text="Character Name")
            align = ttk.Combobox(content, width=10, textvariable=alignmentvar,values=search_db('al_name','Alignments',' ')) 
            alignlbl = ttk.Label(content, text="Alignment")
            player = ttk.Entry(content, width=43)
            playerlbl = ttk.Label(content, text="Player")
            level = ttk.Entry(content, width=58)
            levellbl = ttk.Label(content, text="Character Class and Level")
            deity = ttk.Entry(content, width=21)
            deitylbl = ttk.Label(content, text="Deity")
            homeland = ttk.Entry(content, width=21)
            homelandlbl = ttk.Label(content, text="Homeland")
            race = ttk.Entry(content, width=31)
            racelbl = ttk.Label(content, text="Race")    
            size = ttk.Entry(content, width=15)
            sizelbl = ttk.Label(content, text="Size")
            gender = ttk.Entry(content, width=6)
            genderlbl = ttk.Label(content, text="Gender")
            age = ttk.Entry(content, width=3)
            agelbl = ttk.Label(content, text="Age")
            height = ttk.Entry(content, width=10)
            heightlbl = ttk.Label(content, text="Height")
            weight = ttk.Entry(content, width=10)
            weightlbl = ttk.Label(content, text="Weight")
            hair = ttk.Entry(content, width=10)
            hairlbl = ttk.Label(content, text="Hair")
            eyes = ttk.Entry(content, width=10)
            eyeslbl = ttk.Label(content, text="Eyes")
            languagelbl = ttk.Label(content, text = "Languages Spoken", background='black', foreground='white')
            language1 = ttk.Combobox(content, width = 15, textvariable=lang1, values=search_db('la_name','Languages',''))
            language2 = ttk.Combobox(content, width = 15, textvariable=lang2, values=search_db('la_name','Languages',''))
            language3 = ttk.Combobox(content, width = 15, textvariable=lang3, values=search_db('la_name','Languages',''))
            language4 = ttk.Combobox(content, width = 15, textvariable=lang4, values=search_db('la_name','Languages',''))
            language5 = ttk.Combobox(content, width = 15, textvariable=lang5, values=search_db('la_name','Languages',''))
            language6 = ttk.Combobox(content, width = 15, textvariable=lang6, values=search_db('la_name','Languages',''))
            
            """ basic character information placement """
            content.grid(    column=0, row=0)
            name.grid(       column=1, row=2, columnspan=3)
            namelbl.grid(    column=1, row=3, sticky=(N, W))
            align.grid(      column=4, row=2, sticky=(W), columnspan=1)
            alignlbl.grid(   column=4, row=3, sticky=(N, W))
            player.grid(     column=5, row=2, sticky=(W), columnspan=4)
            playerlbl.grid(  column=5, row=3, sticky=(N,W))
            level.grid(      column=1, row=4, sticky=(W), columnspan=4)
            levellbl.grid(   column=1, row=5, sticky=(N,W), columnspan=3)
            deity.grid(      column=5, row=4, sticky=(W), columnspan=2)
            deitylbl.grid(   column=5, row=5, sticky=(N,W))
            homeland.grid(   column=7, row=4, sticky=(W), columnspan=2)
            homelandlbl.grid(column=7, row=5, sticky=(N,W))
            race.grid(       column=1, row=7, sticky=(W), columnspan=2)
            racelbl.grid(    column=1, row=8, sticky=(N,W))
            size.grid(       column=3, row=7, sticky=(W), columnspan=1)
            sizelbl.grid(    column=3, row=8, sticky=(N,W))
            gender.grid(     column=4, row=7, sticky=(W))
            genderlbl.grid(  column=4, row=8, sticky=(N,W))
            age.grid(        column=4, row=7, sticky=(E))
            agelbl.grid(     column=4, row=8, sticky=(N,E))
            height.grid(     column=5, row=7, sticky=(W), columnspan=1)
            heightlbl.grid(  column=5, row=8, sticky=(N,W))
            weight.grid(     column=6, row=7, sticky=(W), columnspan=1)
            weightlbl.grid(  column=6, row=8, sticky=(N,W))
            hair.grid(       column=7, row=7, sticky=(W), columnspan=1)
            hairlbl.grid(    column=7, row=8, sticky=(N,W))
            eyes.grid(       column=8, row=7, sticky=(W), columnspan=1)
            eyeslbl.grid(    column=8, row=8, sticky=(N,W))
            languagelbl.grid(column=1, row=9, sticky=(W), columnspan=2)
            language1.grid(  column=1, row=10, sticky=(W))
            language2.grid(  column=2, row=10, sticky=(W))
            language3.grid(  column=3, row=10, sticky=(W))
            language4.grid(  column=1, row=11, sticky=(W))
            language5.grid(  column=2, row=11, sticky=(W))
            language6.grid(  column=3, row=11, sticky=(W))            
            
            character.add(content, text='Information')
            

if __name__ == '__main__':
    PathfinderGUI().mainloop()

