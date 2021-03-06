from tkinter import *
from tkinter import ttk
import search_database
from search_database import search_db
import Character
from Character import Character

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
        self._create_abilities_tab(character)
    def _create_abilities_tab(self, character):
            content = ttk.Frame(character, padding=(3,3,12,12))
            content.grid(column=0, row=0)

            """ ability declaration """
            abnamelbl = ttk.Label(content, text="Ability Name", background='black', foreground='white')
            abscorelbl = ttk.Label(content, text = "Abl Score | Mod", background='black', foreground='white')
            tempadjlbl = ttk.Label(content, text = "Temp Adj | Mod", background='black', foreground='white')
            strlbl = ttk.Label(content, text = "   Strength    "  , background='black', foreground='white')
            strabs = ttk.Entry(content, width = 6)
            strabm = ttk.Entry(content, width = 6)
            strtma = ttk.Entry(content, width = 6)
            strtmm = ttk.Entry(content, width = 6) 
            dexlbl = ttk.Label(content, text = "   Dexterity    ", background='black', foreground='white')
            dexabs = ttk.Entry(content, width = 6)
            dexabm = ttk.Entry(content, width = 6)
            dextma = ttk.Entry(content, width = 6)
            dextmm = ttk.Entry(content, width = 6)
            conlbl = ttk.Label(content, text = "Constitution", background='black', foreground='white')
            conabs = ttk.Entry(content, width = 6)
            conabm = ttk.Entry(content, width = 6)
            contma = ttk.Entry(content, width = 6)
            contmm = ttk.Entry(content, width = 6)
            intlbl = ttk.Label(content, text = " Intelligence ", background='black', foreground='white')
            intabs = ttk.Entry(content, width = 6)
            intabm = ttk.Entry(content, width = 6)
            inttma = ttk.Entry(content, width = 6)
            inttmm = ttk.Entry(content, width = 6)
            wislbl = ttk.Label(content, text = "   Wisdom    ", background='black', foreground='white')
            wisabs = ttk.Entry(content, width = 6)
            wisabm = ttk.Entry(content, width = 6)
            wistma = ttk.Entry(content, width = 6)
            wistmm = ttk.Entry(content, width = 6)
            chalbl = ttk.Label(content, text = "   Charisma  ", background='black', foreground='white')
            chaabs = ttk.Entry(content, width = 6)
            chaabm = ttk.Entry(content, width = 6)
            chatma = ttk.Entry(content, width = 6)
            chatmm = ttk.Entry(content, width = 6)

            """ ability placement """
            abnamelbl.grid(  column=1, row=9, sticky = (W))
            abscorelbl.grid( column=2, row=9, sticky = (W))
            tempadjlbl.grid( column=3, row=9, sticky = (W))
            strlbl.grid(     column=1, row=10, columnspan = 2, sticky = (W))
            strabs.grid(     column=2, row=10, sticky = (W))
            strabm.grid(     column=2, row=10, sticky = (E), padx = 5)
            strtma.grid(     column=3, row=10, sticky = (W), padx = 3)
            strtmm.grid(     column=3, row=10, sticky = (E), padx = 8)
            dexlbl.grid(     column=1, row=11, columnspan = 2, sticky = (W))
            dexabs.grid(     column=2, row=11, sticky = (W))
            dexabm.grid(     column=2, row=11, sticky = (E), padx = 5)
            dextma.grid(     column=3, row=11, sticky = (W), padx = 3)
            dextmm.grid(     column=3, row=11, sticky = (E), padx = 8)
            conlbl.grid(     column=1, row=12, columnspan = 2, sticky = (W))
            conabs.grid(     column=2, row=12, sticky = (W))
            conabm.grid(     column=2, row=12, sticky = (E), padx = 5)
            contma.grid(     column=3, row=12, sticky = (W), padx = 3)
            contmm.grid(     column=3, row=12, sticky = (E), padx = 8)
            intlbl.grid(     column=1, row=13, columnspan = 2, sticky = (W))
            intabs.grid(     column=2, row=13, sticky = (W))
            intabm.grid(     column=2, row=13, sticky = (E), padx = 5)
            inttma.grid(     column=3, row=13, sticky = (W), padx = 3)
            inttmm.grid(     column=3, row=13, sticky = (E), padx = 8)
            wislbl.grid(     column=1, row=14, columnspan = 2, sticky = (W))
            wisabs.grid(     column=2, row=14, sticky = (W))
            wisabm.grid(     column=2, row=14, sticky = (E), padx = 5)
            wistma.grid(     column=3, row=14, sticky = (W), padx = 3)
            wistmm.grid(     column=3, row=14, sticky = (E), padx = 8)
            chalbl.grid(     column=1, row=15, columnspan = 2, sticky = (W))
            chaabs.grid(     column=2, row=15, sticky = (W))
            chaabm.grid(     column=2, row=15, sticky = (E), padx = 5)
            chatma.grid(     column=3, row=15, sticky = (W), padx = 3)
            chatmm.grid(     column=3, row=15, sticky = (E), padx = 8)

            """ Basic attribute declaration """
            hplbl = ttk.Label(content, text = "Total HP", background='black', foreground='white')
            hp = ttk.Entry(content, width = 10)
            drlbl = ttk.Label(content, text = "DR", foreground='grey')
            dmgres = ttk.Entry(content, width = 5)
            speedlbl = ttk.Label(content, text = "Speed", background='black', foreground='white')
            bspeed = ttk.Entry(content, width = 10)
            bpdlbl = ttk.Label(content, text = " Base", foreground='grey')
            aspeed = ttk.Entry(content, width = 10)
            asplbl = ttk.Label(content, text = " w/ Armor", foreground='grey')
            sspeed = ttk.Entry(content, width = 5)
            ssplbl = ttk.Label(content, text = "Swim", foreground='grey')
            fspeed = ttk.Entry(content, width = 4)
            fsplbl = ttk.Label(content, text = "Fly", foreground='grey')
            maneuv = ttk.Entry(content, width = 10)
            mnvlbl = ttk.Label(content, text = "Maneuver", foreground='grey')
            cspeed = ttk.Entry(content, width = 5)
            csplbl = ttk.Label(content, text = "Climb", foreground='grey')
            burspd = ttk.Entry(content, width = 4)
            brslbl = ttk.Label(content, text = "Burw", foreground='grey')
            tmdlbl = ttk.Label(content, text = "Temp Mod", foreground='grey')
            tmpmod1 = ttk.Entry(content, width = 9)
            tmpmod2 = ttk.Entry(content, width = 9)
            tmpmod3 = ttk.Entry(content, width = 9)
            wcrlbl = ttk.Label(content, text = "Wounds / HP", background='black', foreground='white')
            wcr1 = ttk.Entry(content, width = 31)
            wcr2 = ttk.Entry(content, width = 31)
            nldlbl = ttk.Label(content, text = "Non-Lethal Damage", background='black', foreground='white')
            nld = ttk.Entry(content, width = 31)
            inilbl = ttk.Label(content, text = "  Initiative  ", background='black', foreground='white')
            initot = ttk.Entry(content, width = 5)
            inidex = ttk.Entry(content, width = 4)
            inimsc = ttk.Entry(content, width = 4)
            inip = ttk.Label(content, text = "+")
            inie = ttk.Label(content, text = "=")
            inidexlbl = ttk.Label(content, text = "Dex", foreground='grey')
            inimsclbl = ttk.Label(content, text = "Misc", foreground='grey')
            initotlbl = ttk.Label(content, text = "Total", foreground='grey')
            inimodlbl = ttk.Label(content, text = "  Modifier  ", foreground='grey')

            """ Basic attribute placement"""
            hplbl.grid(      column=4, row=9, sticky = (E))
            hp.grid(         column=5, row=9, sticky = (W))
            drlbl.grid(      column=6, row=9, sticky = (W))
            dmgres.grid(     column=6, row=9, sticky = (E))
            speedlbl.grid(   column=7, row=9, sticky = (E), padx = 5)
            bspeed.grid(     column=8, row=9, sticky = (W))
            bpdlbl.grid(     column=8, row=10, sticky = (W))
            aspeed.grid(     column=9, row=9, sticky = (W))
            asplbl.grid(     column=9, row=10, sticky = (W))
            sspeed.grid(     column=7, row=11, sticky = (W))
            ssplbl.grid(     column=7, row=12, sticky = (W))
            fspeed.grid(     column=7, row=11, sticky = (E))
            fsplbl.grid(     column=7, row=12, sticky = (E))
            maneuv.grid(     column=8, row=11, sticky = (W))
            mnvlbl.grid(     column=8, row=12, sticky = (W))
            cspeed.grid(     column=9, row=11, sticky = (W))
            csplbl.grid(     column=9, row=12, sticky = (W))
            burspd.grid(     column=9, row=11, sticky = (E))
            brslbl.grid(     column=9, row=12, sticky = (E))
            tmdlbl.grid(     column=10, row=9, sticky = (E))
            tmpmod1.grid(    column=10, row=10, sticky = (W), padx = 3)
            tmpmod2.grid(    column=10, row=11, sticky = (W), padx = 3)
            tmpmod3.grid(    column=10, row=12, sticky = (W), padx = 3)
            wcrlbl.grid(     column=4, row=10, columnspan = 2, sticky = (W))
            wcr1.grid(       column=4, row=11, columnspan = 3, sticky = (NE))
            wcr2.grid(       column=4, row=12, columnspan = 3, sticky = (NE))
            nldlbl.grid(     column=4, row=13, columnspan = 2, sticky = (W))
            nld.grid(        column=4, row=14, columnspan = 3, sticky = (NE))
            inilbl.grid(     column=4, row=16, columnspan = 2, sticky = (W))
            initot.grid(     column=5, row=16, sticky = (E), padx = 12)
            inie.grid(       column=5, row=16, sticky = (E))
            inidex.grid(     column=6, row=16, sticky = (E))
            inip.grid(       column=6, row=16)
            inimsc.grid(     column=6, row=16, sticky = (W))
            inidexlbl.grid(  column=6, row=15, sticky = (E))
            inimsclbl.grid(  column=6, row=15, sticky = (W))
            initotlbl.grid(  column=5, row=15, sticky = (E), padx = 12)
            inimodlbl.grid(  column=4, row=15, sticky = (W))

            """ Fortitude, Reflex, Will Declaration """
            frwtotlbl = ttk.Label(content, text = "Total", foreground='grey')
            frwbaslbl = ttk.Label(content, text = "Base", foreground='grey')
            frwabllbl = ttk.Label(content, text = "Abil.", foreground='grey')
            frwmaglbl = ttk.Label(content, text = "Magic", foreground='grey')
            frwmsclbl = ttk.Label(content, text = "Misc", foreground='grey')
            frwtmplbl = ttk.Label(content, text = "Temp", foreground='grey')
            forlbl = ttk.Label(content, text = "Fortitude ", background='black', foreground='white')
            reflbl = ttk.Label(content, text = "  Reflex    ", background='black', foreground='white')
            willbl = ttk.Label(content, text = "     Will     ", background='black', foreground='white')
            fortot = ttk.Entry(content, width = 3)
            reftot = ttk.Entry(content, width = 3)
            wiltot = ttk.Entry(content, width = 3)
            forbas = ttk.Entry(content, width = 3)
            refbas = ttk.Entry(content, width = 3)
            wilbas = ttk.Entry(content, width = 3)
            forabl = ttk.Entry(content, width = 3)
            refabl = ttk.Entry(content, width = 3)
            wilabl = ttk.Entry(content, width = 3)
            formag = ttk.Entry(content, width = 3)
            refmag = ttk.Entry(content, width = 3)
            wilmag = ttk.Entry(content, width = 3)
            formsc = ttk.Entry(content, width = 3)
            refmsc = ttk.Entry(content, width = 3)
            wilmsc = ttk.Entry(content, width = 3)
            fortmp = ttk.Entry(content, width = 3)
            reftmp = ttk.Entry(content, width = 3)
            wiltmp = ttk.Entry(content, width = 3)
            frwe1 = ttk.Label(content, text = "=")
            frwe2 = ttk.Label(content, text = "=")
            frwe3 = ttk.Label(content, text = "=")
            frwp1 = ttk.Label(content, text = "+")
            frwp2 = ttk.Label(content, text = "+")
            frwp3 = ttk.Label(content, text = "+")
            frwp4 = ttk.Label(content, text = "+")
            frwp5 = ttk.Label(content, text = "+")
            frwp6 = ttk.Label(content, text = "+")
            frwp7 = ttk.Label(content, text = "+")
            frwp8 = ttk.Label(content, text = "+")
            frwp9 = ttk.Label(content, text = "+")
            frwp10 = ttk.Label(content, text = "+")
            frwp11 = ttk.Label(content, text = "+")
            frwp12 = ttk.Label(content, text = "+")
            frwp13 = ttk.Label(content, text = "+")
            frwp14 = ttk.Label(content, text = "+")
            frwp15 = ttk.Label(content, text = "+")
            frwp16 = ttk.Label(content, text = "+")

            """ Fortitude, Reflex, Will Placement """
            frwtotlbl.grid( column=8, row = 13, sticky = (W) )
            frwbaslbl.grid( column=8, row = 13, sticky = (E), padx = 5 )
            frwabllbl.grid( column=9, row = 13, sticky = (W) )
            frwmaglbl.grid( column=9, row = 13, sticky = (E) )
            frwmsclbl.grid( column=10, row = 13, sticky = (W) )
            frwtmplbl.grid( column=10, row = 13, sticky = (E) )
            forlbl.grid(    column=7, row = 14, sticky = (E) )
            reflbl.grid(    column=7, row = 15, sticky = (E) )
            willbl.grid(    column=7, row = 16, sticky = (E) )
            fortot.grid(    column=8, row = 14, sticky = (W) )
            reftot.grid(    column=8, row = 15, sticky = (W) )
            wiltot.grid(    column=8, row = 16, sticky = (W) )
            forbas.grid(    column=8, row = 14, sticky = (E), padx = 9 )
            refbas.grid(    column=8, row = 15, sticky = (E), padx = 9 )
            wilbas.grid(    column=8, row = 16, sticky = (E), padx = 9 )
            forabl.grid(    column=9, row = 14, sticky = (W) )
            refabl.grid(    column=9, row = 15, sticky = (W) )
            wilabl.grid(    column=9, row = 16, sticky = (W) )
            formag.grid(    column=9, row = 14, sticky = (E), padx = 9 )
            refmag.grid(    column=9, row = 15, sticky = (E), padx = 9 )
            wilmag.grid(    column=9, row = 16, sticky = (E), padx = 9 )
            formsc.grid(    column=10, row = 14, sticky = (W) )
            refmsc.grid(    column=10, row = 15, sticky = (W) )
            wilmsc.grid(    column=10, row = 16, sticky = (W) )
            fortmp.grid(    column=10, row = 14, sticky = (E), padx = 9 )
            reftmp.grid(    column=10, row = 15, sticky = (E), padx = 9 )
            wiltmp.grid(    column=10, row = 16, sticky = (E), padx = 9 )
            frwe1.grid(     column=8, row = 14, sticky = (W), padx = 22)
            frwe2.grid(     column=8, row = 15, sticky = (W), padx = 22)
            frwe3.grid(     column=8, row = 16, sticky = (W), padx = 22)
            frwp1.grid(     column=8, row = 14, sticky = (E) )
            frwp2.grid(     column=8, row = 15, sticky = (E) )
            frwp3.grid(     column=8, row = 16, sticky = (E) )
            frwp4.grid(     column=9, row = 14, sticky = (W), padx = 22 )
            frwp5.grid(     column=9, row = 15, sticky = (W), padx = 22 )
            frwp6.grid(     column=9, row = 16, sticky = (W), padx = 22 )
            frwp7.grid(     column=9, row = 14, sticky = (E) )
            frwp8.grid(     column=9, row = 15, sticky = (E) )
            frwp9.grid(     column=9, row = 16, sticky = (E) )
            frwp10.grid(    column=10, row = 14, sticky = (W), padx = 22 )
            frwp11.grid(    column=10, row = 15, sticky = (W), padx = 22 )
            frwp12.grid(    column=10, row = 16, sticky = (W), padx = 22 )

            """ armor class declarations """
            armclslbl= ttk.Label(content, text = "     AC    ", background='black', foreground='white')
            touchalbl= ttk.Label(content, text = " Touch  ", background='black', foreground='white')
            flatftlbl= ttk.Label(content, text = "Flat foot", background='black', foreground='white')
            atftotlbl= ttk.Label(content, text = "Total", foreground='grey')
            atfarmlbl= ttk.Label(content, text = "Armor", foreground='grey')
            arfshdlbl= ttk.Label(content, text = "Shield", foreground='grey')
            arfdexlbl= ttk.Label(content, text = "Dex Mod", foreground='grey')
            arfsizlbl= ttk.Label(content, text = "Size Mod", foreground='grey')
            arfnatlbl= ttk.Label(content, text = "Natural", foreground='grey')
            arfdfllbl= ttk.Label(content, text = "Deflect", foreground='grey')
            arfmsclbl= ttk.Label(content, text = "Misc Mod", foreground='grey')

            armortot= ttk.Entry(content, width = 8)
            touchtot= ttk.Entry(content, width = 8)
            fltfttot= ttk.Entry(content, width = 8)
            armarbon= ttk.Entry(content, width = 6)
            fltarbon= ttk.Entry(content, width = 6)
            armshbon= ttk.Entry(content, width = 6)
            fltshbon= ttk.Entry(content, width = 6)
            armordex= ttk.Entry(content, width = 6)
            touchdex= ttk.Entry(content, width = 6)
            armorsiz= ttk.Entry(content, width = 6)
            touchsiz= ttk.Entry(content, width = 6)
            fltftsiz= ttk.Entry(content, width = 6)
            armornat= ttk.Entry(content, width = 6)
            fltftnat= ttk.Entry(content, width = 6)
            armordfl= ttk.Entry(content, width = 6)
            touchdfl= ttk.Entry(content, width = 6)
            fltftdfl= ttk.Entry(content, width = 6)
            armormsc= ttk.Entry(content, width = 6)
            touchmsc= ttk.Entry(content, width = 6)
            fltftmsc= ttk.Entry(content, width = 6)

            atfep01= ttk.Label(content, text = "=  10 +")
            atfep02= ttk.Label(content, text = "=  10 +")
            atfep03= ttk.Label(content, text = "=  10 +")
            atfp01= ttk.Label(content, text = "+")
            atfp02= ttk.Label(content, text = "+")
            atfp03= ttk.Label(content, text = "+")
            atfp04= ttk.Label(content, text = "+")
            atfp05= ttk.Label(content, text = "+")
            atfp06= ttk.Label(content, text = "+")
            atfp07= ttk.Label(content, text = "+")
            atfp08= ttk.Label(content, text = "+")
            atfp09= ttk.Label(content, text = "+")
            atfp10= ttk.Label(content, text = "+")
            atfp11= ttk.Label(content, text = "+")
            atfp12= ttk.Label(content, text = "+")
            atfp13= ttk.Label(content, text = "+")
            atfp14= ttk.Label(content, text = "+")
            atfp15= ttk.Label(content, text = "+")
            atfp16= ttk.Label(content, text = "+")
            atfp17= ttk.Label(content, text = "+")

            """ armor class placement """
            armclslbl.grid( column = 2, row = 17, sticky = (E), padx=5)
            touchalbl.grid( column = 2, row = 18, sticky = (E), padx=5)
            flatftlbl.grid( column = 2, row = 19, sticky = (E), padx=5)
            atftotlbl.grid( column = 3, row = 20, sticky = (W), padx=5)
            atfarmlbl.grid( column = 4, row = 20)
            arfshdlbl.grid( column = 5, row = 20)
            arfdexlbl.grid( column = 6, row = 20)
            arfsizlbl.grid( column = 7, row = 20)
            arfnatlbl.grid( column = 8, row = 20)
            arfdfllbl.grid( column = 9, row = 20)
            arfmsclbl.grid( column = 10, row = 20)
            armortot.grid(  column = 3, row = 17, sticky = (W))
            touchtot.grid(  column = 3, row = 18, sticky = (W))
            fltfttot.grid(  column = 3, row = 19, sticky = (W))
            armarbon.grid(  column = 4, row = 17)
            fltarbon.grid(  column = 4, row = 19)
            armshbon.grid(  column = 5, row = 17)
            fltshbon.grid(  column = 5, row = 19)
            armordex.grid(  column = 6, row = 17)
            touchdex.grid(  column = 6, row = 18)
            armorsiz.grid(  column = 7, row = 17)
            touchsiz.grid(  column = 7, row = 18)
            fltftsiz.grid(  column = 7, row = 19)
            armornat.grid(  column = 8, row = 17)
            fltftnat.grid(  column = 8, row = 19)
            armordfl.grid(  column = 9, row = 17)
            touchdfl.grid(  column = 9, row = 18)
            fltftdfl.grid(  column = 9, row = 19)
            armormsc.grid(  column = 10, row = 17)
            touchmsc.grid(  column = 10, row = 18)
            fltftmsc.grid(  column = 10, row = 19)
            atfep01.grid(   column = 3, row = 17, sticky=(E))
            atfep02.grid(   column = 3, row = 18, sticky=(E))
            atfep03.grid(   column = 3, row = 19, sticky=(E))
            atfp01.grid(    column = 4, row = 17, sticky=(E))
            atfp02.grid(    column = 5, row = 17, sticky=(E))
            atfp03.grid(    column = 6, row = 17, sticky=(E))
            atfp04.grid(    column = 7, row = 17, sticky=(E))
            atfp05.grid(    column = 8, row = 17, sticky=(E))
            atfp06.grid(    column = 9, row = 17, sticky=(E))
            atfp07.grid(    column = 5, row = 18, sticky=(E))
            atfp08.grid(    column = 6, row = 18, sticky=(E))
            atfp09.grid(    column = 7, row = 18, sticky=(E))
            atfp10.grid(    column = 8, row = 18, sticky=(E))
            atfp11.grid(    column = 9, row = 18, sticky=(E))
            atfp12.grid(    column = 4, row = 19, sticky=(E))
            atfp13.grid(    column = 5, row = 19, sticky=(E))
            atfp14.grid(    column = 6, row = 19, sticky=(E))
            atfp15.grid(    column = 7, row = 19, sticky=(E))
            atfp16.grid(    column = 8, row = 19, sticky=(E))
            atfp17.grid(    column = 9, row = 19, sticky=(E))

            character.add(content, text='Abilities')
            
if __name__ == '__main__':
    PathfinderGUI().mainloop()
