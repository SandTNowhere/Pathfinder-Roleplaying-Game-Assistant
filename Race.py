# Race file for Pathfinder Roleplaying game assistant

import Feat

# some useful information that should be constant for the most part (there are no constants in python)
# can be added to or changed if needed, but should make that later feature
# sizes, includes all for later integration into monsters.
Sizes = ['fine','diminutive','tiny','small','medium','large(tall)','large(long)','huge(tall)','huge(long)',
	 'gargantuan(tall)','gargantuan(long)','colossal(tall)','colossal(long)']
# types of races and subtypes, brushed on with players, almost entirely for monsters.
RaceTypes = ['aberration','animal','construct','dragon','fey','humanoid','magical beast',
             'monstrous humanoid','ooze','outsider','plant','undead','vermin']
# subtypes for stuff, again mostly for monsters.
SubTypes = ['adlet','aeon','agathon','air','angel','aquatic','archon','asura','augmented','azata',
	    'behemoth','catfolk','chaotic','clockwork','cold','colossus','daemon','dark folk','demodand',
	    'demon','devil','div','dwarf','earth','elemental','elf','evil','extraplanar','fire','giant',
	    'gnome','goblinoid','godspawn','good','great old one','halfling','herald','human',
	    'incorporated','inevitable','kaiju','kami','kasatha','kitsune','kyton','lawful','leshy',
	    'mythic','native','nightshade','oni','orc','protean','psychopomp','qlippoth','rakshasa',
	    'ratfolk','reptilian','robot','samsaran','sasquatch','shapechanger','swarm','troop','udaeus',
	    'vanara','vishkanya','water']

# the most flexible of them, should be easy to add to.
Languages = ['aboleth','abyssal','aklo','aquan','auran','boggard','celestial','common','cyclops',
	     'dark folk','draconic','drow sign language','druidic','dwarven','d\'ziriak','elven','giant',
             'gnoll','gnome','goblin','grippli','halfling','ignan','infernal','necril','orc','protian',
	     'sphinx','sylvan','tengu','terran','treant','undercommon','vegepygmy']


#Race class

class Race(object):
    def __init__(self):
        # The name of the race
        self.Name = ' '
        # The static Stat Block of the race, if the race has flexible bonuses to these, then they are under
        # Racial traits rather than here.
        self.Stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha':0}
        # The size of the race 'med' being the standard for most races.
        self.Size = 'med'
        # The type of the race, this has a number of effects on the bonuses and what the race get's but for most
        # characters, this is rather unimportant.
        self.RaceType = 'humanoid'
        # Subtype adds and creates a few more things for the races, however, again, this is more for monsters than
        # characters
        self.SubType = 'human'
        # This is how fast the character moves by default and most move at 30. Extra modes of movement are under
        # Racial Traits
        self.Speed = 30
        # The starting languages of the race, these are always given to the player regardless of race.
        self.StartingLanguages = 'common'
        # The list of race Traits that are more unique than can be immediately described.
        self.traits = None
        # The section of racial information, nothing particularly important in terms of mechanics, but it's needed
        self.Notes = ' '

    def Speed(self):
        return self.speed

    def Name(self):
        return self.name

    def Traits(self):
        return self.traits

    def TraitData(self, Trait):
        return self.traits[Trait]
