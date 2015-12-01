#File for the class class

import Feat
import Spells
import math

# Class class (looking for better name than CLS)

class CLS(object):
    def __init__(self):
        # The name of the class
        self.name = ' '
        # The prerequirements of the class, base classes simply have the default value as there are no
        # requirements, as an addition, everything split by key is an and, everything split in a key is an or.
        # Ex. {'alignment': [ ['lawful',' '] , ['neutral',' '] ]} requires either lawful or neutral, but nothing
        # chaotic in alignment.
        self.reqs = {'level': -1}
        # The levels in the class, this is more for PC's than the class itself.
        self.level = 0
        # The Hit Die size of the class, there this is either 6,8,10, or 12
        self.hd = 6
        # The BAB rate of the class, based off of level. The only three options are 1/2, 3/4, and 1
        self.bab = 1/2
        # The Saves of the class, there are only two progressions good and bad (True and False)
        self.stats = {'fort': False, 'ref': False, 'will': False}
        # This is the skill list for the class.
        self.skills = [' ']
        # The ranks per level that the class gets, again only come in a few level 2,4,6, and 8 all get
        # the intelligence mod to them. It is retroactive so the total number of ranks should be equal to
        # (ranks+int mod)*level
        self.ranks = 2
        # The proficiencies the class gets. Foremost should be the groups of weapons, and at the end should be
        # specific weapons and other such stuff. This can include some Exotic weapons, but will never contain more
        # Exotic weapons as a group.
        self.proficiency = [' ']
        # The non-mechanical text of the class at large, can include the text of archetypes also.
        self.text = ' '
        # Features is a list of features that the class has. In static classes that are for reference, it is all
        # Possible features, if it is being used by a player it is limited to only what they have chosen.
        self.features = None
        # Archetype is a list of Applied archetypes that have been applied. The archetypes should only be added
        # one at a time so that any overlap can be caught immediately. If empty then there are no archetypes
        # active.
        self.Archetype = [' ']
        # Starting Wealth is the wealth the player should have a level 1, this is a bit random, but it only really
        # matters at level 1. This should be a rolled wealth, that gives
        self.StartingGP = ' '

    def HD(self):
        return self.hd

    def Save(self,save):
        if self.stats[save]:
            return 2+math.floor(self.level/2)
        else:
            return math.floor(self.level/3)

    def BAB(self):
        return math.floor(self.level*self.bab)

    def Ranks(self):
        return self.ranks

    def ClassSkills(self):
        return self.Skills

    def IsClassSkills(self, skill):
        if skill in self.skills:
            return True

        return False
