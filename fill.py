#Functions for populating class objects from pathfinder.db

from CLS import CLS
import Feat
import Item
import Monster
import Race
import Spells
import search_database

def fill_cls(trow): #trow=class name 
    try:
        temp=search_database.search_db('*','Classes',(' WHERE cl_name = '+'"'+trow+'"'))
        temp=temp[0] #search_db returns a list of tuples, this isolates the tuple we need
        tbf=CLS.CLS()
        tbf.name=temp[0][1]
        tbf.reqs=[[temp[2],temp[3]],
                  [temp[4],temp[5]],
                  [temp[6],temp[7]],
                  [temp[8],temp[9]],
                  [temp[10],temp[11]]]
        tbf.hd=temp[12]
        tbf.bab=temp[13]
        tbf.stats=[['reflex',temp[14]],['fort',temp[15]],['will',temp[16]]]
        #not sure this should be here
        tbf.skills=search_database.search_db('sk_name','Skills_By_Class',(' WHERE class="'+trow+'"'))
        tbf.skills=tbf.skills[0]
        tbf.ranks=temp[17]
        tbf.proficiency=temp[18]
        tbf.text=temp[19]
        #also not sure if I should add features here
        #same for archtypes
        tbf.StartingGP=temp[20]
        return trow
    except:
        print("Could not create, are you sure "+trow+" is in the database?")
        return
