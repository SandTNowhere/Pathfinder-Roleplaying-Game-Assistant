# Python File for Pathfinder Character Assistant

# includes
import Race
import CLS
import Feat
import Item
import math
import Spells


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
TrainedSkills = ['disable device', 'handle animal', 'knowledge(arcana)', 'knowledge(dungeoneering)',
                 'knowledge(engineering)','knowledge(geography)','knowledge(history)','knowledge(local)',
                 'knowledge(nature)','knowledge(nobility)','knowledge(planes)','knowledge(religion)','linguistics',
                 'proffession','sleight of hand','spellcraft','use magic device']
ArmorPenalty = {'acrobatics': 1,'climb': 1,'disable device': 1, 'escape artist': 1, 'fly': 1, 'ride': 1,
                'sleight of hand': 1,'stealth': 1,'swim': 1}

## The actual class for characters

class Character(object):
        # Fun fact, if you want the variable to be instanced purposefully, just do it in __init__()
        
        #constructor
        def __init__(self): # If it is setting data, assume it's not supposed to be in the end, at best it should be initialization
                # Mechanically useless info. This should be self-explanatory for the most part as this really has
                # little if no mechanical effects.
                self.name = ' '
                self.player = ''
                self.alignment = ['Neutral', 'Neutral'] # for required alignments mostly, but this is a soft requirement
                self.deity = ' '
                self.homeland = ' '
                self.gender = ' '
                self.age = 0
                self.height = ' '
                self.weight = 0
                self.hair = ' '
                self.eyes = ' '
                self.notes = ' '# This is not entirely a catch all, but meant for non-mechanical information.
                
                # mechanical core, all come from this font of life, this also is required by a level 0 char
                # These are the big six, the central most mechanical stats, that are called by more abilities than
                # any other.
                self.stats = {'str': 10,'dex': 10,'con': 10,'int': 10,'wis': 10,'cha': 10}
                # The maximum HP allowed for the character, calculated based off of class HD+Con*Level, this is a
                # stand in till classes are chosen
                self.stats['maxhp'] = 4
                # Another initialization to be made complete in proper creation.
                self.stats['hp'] = 4
                # Temp is a for Temporary HP. 
                self.stats['temp'] = 0
                # This calls up a blank race that has no stats or bonuses
                self.pRace = Race.Race()
                # This sets the basic speed of the character
                self.stats['speed'] = 30
                # This sets the size of the charater, it will also change with the race potentially.
                self.stats['size'] = 'med'
                # Languages are determined by the race, and most languages are learnable, but there are a
                # few secret languages that have requirements to learn.
                self.Language = []
                
                # Class stuff, here we go, into the fun stuff
                self.cls = []
                # A list of feats that are initialized here and properly set during character creation.
                self.Feats = []
                # Creates the list of skills and their dependents that are
                self.skills = STDSkills
                # Creates a list of class skills that again, will be filled properly with character creation.
                self.classSkill = {'null': 'null'}

                # set skill ranks, need to allow for multiple classes
                self.ranks = 0

                # Again, initialized to default value, and should be set during proper creation
                self.GP = 0
                # Cumulative value, should techinally be aggrigated, but is easier to calculate GP = Cum-Items
                # than the other way around, and it gives the GM more fine control over his player's total wealth.
                self.CumulativeGP = 0

                # Equipment slots, Floated off from the main list are weapons and armor as they are unique enough
                # to warrant being separate, also since weapons can often be easily swapped between, weapons are
                # a list unto themselves.
                self.Weapons = []
                # Armor is much more static, but still very different from other items, hence it's place here.
                # There are two pieces of armor, the actual armor, and shields. Shields are not as bad, but
                # Are still rather unique among item types.
                self.Armor = [None, None]
                # the proper equipment slots in order: Belts, Body, Chest, Eyes, Feet, Hands, Head,
                # Headband, Neck, Shield, Shoulders, Wrists, Ring1, and Ring2
                self.Slots = [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
                # Lastly, the slotless equipment section, this is meant to be flexible as there are no limits on
                # Slotless magic items
                self.Slotless = []
                
                # The last part is inventory, this is miscellaneous items that have few if any immediate effects
                # for characters in combat. These items are also much more generic and standardized.
                self.Inventory = []

        # AC is based off of bonuses and is a bit hard to define easily, but it requires a few searches.
        def AC(self, flags, misc):
                ret = 10
                return ret
        
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
                #insert additional bonuses
                return ret
                
        def SR(self):
                TSR = self.pRace.SR()
                # insert check for SR and choose highest, it doesn't stack
                return TSR

	# Returns the requested ability check.
        def AbilityCheck(self, Ability):
                return math.floor((self.stats[Ability]-10)/2)

        # Returns a list of names for features that give bonuses to the situation so they can be called b
        def BonusSearch(self, To, BType):
                ret = []
                ret.extend(self.Race.Bonus(To,BType))
                # Cycle through feats
                if self.Feats:
                        for x in self.Feats:
                                if To == self.Feats[x].BonusTo() and BType == self.Feats[x].BonusType():
                                        ret.append(self.Feats[x].Bonus())
                
                # Cycle through class and their features (and the feats they give *cough*)
                # While players must have a class, mosters may not, so checking is still required.
                if self.cls:
                        for x in self.cls: # Extend rather than append as BonusSearch will return a list
                                ret.extend(self.cls.BonusSearch(To, BType))
                
                # Cycle through armor, and equipment. Weapons are split off as their immediate flexibility make
                # them harder to control and their bonuses may be applied improperly using this function.
                for x in self.Armor: # Since armor always have the slots, even if they aren't filled.
                        if self.Armor[x]: # Since armor can give multiple bonuses to different things.
                                ret.append(self.Armor[x].Bonus(To, BType))

                for x in self.Slots:
                        if self.Slots[x]:
                                ret.append(self.Slots[x].Bonus(To, BType))

                # And last, slotless items
                if self.Slotless:
                        for x in self.Slotless:
                                ret.append(self.Slotless[x].Bonus(To, BType))
                return ret

        def MaxLoad(self):
                if self.stats['str'] in range(0, 11):
                        return 10 * self.stats['str']
                elif self.stats > 14:
                        return 2 * max_load(self.stats['str'] - 5)
                else:
                        return [115, 130, 150, 175][self.stats['stats'] - 11]
		

        def printCharacter(self):
                print "Character Name:" + self.name + " \t Player Name:" + self.player
                print "Alignment: " + self.alignment[0] + ' ' + self.alignment[1] + " \t Deity:" + self.deity + " \t Homeland:" + self.homeland
                print "Gender:" + self.gender + " \t Age:%d \t Height:"%(self.age) + self.height + "\t Weight:%d"%(self.weight)
                print "Hair:" + self.hair + "\t Eyes:" + self.eyes + " \t Race:" + self.pRace.GetName()
                print "---------------------------------------------------------------------------"
                print "Max Hit Points:%d \t Current Hit Points:%d"%(self.stats['maxhp'],self.stats['hp'])
                print "Speed: %d \t Initiative: %d"%(self.Speed(), self.Initiative())
                print "Fortitude: %d \t Reflex: %d \t Will: %d"%(self.Save('fort'),self.Save('ref'),self.Save('will'))
                print "BAB: %d \t CMB: %d \t CMD: %d"%(self.BAB(), self.CMB(), self.CMD())
                print "Ranks: %d"%(self.ranks)
                for i in self.skills:
                        print "%s: %d"%(i,self.SkillCheck(i))
				
	#def update(self):
	#	Update all data upon any alteration.


#test code, comment out and ignore for your work
i = Character()
ClassEx = CLS.cls()

FeatEx = Feat.Feat()

# it throws errors if you ask for something that doesn't exist.
i.printCharacter()
