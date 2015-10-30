# Spells and a rough layout of this I'll try to comment as much as possible
# For more detail on what I've said here, go to this address. http://paizo.com/pathfinderRPG/prd/magic.html


#If a spell does not have one of these parts, leave it at it's default value to mark it as unused.
class Spell(object):
    def __init__(self):
        self.Name = ' ' #name, no mechanical effects
        # school, good god the effects, this defines what school it is defined as for feats and features that deal
        # with schools of spells, there are only 7 to speak of, Enchantment, Evocation, Illusion, Transmutation,
        # Necromancy, Conjuration, Divination, and Abjuration
        self.School = ' '
        # Subschool, related so school. Often the spell will have a subschool that gives more specific details
        # But the subschool is divided by school and the direct effects are much less
        self.Subschool = ' '
        # Domain is an alternative set of rules to the school/subschool and is meant for divine casters. It has a
        # few effects on the spell, but for the most part it's just for organization as divine casters don't go by
        # school. It is split into domain name and level in the domain, just like the self.Level is.
        self.Domain = {'Name': 0}
        # Subdomain is like subschool is to school, however, rather than simply being a specification, it's an
        # alternative much like archetypes are for classes, it replaces the spells from it's parent domain, to make
        # it into a subdomain. Domain and subdomain could be folded together, but for now they are separate for
        # better comparative organization.
        self.Subdomain = {'name': 0}
        # Descriptor is one of a number of flags that are important for other things, Some metamagics alter these
        # but for the most part these are simply for the user to make note of and have ready should circumstances
        # come up. The second part in () can usually be ignored for our needs.
        self.Descriptor = '[Descriptor](more detail)'
        # This is divided by class as many spells are shared by multiple classes, but may have different levels for
        # different classes. This is the spell level, not the caster's level.
        self.Level = {'caster': 0}
        # The time it takes to cast the spell, often it's a standard action, but it can by almost anything, mildly
        # important for a few things such as metamagics (Quicken specifically but that's details)
        self.Time = ' '
        # There are 5 separate components that can exist in a spell: verbal 'v', somatic 's', material 'm',
        # focus 'f', and divine focus 'df', these also have effects with feats and also are important to other
        # things. There is a note that some classes can change these (see psychic magic for details). If there is
        # a material focus it will say at the in in the hypothetical 6th slot.
        self.Components = [' ']
        # This is how far you can be from your target, sometimes this is a dynamic function, but we can have it look
        # for the flags of Close, Medium, and Long, everything else is as is.
        self.Range = ' ' 
        # Target is who or what can be effected by the spell, often it will be something nebulous, but it should be
        # a non-issue for our program.
        self.Target = ' '
        # Duration is how long it lasts, again this has a few predefined examples, and we can make catches for them
        # and otherwise use functions, also some metamagic effects here.
        self.Duration = ' '
        # This is an expansion onto duration which gives any extranious details tha may be important for the caster
        # but don't truly alter the spell's max duration.
        self.DurationDetail = ' '
        # Saving throw has two parts and up to a number of saves, for simple multiple saves such as Phantasmal
        # Killer which requires both a will and a fort save to have its effects, modifiers will be given on the part
        # returned by the dictionary. Examples include {'will': 'to disbelieve'} and {'will': 'negates(harmless)'}
        self.Duration = {' ': ' '}
        # Spell resistance is a simple yes or no, and marks it as having to break spell resistance if it exists on
        # the affected party
        self.SR = False
        # Description is mechanically useless to our program, but it holds all the details to make the spells work
        self.Desc = " "

        # Bonus is designed in a similar fashion to feats and enchantments, but these only last for a specific
        # Duration and must be in the active position to give their effect.

        # What it goes to be it skill or stat or attacks
        self.BonusTo = [' ']
        # The amount of the bonus, if there is a scaling bonus from caster level it gives it in the next spot
        self.BonusOf = [1]
        # The per X caster level part of scaling bonuses. If it is 0 it ignores it
        self.PerCL = [0]
        # Type is what the bonus counts as, this is mostly for purposes of stacking, but overall, shouldn't
        # be too much of a problem with spells.
        self.BonusType = [' ']
        # The maximum of a flat bonus that it gives
        self.BonusMax = [0]

        # The rolls to be had by the spell
        # Rolls are done in duples, XdX
        self.Roll = [[0,0]]
        # Caster level bonus Ratio, caster level never changes die size, only number of die
        self.BonusRT = [0]
        # The maximum number of dice that can be rolled by the roll.
        self.RollDieMax = [0]
        # any flat damage will be marked in the previous bonus section

        # Effect is the area or how it effects a grouping of things, this include how it is aimed and other such
        # stuff.

        # The type of attack area it makes, this can by anything from a ray, to a missle, to an area Attatched to it
        # is extra details such as the cone, line, or whathave you of the effect, this includes number of things.
        # If the spell effects a number of creatures on a scalling level, it will put it in the bonus area as the
        # last thing for simplicity
        self.Effect = {' ': ' '}
