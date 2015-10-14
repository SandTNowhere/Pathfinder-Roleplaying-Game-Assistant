# Python File for Pathfinder Character Assistant

# includes
import Race
import CLS
import Feat
import Item
import math


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
           'spellcraft': 'int', 'stealth': 'dex', 'survival': 'wis', 'swim': 'str',
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

class Character(object):
        # Attributes
        # Fun fact, if you want the variable to be instanced purposefully, just do it in __init__()
        feats = 0# a list of strings, rather than making more instances than neccissary, just use this for searching
        cumulativeGold = 0 # the total value of everything owned by the player
        gold = 0# should be a value, 1 = 1gp so .1 = 1sp, and .01 = 1cp
        #equipment slots
        #items all items, active and inactive
        languages = 0
        
        #constructor
        def __init__(self):
                #Mechanically useless info
                self.name = 'Bumquist Garbelkox'
                self.player = 'Uranus'
                self.alignment = ['chaotic', 'evil'] # for required alignments mostly
                self.deity = 'None'
                self.homeland = 'High But'
                self.gender = 'Male'
                self.age = 69
                self.height = '6\'9"'
                self.weight = 420
                self.hair = 'Black'
                self.eyes = 'Black'
                
                #mechanical core, all come from this font of life, this also is required by a level 0 char
                self.stats = {'str': 10}
                self.stats['str'] = 18
                self.stats['dex'] = 12
                self.stats['con'] = 14
                self.stats['int'] = 13
                self.stats['wis'] = 12
                self.stats['cha'] = 7
                self.stats['temp'] = 0
                self.pRace = Race.Race('human')
                self.stats['speed'] = self.pRace.Speed()
                
                #Class stuff, here we go, into the fun stuff
                self.cls = CLS.CLS('fighter') # technically should only give level 1 for init, but we'll deal with that later
                self.stats['maxhp'] = self.cls.HD()*self.cls.level
                self.stats['hp'] = self.stats['maxhp']
                self.feats = ['power attack', 'weapon focus', 'skill focus(climb)']
                self.skills = STDSkills
                self.classSkill = {'null': 'null'}
                
                #for loop to make class skills
                for i in self.skills:
                        self.classSkill[i] = False

                for i in self.cls.skills:
                        self.classSkill[i] = True

                del self.classSkill['null']
                
                # set skill ranks, need to allow for multiple classes
                self.ranks = (self.cls.Ranks() + self.AbilityCheck('int'))*self.cls.level
                # check for skilled bonus feat
                if 'skilled' in self.pRace.Traits():
                        self.ranks = self.ranks + 1*self.cls.level# should aggrigate level here

                # put ranks into skills, should never go higher than the ranks allowed, and no more ranks than level
                self.skills['climb'] = 5
                self.skills['handle animal'] = 5
                self.skills['ride'] = 5
                self.skills['intimidate'] = 5
                        
                
        
        #functions (... means to be filled)
                
        def AC(self, flags, misc):
                return 10+self.stats['dex']
        
        #def Touch(self):
        #def Flatfooted(self):
        #def Attack(self):
        #def Damage(self):
        
        def Initiative(self):
                return self.AbilityCheck('dex')
        
        def Save(self,save):
                stat = 'null'
                if save == 'fort':
                        stat = 'con'
                elif save == 'ref':
                        stat = 'dex'
                elif save == 'will':
                        stat = 'wis'
                else: #catch
                        return False

                ret = self.AbilityCheck(stat)
                #for i in self.cls:
                ret = ret + self.cls.Save(save)

                return ret
        
        def BAB(self):
                ret = 0
                #for i in self.cls
                ret = self.cls.BAB()
                return ret
                
        def CMB(self):
                ret = self.BAB() + self.AbilityCheck('str') #+ self.SizeMod()
                return ret
        
        def CMD(self):
                ret = self.BAB() + self.AbilityCheck('str') + self.AbilityCheck('dex') #+ self.SizeMod()
                return ret
        
        def Speed(self):
                # insert check for speed increases options and adding them together along with any penalties
                # don't forget to include other potential movement methods.
                return self.stats['speed']
        
        def SkillCheck(self, skill):
                ret = self.skills[skill]
                ret = ret + self.AbilityCheck(STDBase[skill])
                if self.classSkill[skill] and (self.skills[skill] > 0):
                        ret = ret + 3
                return ret
                
        #def SR(self):
		
        def AbilityCheck(self, Ability):
                return math.floor((self.stats[Ability]-10)/2)
		

        def printCharacter(self):
                print "Character Name:" + self.name + " \t Player Name:" + self.player
                print "Alignment: " + self.alignment[0] + ' ' + self.alignment[1] + " \t Deity:" + self.deity + " \t Homeland:" + self.homeland
                print "Gender:" + self.gender + " \t Age:%d \t Height:"%(self.age) + self.height + "\t Weight:%d"%(self.weight)
                print "Hair:" + self.hair + "\t Eyes:" + self.eyes + " \t Race:" + self.pRace.Name()
                print "---------------------------------------------------------------------------"
                print "Max Hit Points:%d \t Current Hit Points:%d"%(self.stats['maxhp'],self.stats['hp'])
                print "Speed: %d \t Initiative: %d"%(self.Speed(), self.Initiative())
                print "Fortitude: %d \t Reflex: %d \t Will: %d"%(self.Save('fort'),self.Save('ref'),self.Save('will'))
                print "BAB: %d \t CMB: %d \t CMD: %d"%(self.BAB(), self.CMB(), self.CMD())
                for i in self.skills:
                        print "%s: %d"%(i,self.SkillCheck(i))
				
	#def update(self):
	#	Update all data upon any alteration.


#test code, comment out and ignore for your work

i = Character()

# it throws errors if you ask for something that doesn't exist.
i.printCharacter()
