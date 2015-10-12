#File for the class class

import Feat

# Class class (looking for better name than CLS)

class CLS:
    name = 'herp-derp'
    level = 1
    stats # an array, in order hd, bab, fort, ref, will
    skills = ['null']
    ranks = 0
    proficiency
    features # like character, this is a list of names, these will be searched rather than created.
    text = 'null' # for any overarching text with little to no value mechanically
    Archetype = 'null' # this should be for later and switch out class features for others

    def __init__(self,cname):
        name = cname
        level = 5
        stats = [10, 1,True,False,False]
        skills = ['climb','craft', 'handle animal', 'intimidate', 'knowledge(dungeoneering),
                  'knowledge(engineering)', 'profession', 'ride', 'survival', 'swim']
        ranks = 2
        proficiency = ['simple','martial','light armor', 'medium armor', 'heavy armor', 'shields', 'tower shield']
        text = 'hur-hur'
        features = ['Fighter Bonus Feat', 'bravery', 'armor training', 'weapon training']
