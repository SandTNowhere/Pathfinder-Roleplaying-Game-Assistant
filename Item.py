# Equipment, items, weapons, and armor

# This is going to hold separate classes for items, equipments, armor, and weapons as these three act very
# differently from each other, if there are better ideas we can handle them, this is just a seed afterall.

# this currently also holds enchantments for arms and armor.

class Item(object):
    name = 'dohicky'
    price = 0
    weight = 1000000
    text = 'what\'s to say?'
    source = 'book'
	
	
# technically magical items, but equipment is more generic and is a better name for a class
class equimpent(object): 
	name = 'whizbang'
	aura = 'something strange'
	CL = 1
	slot = 'belt' # may replace with number, but we can discuss this when we make items implemented
	price = 1
	weight = 1
	#bonuses method TBD
	craftReqs = ['feat', 'spell\'s']
	
	
class Armor(object):
    name = 'water pail'
    price = 0
    ACBonus = 0
    MaxDex = 0
    ArmorPenalty = -1
    SpellFailure = 100
    Speed = [30,20] #split into 30 and 20 foot speeds
    weight = 0
    text = 'words'
    source = 'book'
    mods = 0 #non-magical mods that are generally cheap.
    #enchantments
	
	
	
class Weapon(object):
    name = 'soft, purple, rubber baseballbat'
    catagory = 'simple'
    handedness = 'light'
    cost = 0
    damage = '1d3' # defaults to medium, should change with size type
    size = 'medium'
    critical = '19-20x3'
    range = 10 # suggest -1 for - or rangeless
    weight = 4
    type = ['B'] # the type of damage dealt
    special = ['nonlethal'] # what special features are included with it.
    source = 'book'
    text = 'stuff'
	
class Enchantments(object):
	name = 'something'
	#This is a bit funny, but hear me out.
	# A enchant is a bonus price, bonus price scales based off of current enchantment on the item
	# if it has a flat bonus price enchant will be 0 and price will hold the price of the enchantment
	# this price is added flatly to the cumulative weapon enchantment and doesn't count toward the overall
	# enchantment of the weapon
	price = 0
	enchant = 0
	aura = 'strange'
	CL = 0
	Weapon = True #enchantments like these are almost exclusive to weapons and armor
