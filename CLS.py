#File for the class class

import Feat
import Spells
import math

# Class class (looking for better name than CLS)

class CLS(object):
    def __init__(self,cname):
        #insert search/call to collect all class info from storage
        self.name = cname
        self.reqs = {'level': -1}
        self.level = 5
        self.hd = 10
        self.bab = 1
        self.stats = {'fort': True}
        self.stats['ref'] = False
        self.stats['will'] = False
        self.skills = ['climb','craft', 'handle animal', 'intimidate', 'knowledge(dungeoneering)',
                  'knowledge(engineering)', 'profession', 'ride', 'survival', 'swim']
        self.ranks = 2
        self.proficiency = ['simple','martial','light armor', 'medium armor', 'heavy armor', 'shields', 'tower shield']
        self.text = 'hur-hur'
        self.features = ['Fighter Bonus Feat', 'bravery', 'armor training', 'weapon training']
        self.Archetype = ['null']
        self.text = 'null'

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
