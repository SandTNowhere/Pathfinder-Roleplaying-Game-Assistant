import config
import sqlite3
from config import database
import search_database
from search_database import search_db
import Character
from Character import Character

#chobj = character object to be saved
def save_character(chobj):
    #convert chobj to a list
    insert_me=[chobj.name,chobj.player,chobj.alignment,chobj.deity,chobj.homeland,
               chobj.gender,chobj.age,chobj.height,chobj.weight,chobj.hair,chobj.eyes,
               chobj.notes,chobj.stats['str'],chobj.stats['dex'],chobj.stats['con'],
               chobj.stats['int'],chobj.stats['wis'],chobj.stats['cha'],chobj.stats['maxhp'],
               chobj.stats['hp'],chobj.stats['temp'],'"""'+str(chobj.pRace.Name)+'"""',
               chobj.stats['speed'],chobj.stats['size']]
    temp='"""'
    if chobj.Language:
        for lang in chobj.Language:
            temp+=lang+','
        temp=temp[:len(insert_me)-1]+'""",'
    else: temp='""" """'
    insert_me.append(temp)
    insert_me.append('fighter')

    temp='"""'
    if chobj.Feats:
        for feat in chobj.Feats:
            temp += feat+','
        temp=temp[:len(insert_me)-1]+'""",'
    else:
        temp='""" """'
    insert_me.append(temp)

    temp='"""'
    if chobj.skills:
        for skill in chobj.skills:
            temp+=skill+','
        temp=temp[:len(insert_me)-1]+'"""'
    else:
        temp='""" """'
    insert_me.append(temp)

    insert_me.append(' ')
    insert_me.append(chobj.ranks)
    insert_me.append(chobj.GP)
    insert_me.append(chobj.CumulativeGP)

    temp='"""'
    if chobj.Weapons:
        for weapon in chobj.Weapons:
            temp=weapon+','
        temp=temp[:len(insert_me)-1]+'""",'
    else:
        temp='""" """'
    insert_me.append(temp)
    
    temp='"""'
    if chobj.Armor:
        for armor in chobj.Armor:
            temp+=armor+','
        temp=temp[:len(insert_me)-1]+'""",'
    else:
        temp='""" """'
    insert_me.append(temp)

    temp='"""'
    if chobj.Slots:
        for slot in chobj.Slots:
            temp+=slot+','
        temp=temp[:len(insert_me)-1]+'""",'
    else:
        temp='""" """'
    insert_me.append(temp)

    temp='"""'
    if chobj.Slotless:
        for item in chobj.Slotless:
            temp+=item+','
        temp=temp[:len(insert_me)-1]+'""",'
    else:
        temp='""" """'
    insert_me.append(temp)

    temp='"""'
    if chobj.Inventory:
        for item in chobj.Inventory:
            temp=item+','
        temp=temp[:len(insert_me)-1]+'"""'
    else:
        temp='""" """'
    insert_me.append(temp)

    #open db
    db=sqlite3.connect(database)
    db.text_factory=str
    cursor=db.cursor()

    #is character already in db? If not, find next empty spot in db
    here=search_db('ch_id','Characters',('WHERE ch_name="'+chobj.name+'" AND pl_name="'+chobj.player+'"'))
    if not here:
        here=search_db('max(rowid)','Characters','')[0][0]
        if not here: here=0
        else: here += 1
    else:
        command='DELETE FROM Characters WHERE ch_id='+here+';'
        db.execute(command)
        
    command='INSERT INTO Characters VALUES(?'
    for i in range(36):
        command+=',?'
    command+=');'
    here=[here]+insert_me

    print (command,here)
    
    db.execute(command,here)

    #save and close db
    db.commit()
    db.close()
    return


    
    

