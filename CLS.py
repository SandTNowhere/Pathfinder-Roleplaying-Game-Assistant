#File for the class class

import Feat

# Class class (looking for better name than CLS)

class CLS(object):
    name = 'herp-derp'
    level = 1
    stats = {'hd': 0, 'bab': 1,'fort': False,'ref': False,'will': False, 'ranks': 0}
    skills = ['null']
    proficiency = [0]
    features = [0] # like character, this is a list of names, these will be searched rather than created.
    text = 'null' # for any overarching text with little to no value mechanically
    Archetype = 'null' # this should be for later and switch out class features for others

    def __init__(self,cname):
        self.name = cname
        self.level = 5
        self.stats['hd'] = 10
        self.stats['bab'] = 1
        self.stats['fort'] = True
        self.stats['ref'] = False
        self.stats['will'] = False
        self.skills = ['climb','craft', 'handle animal', 'intimidate', 'knowledge(dungeoneering)',
                  'knowledge(engineering)', 'profession', 'ride', 'survival', 'swim']
        self.ranks = 2
        self.proficiency = ['simple','martial','light armor', 'medium armor', 'heavy armor', 'shields', 'tower shield']
        self.text = 'hur-hur'
        self.features = ['Fighter Bonus Feat', 'bravery', 'armor training', 'weapon training']

    def hd(self):
        return self.stats['hd']
