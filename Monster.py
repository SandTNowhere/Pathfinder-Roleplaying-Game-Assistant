# Monster Class File, Being prebuilt for later and as it can do many things a player can both can be improved at the
# same time.

import Character

# A few copies over from Race for the sake of eas of use.

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

# The Monster holder. This will have access to monsterous feats and abilities that are ordinarily out of the range
# Of players. More testing would be needed to ensure these acutally work.

class Monster(object):
    def __init__(self):
        # The monster's name
        self.Name = ' '
        # The monster's base race (for reference)
        self.Base = ' '
        # The monster's type
        self.Type = ' '
        # The subtypes of the monster
        self.SubType = [' ']
        # The size of the creature
        self.Size = 'med'
        # The templates that have been added on.
        self.Templates = [Templates()]
        # The character sheet that the monster holds most of it's data in. (may consider changing out
        self.CharacterSheet = Character.Character()
        # A list of monster abilities that are unique to them and often have no direct method of gaining them.
        # These are often built into the race or templates of the monster in the first place.
        self.Abilities = ' '
        # A list of feats this gives access to monster feats
        self.Feats = [' ']



# Templates are unique to monsters, though players may have them as well with GM prermission, though if they do
# they have officially entered monster territory and should be treated for the most part as such.
class Templates(object):
    def __init__(self):
        # The name of the template
        self.Name = ' '
