# Equipment, items, weapons, and armor

# This is going to hold separate classes for items, equipments, armor, and weapons as these three act very
# differently from each other, if there are better ideas we can handle them, this is just a seed afterall.

# this currently also holds enchantments for arms and armor.

# This is primarily meant for mundane items, however it does still support magic items as many of these unequipable
# items are consumeable items that give magical benefits
class Item(object):
    def __init__(self):
        # The name of the item 
        self.Name = ' '
        # The type of item, mostly for magic items, but still important.
        self.Type = ' '
        # The price of the item, this is very maliable as many magic items are priced based on extact effects and
        # details
        self.Price = 0
        # The weight of the item, not much to say really.
        self.Weight = 0
        # The text of the item, or what have you.
        self.Text = 'what\'s to say?'
        # The enchantment of the item, and how many charges (most will only ever be 1 as potions have only 1 use)
        self.Enchantment = None
        # The charges of the item
        self.Charges = 0
        # Lastly, some items recharge daily, so here's a quick thing for that.
        self.Recharge = False
        # The source of the book outside, for reference.
        self.Source = 'book'
	
	
# technically magical items, but equipment is more generic and is a better name for a class
class equimpent(object):
    def __init__(self):
        # The name of the equipment
        self.Name = ' '
        # The magical aura of the item, while non-magical items don't have these most equipment other than armor and
        # Weapons are magical.
        self.Aura = ' '
        # The caster level of the enchantment of the item. Same thing as the aura.
        self.CL = 0
        # The slot the item belongs to. Weapons and armor are not valid slots for this class.
        self.Slot = ' '
        # Self explanatory
        self.Price = 0
        # Self Explanatory
        self.Weight = 0
        # The requirements to craft the item yourself. Often in the order of 'feat' then 'spell', price is based off
        # of the items market price (1/2 market price to make yourself).
        self.CraftReqs = [' ']
        # The enchantment it has, this is cover almost everything it does
        self.Enchantments = None
	

# Armor is equiped and only one may be had by any character at any time in terms of effects.
class Armor(object):
    def __init__(self):
        # The title of the Armor, often default, but allows for the item to be called something other than it's
        # base item name.
        self.Title = ' '
        # The name of the Armor
        self.Name = ' '
        # Is this armor, or a Shield
        self.IsArmor = True
        # The price of the item
        self.Price = 0
        # The armor bonus to AC that the item gives.
        self.ACBonus = 0
        # The Highest the character's Dexterity bonus to AC can be. -1 is the flag for unlimited dex bonus.
        self.MaxDex = 0
        # The penalty applied to skills that have an armor penalty
        self.ArmorPenalty = 0
        # The percent chance of failure for those trying to cast spells in the armor
        self.SpellFailure = 0
        # The ammount of speed that it slows the wearer down by, split into speed base 30 and base 20.
        self.Speed = [0,0]
        # The weight of the armor
        self.Weight = 0
        # The extra text of the Armor and/or it's mods
        self.Text = 'words'
        # The source book that the item comes from.
        self.Source = 'book'
        # A collection of small bonuses and other items that are simply flag as they are incredibly static. They
        # Mark the difference between the base item and the specific item in question.
        self.Mods = 0 #non-magical mods that are generally cheap.
        # The enchantment the item holds and the collection of total bonuses
        self.Enchantments = None
	
	
	
class Weapon(object):
    def __init__(self):
        # The title of the weapon if people want to name it something else.
        self.Title = ' '
        # The name of the item
        self.Name = ' '
        # The catagory of the item, simple, martial, and exotic
        self.Catagory = ' '
        # The handedness of the weapon, as a note, ranged weapons included as their own handedness as most can be
        # held in one hand but require two to use. The list light, one-handed, two-handed, and ranged
        self.Handedness = ' '
        # the cost of the item, should include the value of the item in GP
        self.Cost = 0
        # The damage of the item, this will be added to and altered, but overall it's very static. It is split into
        # number of die and the size of the die d1 is a should be ignored and just put at 1 and all weapons, even
        # with penalty a weapon will always deal at least 1 point of damage. If the size changes from the weapon it
        # should automatically change the damage to the appropriate damage.
        self.Damage = [ 1, 1]
        # The size of the weapon, Again, most default to medium, but if altered it will effect the standard damage
        # of the weapon.
        self.Size = ' '
        # The critical range of the weapon and the multiplyer of the weapon. Unlike other things, the defaults for
        # this is a 20 with a x2 multiplier as this is the most common and standard.
        self.Critical = [20,2]
        # The range of the weapon if it has one. If the range is -1 then it has no range and is not meant to be
        # thrown, Feats can change this, but that's something else entirely.
        self.Range = 10
        # The weight of the weapon
        self.Weight = 4
        # The damage type of the weapon, some weapons can have multiple types (for example a proper bite attack is
        # considered to be B,P, and S. The Types are Bludgeoning, Piercing, and Slashing.
        self.Type = [' '] # the type of damage dealt
        # This is any special features the weapon has, these are both dependent on the item itself and other special
        # modifiers such as material. For the most part it should be static.
        self.Special = [' ']
        # The book it comes from.
        self.Source = ' '
        # The text of the item for mor details.
        self.Text = ' '
        # The enchantments of the item
        self.Enchantments = None

# Enchantments are going to need a bit more of an explanation than the other items. 1st, for armor and weapons, they
# Calculate their value differently and add to it their items a bit differently than other magic items. Standard
# magic items have a straightforward price to them, that is defined elsewhere. While other's are dependent upon the
# spell they are enchanted with and the level of strength they are given with.
# Armor and weapons are cumulative in their cost, For armor the price is dependent upon the total enchantments on
# it. For weapons the price of the enchantment is dependent on the value of the total enchantments^2*2,000.
# Armor is the same but only 1,000. There are also 'flat' enchantments which have a flat price, but no 'enchantment'
# price to them, and so they are easier and don't apply to the standard limit to item's bonuses. Most items have a
# limit to how much they can be enchanted. It's a soft limit as you can go beyond this limit, but it is considered
# beyond standard games and the price increases drastically. We can add that in later.
# 2nd The enchantments can in many ways be like feats and give specific bonuses, these bonuses are far more likely
# to be static than feats, and some of them even give access to feats. I'll do my best with this enchantment section
# BUT it's something to bring up later.
# Lastly, Enchantments are incredibly static all things considered and can easily be stockpiled.
class Enchantments(object):
    def __init__(self):
        # The name of the enchantment
        self.name = ' '
        # The flat price of the enchantment
        self.price = 0
        # The enchantment price that is added to weapons and armor.
        self.enchant = 0
        # The aura of the enchantment, this is primarily for weapons and armor, but is also to confirm other item's
        # and equipment's auras.
        self.aura = ' '
        # The caster level of the bonus, this is both a requirement and a modifier. Again, it also reafirms the
        # item's bonuses.
        self.CL = 0
        # What the weapon is allowed on by default, this can be broken, but it must still make sense. This does
        # include more specific requirements such as must be on ranged weapons and such, but so long as it's not a
        # weapon or armor enchantment, it's a soft requirement.
        self.Weapon = [' ']
        # The text of the enchantment in general.
        self.Text = ' '
        # The shortened text that states only the bonuses given, so that it can be added to miscellaneous notes.
        self.SubText = ' '
        
        # Now onto the enchantment's effects.
        # What the effect is going to.
        self.BonusTo = [' ']
        # The ammount of the bonus
        self.BonusOf = [' ']
        # What the scaling bonus.
        self.BonusPer = [' ']
        # What the bonus is pulling from if any.
        self.BonusFrom = [' ']
        
        # If they give feats
        self.BonusFeat = None
        # If they give spells
        self.Spells = None
