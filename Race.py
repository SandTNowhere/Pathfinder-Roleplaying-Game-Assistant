# Race file for Pathfinder Roleplaying game assistant

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

class Race:
    #Attributes
    stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha':0}
    size = 'med'
    type = 'humanoid'
    subtype = 'human'
    speed = 30
    startingLanguages = 'Common'
    #traits, method of work TBD
	
	#lore/race information typed out in words
	extraText = 'uman bro'

    
