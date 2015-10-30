# Feat file
# This is a holder for the three classes of Feat, Feature, and Trait, these are separated to make mechanical
# separation more clear. Feats are not Features are not Traits, though Features and Traits may give feats.


# Feats are gained by 3 main means. 1st by level, players get them every odd level they achieve. This is
# cumulative level not class level dependent.  2nd is by feature and trait gifts. These are usually limited
# or specified in some way (fighter bonus feats must be combat feats) and so are simply added to the pile.
# 3rd and the most rare method is by items. Some enchantments give the effect of a feat (Mighty Cleaving is a
# perfect example) and should be included in combat effects. These feats however shouldn't be allowed to meet
# prerequirements for other things. So ignore feats from enchantments when offering new feats.
class Feat(object):
    def __init__(self):
        # The name of the Feat, this can be used for a number of things, but more often than not it will be
        # ignored
        self.Name = ' '
        # Subname is for feats with multiple possible uses, such as Exotic weapon proficiency or weapon focus.
        self.Subname = ' '
        # Flags is a list of feat types that the feat meets, such as combat, metamagic, and so on. This is
        # for both organization, filtering, and bonus feats from other sections.
        self.Flags = [' ']
        # The prerequirement to getting the feat, this can easily be multiple things from class, to feature, to
        # stats
        self.Prereq = [' ']
        # If it's looking for something more specific here's where it will be. As a note, for required features
        # the Prereq will be 'feature' the ReqVal will be 'FeatureName' in many cases it will be a number.
        # Also, in the case for negative requirements (Cannot have X) it will have a -1 in the spot
        self.ReqVal = [0]

        # Bonuses and their application All of these arrays should be of even size, even if there are some blank
        # spots. If a feat replaces something (a la weapon finesse) this will also subtract out the bonus
        # What this Feat alters, can be anything from an attack, to a skill, etc.  This includes penalties.
        # If there are specific alterations based on other systems, include both standard and special lines.
        self.BonusTo = [' ']
        # What is being added to the stat
        self.BonusOf = [0]
        # What it scales off of it it's not 1:1
        self.BonusPer = [1]
        # What it is pulling from statwise
        self.BonusFrom = [' ']

        # A special modifier that pulls in another feature. This is to be None if there is no feature to be called
        # If one is going to be called it needs to be initialized by copying a preexisting one. Try not to make
        # not new features in here, that's just out of this scope. Also, requirements are still being inforced
        # unless specifically stated otherwise.
        self.BonusFeature = None


# Features are abilities and other such stuff that's given by classes as you level up in them, they are often
# static, though some offer multiple choices or choice from a list. With archetyped classes it allows for some
# abilities to be swapped out, but that'll be covered more in CLS than here as this will support it, but most of
# the logic for such stuff will be on the CLS side of things. Some feats can allow for more Features, but these
# Abilities are fairly easy to weed out.
class Feature(object):
    def __init__(self):
        # The name of the feature
        self.Name = ' '
        # Parent Class, There are a few classes that share features, but it's easier to copy them for each class
        # than to make this that flexible from my position
        self.Parent = ' '
        # Level is either the level it is gained, or the level it becomes available.
        self.Level = 0
        
        # This is where the complex stuff starts
        



# Traits are by far the simplest of the three as it has no requirements to speak of, but it also has the ability
# to be swaped out for other racial traits.
class Traits(object):
    
