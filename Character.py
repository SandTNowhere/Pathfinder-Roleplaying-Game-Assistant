# Python File for Pathfinder Character Assistant

# includes
import Race
import CLS
import Feat
import Item


# Global lists for skills could probably be floated off into a less permanent file for ease of alteration.
# These are dictionaries.
STDSkills = {'acrobatics': 0, 'appraise': 0, 'bluff': 0, 'climb': 0, 'diplomacy': 0, 'disable device': 0,
             'disguise': 0, 'escape artist': 0, 'fly': 0, 'handle animal': 0, 'heal': 0, 'intimidate': 0,
             'linguistics': 0, 'perception': 0, 'ride': 0, 'sense motive': 0, 'slight of hand': 0,
             'spellcraft': 0, 'stealth': 0, 'survival': 0, 'swim': 0, 'use magic device': 0,
             'knowledge(arcana)': 0, 'knowledge(dungeoneering)': 0, 'knowledge(engineering)': 0,
             'knowledge(geography)': 0, 'knowledge(history)': 0, 'knowledge(local)': 0, 'knowledge(nature)': 0,
             'knowledge(nobility)': 0, 'knowledge(planes)': 0, 'knowledge(religion)': 0}
STDBase = {'acrobatics': 'dex', 'appraise': 'int', 'bluff': 'cha', 'climb': 'str', 'diplomacy':
           'cha', 'disable device': 'dex', 'disguise': 'cha', 'escape artist': 'dex', 'fly': 'dex',
           'handle animal': 'cha', 'heal': 'wis', 'intimidate': 'cha', 'linguistics': 'int',
           'perception': 'wis', 'ride': 'dex', 'sense motive': 'wis', 'slight of hand': 'dex',
           'spellcraft': 'int', 'stealth': 'dex', 'survival': 'wis', 'swim': 'swim',
           'use magic device': 'cha', 'knowledge(arcana)': 'int', 'knowledge(dungeoneering)': 'int',
           'knowledge(engineering)': 'int', 'knowledge(geography)': 'int', 'knowledge(history)': 'int',
           'knowledge(local)': 'int', 'knowledge(nature)': 'int', 'knowledge(nobility)': 'int', 'knowledge(planes)': 'int',
           'knowledge(religion)': 'int'}
# the variable skills have been left out (craft, Knowledge (should be added hard), proffession,
# perform, artistry, and lore.

# an optional list to allow acces to may ingore for now, it's more a test
CondensedSkills = {'acrobatics': 0, 'athletics': 0, 'finesse': 0, 'influence': 0, 'nature': 0,
                   'perception': 0, 'performance': 0, 'religion': 0, 'society': 0, 'spellcraft': 0,
                   'stealth': 0, 'survival': 0}
CondensedBase = {'acrobatics': 'dex', 'athletics': 'str', 'finesse': 'dex', 'influence': 'cha', 'nature': 'int',
                   'perception': 'wis', 'performance': 'cha', 'religion': 'int', 'society': 'int', 'spellcraft': 'int',
                   'stealth': 'dex', 'survival': 'wis'}

# a much more common bonus to the standard skill list, that gives more skillpoints to specifically fill
# out these skills, doesn't change anything about these skills in particular, just separates them out. 
# This is a simple list
BackgroundSkills = ['appraise', 'artistry', 'handle animal', 'linguistics', 'knowledge(engineering)',
                    'knowledge(geography)', 'knowledge(history)', 'knowledge(nobility)', 'lore', 'perform',
                    'profession', 'sleight of hand']

# list for trained/untrained and dict for armor penalty for skills
#TrainedSkills = []
#ArmorPenalty = {}

## The actual class for characters

class Character:
        # Attributes
        misc = {'name': 'Someone', 'player': 'no one'}
        stats = {'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10, 'hp': 10,
                 'maxhp': 10, 'temp': 0, 'speed': 30}
        skills = { 'null': 0}
        skillBase = {'null': 'NULL'}
        classSkill = {'null': False}
        pRace # should be init'd in the init
        cls
        feats # a list of strings, rather than making more instances than neccissary, just use this for searching
        gold # should be a value, 1 = 1gp so .1 = 1sp, and .01 = 1cp
        #equipment slots
        #items all items, active and inactive
        miscFlags = 0
        languages
        
        #constructor
        def __init__(self):
                #Mechanically useless info
                misc['name'] = 'Garbelkox'
                misc['player'] = 'Uranus'
                misc['Deity'] = 'None'
                misc['homeland'] = 'High But'
                misc['gender'] = 'Male'
                misc['age'] = 21
                misc['height'] = '6\'3"'
                misc['weight'] = 420
                misc['hair'] = 'Black'
                misc['eyes'] = 'Black'
                #mechanical core, all come from this font of life, this also is required by a level 0 char
                stats['str'] = 18
                stats['dex'] = 12
                stats['con'] = 14
                stats['int'] = 13
                stats['wis'] = 12
                stats['cha'] = 7
                pRace = Race.Race()
                stats['speed'] = pRace.Speed()
                #Class stuff, here we go, into the fun stuff
                cls = CLS.CLS('fighter') # technically should only give level 1 for init, but we'll deal with that later
                stats['maxhp'] = cls.hd()*cls.level
                feats = ['power attack', 'weapon focus', 'weapon specialization']
                del self.skills['null']
                self.skills = STDSkills
                #for loop to make class skills
                for i in skills:
                        classSkill[i] = False

                for i in cls.skills:
                        classSkill[i] = True
                
        
        #functions (... means to be filled)
                
        def AC(self, flags, misc):
                return 10+self.stats['dex']
        
        #def Attack(self):
        #def Damage(self):
        #def Initiative(self):
        #def Fort(self):
        #def Ref(self):
        #def Will(self):
        #def BAB(self):
        #def CMB(self):
        #def CMD(self):
        #def Speed(self):
        #def SkillCheck(self, skill, mods):
        #def SR(self):
        #def AbilityCheck(self, Ability):



#test code, comment out and ignore for your work

i = Character()

# it throws errors if you ask for something that doesn't exist.
print i.skills
