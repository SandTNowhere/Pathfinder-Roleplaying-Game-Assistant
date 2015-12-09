# -*- coding: cp1252 -*-
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
             'linguistics': 0, 'perception': 0, 'ride': 0, 'sense motive': 0, 'sleight of hand': 0,
             'spellcraft': 0, 'stealth': 0, 'survival': 0, 'swim': 0, 'use magic device': 0,
             'knowledge(arcana)': 0, 'knowledge(dungeoneering)': 0, 'knowledge(engineering)': 0,
             'knowledge(geography)': 0, 'knowledge(history)': 0, 'knowledge(local)': 0, 'knowledge(nature)': 0,
             'knowledge(nobility)': 0, 'knowledge(planes)': 0, 'knowledge(religion)': 0}
STDBase = {'acrobatics': 'dex', 'appraise': 'int', 'bluff': 'cha', 'climb': 'str', 'diplomacy':
           'cha', 'disable device': 'dex', 'disguise': 'cha', 'escape artist': 'dex', 'fly': 'dex',
           'handle animal': 'cha', 'heal': 'wis', 'intimidate': 'cha', 'linguistics': 'int',
           'perception': 'wis', 'ride': 'dex', 'sense motive': 'wis', 'sleight of hand': 'dex',
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
                'sleight of hand': 1,'stealth': 1,'swim': 1, 'appraise': 0, 'bluff': 0, 'diplomacy': 0,
                'disguise': 0, 'handle animal': 0, 'heal': 0, 'intimidate': 0,
                'linguistics': 0, 'perception': 0, 'sense motive': 0, 'spellcraft': 0, 'survival': 0,
                'use magic device': 0, 'knowledge(arcana)': 0, 'knowledge(dungeoneering)': 0,
                'knowledge(engineering)': 0, 'knowledge(geography)': 0, 'knowledge(history)': 0,
                'knowledge(local)': 0, 'knowledge(nature)': 0, 'knowledge(nobility)': 0, 'knowledge(planes)': 0,
                'knowledge(religion)': 0}

# This list is an array for Bonus Types. This is going to be useful for many things so I'm putting it here till a
# better location can be had, if there is one. Also, a good format needs to be found for it as this is a placeholder
# format. For more details, http://www.d20pfsrd.com/basics-ability-scores/glossary
# Anything which simply has [' '] can apply to anything.
BonusTypes = {'alchemical': ['ability scores','saves'],'armor': ['AC'],'circumstance': ['attacks','checks'],
              'competence': ['attacks','checks','saves'],'deflection':['AC'],'dodge':['AC'],
              'enhancement':['ability scores','AC','attacks','damage','speed'],'inherent':['ability scores'],
              'insight':['AC','attacks','checks','saves'],'luck':['AC','attacks','checks','damage','saves'],
              'morale':['attacks','checks','damage','saves','str','con','dex'],'natural armor': ['AC'],
              'profane': ['AC','checks','damage','DC','saves'],'racial':[' '],'resistance':['saves'],
              'sacred':['AC','checks','damage','DC','saves'],'shield':['AC'],
              'size':['ability scores','attacks','AC'],'trait':[' '],'untyped':[' ']}

## The actual class for characters

class Character(object):
        # Fun fact, if you want the variable to be instanced purposefully, just do it in __init__()
        
        #constructor
        def __init__(self): # If it is setting data, assume it's not supposed to be in the end, at best it should be initialization
                # Mechanically useless info. This should be self-explanatory for the most part as this really has
                # little if no mechanical effects.
                self.name = ' '
                self.player = ' '
                self.alignment = ' ' # for required alignments mostly, but this is a soft requirement simplified to single string for current purposes.
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
                # any other. Racial bonuses are included, but for all consistency checks that don't include race,
                # it should be subtracted out. It's easier that way.
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
                self.stats['size'] = 'medium'
                # Languages are determined by the race, and most languages are learnable, but there are a
                # few secret languages that have requirements to learn.
                self.Language = []
                
                # Class stuff, here we go, into the fun stuff
                self.cls = [CLS.CLS()]
                # A list of feats that are initialized here and properly set during character creation.
                # All feats gained, either through class or level, there can only be as many feats as given through
                # level, all feats that are named in other parts (features, traits, etc.) are ignored in the total
                # count. ex, someone takes the fighter bonus feat to get alertness, alertness' bonuses will be here
                # it's name is recorded under that fighter feature called bonus feat, and so it's ignored when
                # checked for feats. Any feat that has no source, will throw an problem
                self.Feats = []
                # Creates the list of skills and ranks
                self.skills = STDSkills
                # Creates a list of class skills that again, will be filled properly with character creation.
                self.classSkill = {'null': 'null'}

                # set max skill ranks of the player
                self.ranks = 0

                # Again, initialized to default value, and should be set during proper creation
                self.GP = 0
                # Cumulative value, should techinally be aggrigated, but is easier to calculate GP=Cumulative-Items
                # than the other way around, and it gives the GM more fine control over his player's total wealth.
                # and makes it easier to tell when someone is creating wealth.
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

        # The total ranks of the character, this is also an update for the character
        def TotalRanks(self):
                ret = 0
                for i in self.cls:
                       ret += (i.ranks+self.AbilityCheck('int'))*i.level

                self.ranks = ret
                return ret

        def ArmorAC(self):
                if self.Armor[0]:
                        return self.Armor[0].AC()
                else:
                        return 0

        def ShieldAC(self):
                if self.Armor[1]:
                        return self.Armor[1].AC()
                else:
                        return 0

        # AC is based off of bonuses and is a bit hard to define easily, but it requires a few searches.
        def AC(self):
                ret = 10
                MaxDexArmor = -1
                MaxDexShield = -1
                # Add armor bonus [Armor[0]]
                if self.Armor[0]:
                        ret += self.Armor[0].AC()
                        MaxDexArmor = self.Armor[0].MaxDex
                # Add Shiled Bonus [Armor[1]]
                if self.Armor[1]:
                        ret += self.Armor[1].AC()
                        MaxDexShield = self.Armor[1].MaxDex
                # add dex capped by the armor
                temp = self.AbilityCheck('dex')
                if MaxDexArmor != -1 and temp > MaxDexArmor:
                        temp = MaxDexArmor
                if MaxDexShield != -1 and temp > MaxDexShield:
                        temp = MaxDexShield
                ret += temp
                # add class feature bonuses
                # add feat bonuses.
                return ret

        # Touch AC is a variant Armor class that is based off of your ability to dodge exclusively.
        def Touch(self):
                ret = self.AC()
                # remove armor bonus
                # remove Shield bonus
                # remove natural armor
                return ret

        # Flatfooted AC is another variant, however this is based off of the hardness of your armor, as you are
        # unable to dodge.
        def Flatfooted(self):
                ret = 10
                # remove dexerity
                # remove 
                return ret

        # The attack roll to hit, this doesn't include damage this is only checking for the hit.
        def Attack(self, Weapon = None):
                ret = self.BAB()
                # Check if With Weapon
                if Weapon != None:
                        # Get info from weapon including it's bonuses
                        temp = Weapon.Attack()
                        # check weapon for type and decide str or dex as the to hit stat (melee is strength and range is dex by
                        if Weapon.Handedness == 'ranged':
                                temp = temp + self.AbilityCheck('dex')
                        else:
                                # default don't check for weapon finesse, weapon finesse's bonus is calculated to remove str while
                                # adding dex. Weapons that add dex by default are not finessible
                                temp = temp + self.AbilityCheck('str')
                        
                        ret = ret + temp
                # add feat bonuses, most of these are dependent on weapons but some aren't
                # Put any penalties onto it
                return ret

        # The damage of the attack, this is based off of the weapon and damage, and has nothing to do with actually
        # hitting. This is pure damage. It should return of what should be rolled by the
        # player as a string (and/or numbers parsed for use in a string.
        def Damage(self, Weapon = None):
                # Get base damage
                if Weapon != None: # Weapon
                        ret = "%dd%d"%((Weapon.Damage[0]), Weapon.Damage[1])
                else: # Unarmed
                        # Based on creature size and bonuses
                        # Check for bonuses
                        if self.stats['size'] == 'medium':
                                ret  = "1d3"
                        if self.stats['size'] == 'small':
                                ret = "1d2"
                # Add damage bonuses Melee, ranged is dependent on other stuff and doesn't add bonuses naturally
                # one handed only adds STR, two-handed Adds 1.5 STR (rounded down)
                if Weapon == None:
                        ret = ret + "+%d"%(self.AbilityCheck('str'))
                elif Weapon.Handedness == 'ranged':
                        ret = ret
                elif Weapon.Handedness == 'two-handed':
                        ret = ret + "+%d"%(math.floor(1.5*self.AbilityCheck('str')))
                else: # light and one-handed
                        ret = ret + "+%d"%(self.AbilityCheck('str'))

                return ret
                                
                        
        
        def Initiative(self):
                ret = self.AbilityCheck('dex')
                # search through bonuses
                return ret
        
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
                for i in self.cls:
                        ret = ret + i.Save(save)

                return ret
        
        def BAB(self):
                ret = 0
                for i in self.cls:
                        ret = ret + i.BAB()
                return ret
                
        def CMB(self):
                ret = self.BAB() + self.AbilityCheck('str') #+ self.SizeMod()
                return ret
        
        def CMD(self):
                ret = 10 + self.BAB() + self.AbilityCheck('str') + self.AbilityCheck('dex') #+ self.SizeMod()
                return ret
        
        def Speed(self):
                # insert check for speed increases options and adding them together along with any penalties
                # don't forget to include other potential movement methods.
                return self.stats['speed']
        
        def SkillCheck(self, skill):
                ret = self.skills[skill]
                ret = ret + self.AbilityCheck(STDBase[skill])
                if skill in self.classSkill:
                        ret += 3
                # Penalties applied
                Penalty = 0
                if self.Armor[0]:
                        Penalty = self.Armor[0].ArmorPenalty
                if self.Armor[1]:
                        Penalty = self.Armor[1].ArmorPenalty
                ret += ArmorPenalty[skill]*Penalty
                return ret

        def SkillRanks(self, skill):
                return self.skills[skill]
                
        def SR(self):
                TSR = 0
                return TSR

        # Returns the requested ability check.
        def AbilityCheck(self, Ability):
                return math.floor((self.stats[Ability]-10)/2)

        # Returns a list of names for features that give bonuses to the situation so they can be called b
        #def BonusSearch(self, To, BType):
        #        ret = []
        #        ret.extend(self.Race.Bonus(To,BType))
        #        # Cycle through feats
        #        if self.Feats:
        #                for x in self.Feats:
        #                        if To == self.Feats[x].BonusTo() and BType == self.Feats[x].BonusType():
        #                                ret.append(self.Feats[x].Bonus())
        #        
        #        # Cycle through class and their features (and the feats they give *cough*)
        #        # While players must have a class, mosters may not, so checking is still required.
        #        if self.cls:
        #                for x in self.cls: # Extend rather than append as BonusSearch will return a list
        #                        ret.extend(self.cls.BonusSearch(To, BType))
        #       
        #        # Cycle through armor, and equipment. Weapons are split off as their immediate flexibility make
        #        # them harder to control and their bonuses may be applied improperly using this function.
        #        for x in self.Armor: # Since armor always have the slots, even if they aren't filled.
        #                if self.Armor[x]: # Since armor can give multiple bonuses to different things.
        #                        ret.append(self.Armor[x].Bonus(To, BType))
        #
        #        for x in self.Slots:
        #                if self.Slots[x]:
        #                        ret.append(self.Slots[x].Bonus(To, BType))
        #
        #        # And last, slotless items
        #        if self.Slotless:
        #                for x in self.Slotless:
        #                        ret.append(self.Slotless[x].Bonus(To, BType))
        #        return ret

        def MaxLoad(self,STR):
                if STR in range(0, 11):
                        return 10 * STR
                elif self.stats['str'] > 14:
                        return 2 * self.MaxLoad(STR - 5)
                else:
                        return [115, 130, 150, 175][STR - 11]

        def UpdateMaxHP(self):
                temp = 0
                for i in self.cls:
                        temp = i.level * (i.hd + self.AbilityCheck('con'))
                
                self.stats['maxhp'] = temp

        def FullRecover(self):
                self.stats['hp'] = self.stats['maxhp']

        # This is test code and should not be seen as part of the end product to be shown. It's rough and simply for
        # command Python IDLE testing of Character.py
        def printCharacter(self):
                print ("Character Name:" + self.name + " \t Player Name:" + self.player)
                print ("Alignment: " + self.alignment[0] + ' ' + self.alignment[1] + " \t Deity:" + self.deity + " \t Homeland:" + self.homeland)
                print ("Gender:" + self.gender + " \t Age:%d \t Height:"%(self.age) + self.height + "\t Weight:%d"%(self.weight))
                print ("Hair:" + self.hair + "\t Eyes:" + self.eyes + " \t Race:" + self.pRace.GetName())
                print ("STR: %d DEX: %d CON: %d INT: %d WIS: %d CHA: %d"%(self.stats['str'],self.stats['dex'],self.stats['con'],self.stats['int'],self.stats['wis'],self.stats['cha']))
                print ("---------------------------------------------------------------------------")
                print ("Max Hit Points:%d \t Current Hit Points:%d"%(self.stats['maxhp'],self.stats['hp']))
                print ("Speed: %d \t Initiative: %d"%(self.Speed(), self.Initiative()))
                print ("Fortitude: %d \t Reflex: %d \t Will: %d"%(self.Save('fort'),self.Save('ref'),self.Save('will')))
                print ("BAB: %d \t CMB: %d \t CMD: %d \t Spell Resistance: %d"%(self.BAB(), self.CMB(), self.CMD(), self.SR()))
                print ("Armor Class: %d \t Touch: %d \t FlatFooted: %d"%(self.AC(),self.Touch(),self.Flatfooted()))
                print ("---------------------------------------------------------------------------")
                print ("Ranks: %d"%(self.TotalRanks()))
                print ("Skill: Ability Bonus + Ranks - Penalty = Total")
                CheckPenalty = 0
                if self.Armor[0]:
                        CheckPenalty += self.Armor[0].ArmorPenalty
                if self.Armor[1]:
                        CheckPenalty += self.Armor[1].ArmorPenalty
                for i in sorted(self.skills.keys()):
                        print ("%s: %d + %d - %d = %d"%(i, self.AbilityCheck(STDBase[i]), self.SkillRanks(i), ArmorPenalty[i]*(CheckPenalty), self.SkillCheck(i)))
                print ("Max Carrying Capacity:%d"%(self.MaxLoad(self.stats['str'])))
                print ("---------------------------------------------------------------------------")
                print ("Classes:")
                for i in self.cls:
                        print ("%s  %d"%(i.name,i.level))
                print ("Weapon Attacks:")
                print ("\t Unarmed Strike +%d: %s"%(self.Attack(), self.Damage()))
                if self.Weapons:
                        for i in self.Weapons:
                                print ("\t %s +%d: %s"%(i.Name, self.Attack(i), self.Damage(i)))

        # A check to see if anything is out of the ordinary, or outside of the rules, responds not with a message
        # that points out all errors in the sheet. This is both parts that break the rules, or any part that
        # shouldn't be empty that is (such as empty feat slots that shouldn't be empty).
        def ConsistencyCheck(self):
                pass
                        


        # DING is a special context to allow for easy alteration and addition of new features from level to level.
        # It is split into steps.
        # 1st is Ability score buffs that are gained this level.
        # 2nd is the class level your taking and all of it's bonuses and buffs. This is features, feats, both given
        # by the class and by the overall level of the player.
        # 3rd is allocation of all gained skillpoints.
        # The reason for this order is that if people put in skillpoints before leveling their class they may
        # gain early access to a prestige feat, or an ability with higher requirements.
        # currently this is defunct as this is going to need some special handling by the GUI people to make it.
        def DING(self):
                pass
                                


#test code, comment out and ignore for your work at higher levels.
ClassEx = CLS.CLS()
ClassEx.name = 'Fighter'
ClassEx.level = 1
ClassEx.hd = 10
ClassEx.bab = 1
ClassEx.stats['fort'] = True
ClassEx.skills = ['climb','craft','handle animal','intimidate','knowledge(dungeoneering)',
                  'knowledge(engineering)','profession','ride','survival','swim']
ClassEx.proficiency = ['simple','martial','armor(light)','armor(medium)','armor(heavy)','shields','tower shield']
ClassEx.text = """Some take up arms for glory, wealth, or revenge. Others do battle to prove themselves, to protect others, or because they know nothing else. Still others learn the ways of weaponcraft to hone their bodies in battle and prove their mettle in the forge of war. Lords of the battlefield, fighters are a disparate lot, training with many weapons or just one, perfecting the uses of armor, learning the fighting techniques of exotic masters, and studying the art of combat, all to shape themselves into living weapons. Far more than mere thugs, these skilled warriors reveal the true deadliness of their weapons, turning hunks of metal into arms capable of taming kingdoms, slaughtering monsters, and rousing the hearts of armies. Soldiers, knights, hunters, and artists of war, fighters are unparalleled champions, and woe to those who dare stand against them.
Role: Fighters excel at combat—defeating their enemies, controlling the flow of battle, and surviving such sorties themselves. While their specific weapons and methods grant them a wide variety of tactics, few can match fighters for sheer battle prowess."""
ClassEx.StartingGP = '5d6x10 gp'

FBF = Feat.Feature()
FBF.Name = 'Fighter Bonus Feat'
FBF.Parent = 'Fighter'
FBF.Level = 1
FBF.BonusFeat = ['Weapon Focus','Shortsword']
FBF.FeatLimits = ['combat']
FBF.Text = """
At 1st level, and at every even level thereafter, a fighter gains a bonus feat in addition to those gained from normal advancement (meaning that the fighter gains a feat at every level). These bonus feats must be selected from those listed as Combat Feats, sometimes also called “fighter bonus feats.”

Upon reaching 4th level, and every four levels thereafter (8th, 12th, and so on), a fighter can choose to learn a new bonus feat in place of a bonus feat he has already learned. In effect, the fighter loses the bonus feat in exchange for the new one. The old feat cannot be one that was used as a prerequisite for another feat, prestige class, or other ability. A fighter can only change one feat at any given level and must choose whether or not to swap the feat at the time he gains a new bonus feat for the level.
"""

ClassEx.features = [FBF]

REX = Race.Race()
REX.Name = 'Human'
REX.RaceType = 'Humanoid'
REX.SubType = 'Human'
REX.StartingLanguages = ['common']
REX.Traits = [Feat.Trait(), Feat.Trait(), Feat.Trait()]
REX.Notes = 'Human'

#test Weapon standard case, nothing special
SWEP = Item.Weapon()
SWEP.Title = ' '
SWEP.Name = 'Club'
SWEP.Catagory = 'Simple'
SWEP.Handedness = 'One-Handed'
SWEP.Cost = 0
SWEP.Damage[0] = 1
SWEP.Damage[1] = 6
SWEP.Size = 'Medium'
SWEP.Critical = [20,2]
SWEP.Range = 10
SWEP.Weight = 3
SWEP.Type = ['B']
SWEP.Special = []
SWEP.Source = 'PRG:CRB'
SWEP.Text = 'This weapon is usually just a shaped piece of wood, sometimes with a few nails or studs embedded in it.'
SWEP.Enchantments = None

SARM = Item.Armor()
SARM.Name = 'Fullplate'
SARM.IsArmor = True
SARM.Price = 1500
SARM.ACBonus = 9
SARM.MaxDex = 1
SARM.ArmorPenalty = -6
SARM.SpellFailure = 35
SARM.Speed = [20,15]
SARM.Weight = 50
SARM.text = 'This metal suit includes gauntlets, heavy leather boots, a visored helmet, and a thick layer of padding that is worn underneath the armor. Each suit of full plate must be individually fitted to its owner by a master armorsmith, although a captured suit can be resized to fit a new owner at a cost of 200 to 800 (2d4 × 100) gold pieces.'
SARM.Source = 'PRG:CRB'

Test = Character()
Test.cls[0] = ClassEx
Test.stats['str'] = 15
Test.stats['dex'] = 18
Test.stats['int'] = 14
Test.stats['con'] = 16
Test.Weapons = [SWEP]
Test.UpdateMaxHP()
Test.FullRecover()
Test.Armor[0] = SARM

# it throws errors if you ask for something that doesn't exist.
#Test.printCharacter()
