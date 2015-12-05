# Creates sqlite3 tables for Spells and other, related tables.
# tables are based on class objects but are not exact matches to those
#   objects as instances of class objects are meant to be customizable
#   versions of entries found in the tables.
# Will expand later to create all tables needed for the project.

import sqlite3
from config import database

connection = sqlite3.connect(database)
cursor = connection.cursor()

# Stats.(strength, intelligence, etc)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Stats(
st_id INTEGER PRIMARY KEY,
st_name VARCHAR(20),
st_descrip TEXT -- explanation of what the stat does.
);''')

#Racial Sizes (med, large(tall), colossal(long), etc )
cursor.execute('''
CREATE TABLE IF NOT EXISTS Racial_Sizes(
rs_id INTEGER PRIMARY KEY,
rs_name VARCHAR(30)
);''')

#Racial Types (aberration, animal, dragon, etc)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Racial_Types(
rt_id INTEGER PRIMARY KEY,
rt_name VARCHAR(30)
);''')

#Racial Sub-Types (air, angel, kaiju, kami, etc)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Racial_Sub_Types(
rst_id INTEGER PRIMARY KEY,
rst_name VARCHAR(30)
);''')

#Traits
cursor.execute('''
CREATE TABLE IF NOT EXISTS Racial_Traits(
rtr_id INTEGER PRIMARY KEY,
rtr_name VARCHAR(30),
description TEXT
);''')

#Races
cursor.execute('''
CREATE TABLE IF NOT EXISTS Races(
ra_id INTEGER PRIMARY KEY,
ra_name VARCHAR(30),
base_str INTEGER,
base_dex INTEGER,
base_con INTEGER,
base_int INTEGER,
base_wis INTEGER,
base_cha INTEGER,
size VARCHAR(30),
type VARCHAR(30),
sub_type VARCHAR(30),
speed INTEGER,
traits VARCHAR30,
notes TEXT,
FOREIGN KEY (size) REFERENCES Racial_Sizes(rs_name),
FOREIGN KEY (type) REFERENCES Racial_Types(rt_name),
FOREIGN KEY (sub_type) REFERENCES Racial_Sub_Types(rst_name)
FOREIGN KEY (traits) REFERENCES Racial_Traits(rtr_name)
);''')

#Languages. Also links to races that learn them naturally.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Languages(
la_id INTEGER PRIMARY KEY,
la_name VARCHAR(30),
race VARCHAR,
FOREIGN KEY (race) REFERENCES Races (ra_name)
);''')

#Classes.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Classes(
cl_id INTEGER PRIMARY KEY,
cl_name VARCHAR(30),
prereqs VARCHAR(30),   -- expand to something that the sys can understnad? Maybe, currently it looks for flags and if they meet the numerical requirement it asks for.
hit_dice INTEGER,      
base_atk_bonus REAL,  
save_reflex BOOLEAN,   -- FALSE = bad, TRUE=good
save_fortitude BOOLEAN,
save_will BOOLEAN,
rank_per_level INTEGER,
proficencies TEXT,  -- bows, exotics, two-handed, etc
description TEXT,   -- book description of class
-- features also left out and put in their own table.
initial_gp REAL,     -- starting money
CHECK(base_atk_bonus = .5 OR base_atk_bonus = .75 OR base_atk_bonus = 1)
);''')

#Skills
cursor.execute('''
CREATE TABLE IF NOT EXISTS Skills(
skd_id INTEGER PRIMARY KEY,
sk_name VARCHAR(30),
sk_desc TEXT
);''')

#Skill/Class relations
cursor.execute('''
CREATE TABLE IF NOT EXISTS Skills_by_Class(
skbc_id INTEGER PRIMARY KEY,
sk_name VARCHAR(30),
class VARCHAR(30),
FOREIGN KEY (class) REFERENCES Classes(cl_name),
FOREIGN KEY (sk_name) REFERENCES Skills(sk_name)
);''')

#Features.
# We sholud probably go over this together.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Features(
fet_id INTEGER PRIMARY KEY,
fet_name VARCHAR(30),
min_level INT, -- minimum level needed to acquire
               -- may need to be moved to Features_by_Class
               -- if this is variable by class
-- don't understand what slot is supposed to be doing,
-- so not sure if it should be in db
-- same for Bonus Feats, Feat Limits, BonusTo, BonusOf, BonusPer,
-- BonusFrom, BonusType and the various Points attributes
--
-- Slot is for archetyping, an archetype changes out some class features for other class features, but you may apply as many archetypes as you wish. BUT, they cannot overlap, hence the slot.
active INT, -- 0 = Passive, 1 = Active, anything else means it has both an active and a passive component
description TEXT -- book description
);''')

# feature/class relations
cursor.execute('''
CREATE TABLE IF NOT EXISTS Features_by_Class(
fetbc_id INTEGER PRIMARY KEY,
fetbc_name VARCHAR(30),
class VARCHAR(30),
FOREIGN KEY (class) REFERENCES Classes(cl_name),
FOREIGN KEY (fetbc_name) REFERENCES Features(fet_name)
);''')

#Archetypes. Can more than one base class have the same archetype?
#  Assuming no at the moment.
# No, Archetypes cannot have more than one class at a time. Names may be shared, but that is what the class part is for, to keep any similar naming problems that coldu arries a non-issue.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Archetypes(
ar_id INTEGER PRIMARY KEY,
ar_name VARCHAR(30),
description TEXT,
class VARCHAR(30),
FOREIGN KEY (class) REFERENCES CLASSES(cl_name)
);''')

#Feats
# This needs quite a bit of correction, but this feature, not feat, from how it's been written.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Feats(
fe_id INTEGER PRIMARY KEY,
fe_name VARCHAR(30),
class VARCHAR(30),
arche VARCHAR(30),
min_level INTEGER DEFAULT 0,
-- should slot be included? Yes, it is pertinent for Archetyping.
bonus_feat_1 VARCHAR(30),
bonus_feat_2 VARCHAR(30),
bonus_feat_3 VARCHAR(30),
bonus_feat_n TEXT,
-- not sure exactly what feat limits is.
--   does having a feat limit what other feats you can take? 
--   or is this something else?
--
-- Feat limits are what is allowed to be taken by the feature. Most features give a preexisting list of feats, or type of feat that is allowed.
-- So should Feat limit be a list of feats that are referenced or just a Text field?
active BOOLEAN,  -- True=activate to use, False= always active
-- not sure what to do with Bonus stuff
-- I'm not quite sure either, but again, it's part of the logic to apply numerical bonuses.
points_static INTEGER,
points_dynam INTEGER,
points_stat VARCHAR(30),
points_mod REAL,
descrption TEXT,
FOREIGN KEY (class) REFERENCES CLASSES(cl_name),
FOREIGN KEY (arche) REFERENCES Archetypes(ar_name),
FOREIGN KEY (points_stat) REFERENCES Stats(st_name),
FOREIGN KEY (bonus_feat_1) REFERENCES Feats(fe_name),
FOREIGN KEY (bonus_feat_2) REFERENCES Feats(fe_name),
FOREIGN KEY (bonus_feat_3) REFERENCES Feats(fe_name)
);''')

#Traits
cursor.execute('''
CREATE TABLE IF NOT EXISTS Traits(
tr_id INTEGER PRIMARY KEY,
tr_name VARCHAR(30),
-- still not sure what's up with slots
-- Slots in this case, are for traits that can be taken instead of others, but they cannot overlap with each other.
feat VARCHAR(30),  --associated feat.
daily_uses INTEGER DEFAULT -1,
FOREIGN KEY (feat) REFERENCES Feats(fe_name)
-- still not sure about bonus stuff either
-- Reference would be better, but a simple string could get the job done if we do it right.
);''')

#Item types (weapon, shield, armor, sword, etc).
#  For use with enchantments and other things that care about item type.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Item_types(
it_id INTEGER PRIMARY KEY,
it_name VARCHAR(30)
);''')

#Enchantments.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Enchantments(
ec_id INTEGER PRIMARY KEY,
ec_name VARCHAR(30),
base_price REAL,  -- price of enchanting
price_mod REAL,   -- price adjustment to enchanted item
aura VARCHAR(30), 
caster_level INTEGER DEFAULT 0,
available_for VARCHAR(30),
description TEXT, -- book description
summary TEXT,      -- boiled down description (+2 fire damage or whatever)
FOREIGN KEY (available_for) REFERENCES Item_types (it_name)
);''')

# Items
cursor.execute('''
CREATE TABLE IF NOT EXISTS Items(
it_id INTEGER PRIMARY KEY,
it_name VARCHAR(30),
it_type VARCHAR(30),
price REAL,
weight REAL,
descritption TEXT,
enchantment VARCHAR(30), -- reference another table? allow multi-enchant?
charges INTEGER,
rechargeable BOOLEAN,
source VARCHAR(30), -- reference another table?
FOREIGN KEY (it_type) REFERENCES Item_types (it_name)
);''')

# Equipment. Not Armor or Weapons. These are the base versions and may
# not be the same as what appears in a given character sheet or campaign.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Equipment(
eq_id INTEGER PRIMARY KEY,
eq_name VARCHAR(30),
aura VARCHAR(20),  -- leave empty if not applicable
caster Level INT,  -- 0 if not applicable
slot VARCHAR(20),  -- Slot refers to equipment slot. Back, head, neck, right index finger, etc
                   -- unslotted if multiples can be equipped.
price REAL, 
weight REAL,
craft_requirements TEXT,
enchantment_1 VARCHAR(30),
enchantment_2 VARCHAR(30),
enchantment_3 VARCHAR(30),
enchantment_n TEXT,
FOREIGN KEY (enchantment_1) REFERENCES Enchantments (ec_name),
FOREIGN KEY (enchantment_2) REFERENCES Enchantments (ec_name),
FOREIGN KEY (enchantment_3) REFERENCES Enchantments (ec_name)
);''')

#Armour.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Armour(
ar_id INTEGER PRIMARY KEY,
ar_name VARCHAR(30),
eq_slot VARCHAR(30),
base_price REAL,
ac_bonus INTEGER DEFAULT 0,
max_dex INTEGER DEFAULT -1, -- -1 if not applicable
armour_penalty INTEGER DEFAULT 0,
spell_failure INTEGER DEFAULT 0,
speed20 INTEGER DEFAULT 0,
speed30 INTEGER DEFAULT 0,
weight REAL,
description TEXT --description from book
);''')

#Weapons.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Weapons(
we_id VARCHAR(30),
we_name VARCHAR(30),
category VARCHAR(30),   
handedness VARCHAR(30),
base_price REAL,       
damage_dt INTEGER,      -- die type
damage_dn INTEGER,      -- number of dice
size VARCHAR(20),
crit_rng INTEGER,       -- critical range
crit_m INTEGER,         -- critical multiplier
range INTEGER DEFAULT -1,  -- -1 if not meant to be thrown
weight REAL,
dam_type VARCHAR(30),   -- reference list?
description TEXT,        -- from book
FOREIGN KEY (category) REFERENCES Item_types (it_name)  -- relying on those entering the data to not list a sabre as a type of armor
CHECK(handedness = "one" OR handedness = "two" OR handedness = "one or two" OR handedness = "special"), -- this about cover it?
CHECK(size="fine" OR size ="diminutive" OR size="tiny" OR size ="medium" OR size="large" OR size="huge" OR size="Gargantuan" OR size="colossal")

);''')

# Powers granted by priest domains
cursor.execute('''
CREATE TABLE IF NOT EXISTS Granted_Powers(
gp_id INTEGER PRIMARY KEY,
gp_name VARCHAR(20),
effect TEXT -- may expand this later to be more similar to spells
);''')

# Wizardry Schools, not Hogwarts
cursor.execute('''
CREATE TABLE IF NOT EXISTS Schools(
sc_id INTEGER PRIMARY KEY,
sc_name VARCHAR(20)
);''')

# Cleric Domains
cursor.execute('''
CREATE TABLE IF NOT EXISTS Domains(
do_id INTEGER PRIMARY KEY,
do_name VARCHAR(20),
deities VARCHAR(200),
power1 VARCHAR(20),
power2 VARCHAR(20),
power3 VARCHAR(20), -- unlikely to be used
power4 VARCHAR(20),  -- unlikely to be used

FOREIGN KEY (power1) REFERENCES Granted_Powers(gp_name),
FOREIGN KEY (power2) REFERENCES Granted_Powers(gp_name),
FOREIGN KEY (power3) REFERENCES Granted_Powers(gp_name),
FOREIGN KEY (power4) REFERENCES Granted_Powers(gp_name)
);''')

# Spell Descriptors. Acid, fire, ice, etc
cursor.execute('''
CREATE TABLE IF NOT EXISTS Descriptors(
de_id INTEGER PRIMARY KEY,
de_name VARCHAR(20)
);''')

#Spell types. Enhancement, attack, etc
cursor.execute('''
CREATE TABLE IF NOT EXISTS Spell_Types(
ty_id INTEGER PRIMARY KEY,
ty_name VARCHAR(20)
);''')

# Spells
cursor.execute('''
CREATE TABLE IF NOT EXISTS Spells (
id INTEGER PRIMARY KEY,
sp_name VARCHAR(64),
school VARCHAR(20), -- include school and subschool, space delim
domain VARCHAR(20), -- include domain and subdomain, space delim
descriptor1 VARCHAR(20), --acid, fire, etc
descriptor2 VARCHAR(20), 
descriptor3 VARCHAR(20),
descriptor4 VARCHAR(20),
descriptor5 TEXT,	-- catch all for spells with more than 4 descriptors

sp_level INT,  -- spell level
time VARCHAR(20),  -- casting time
components TEXT, -- verbal, semantic, etc
range VARCHAR(10), -- range of the spell
target VARCHAR(20), -- legal targets for spell (ex: self)
duration VARCHAR(20), 
dur_efemera VARCHAR(20),
save_stat VARCHAR(20) ,
save_descrip TEXT, -- describes effect of succesful save
resist INT, --bool. Used for spells that are affected by spell resistance
sp_descrip TEXT, -- spell description

bonus_to VARCHAR(20), -- this section is still a work in progress
bonus_of INT,
bonus_per_CL INT,
bonus_type VARCHAR(20),
bonus_max INT,
roll_type INT, -- type of dice to roll
roll_number INT, -- number of dice to roll
bonus_rt VARCHAR(20),
roll_max INT, -- max bonus from bonus_rt
effect VARCHAR (255), -- AoE type/max number of targets/targeting methodology

CHECK (sp_level >= 0 AND sp_level <= 9),
CHECK (range = 'close' OR range = 'medium' OR range = 'long'),
CHECK (resist = 0 OR resist = 1),

FOREIGN KEY (school) REFERENCES Schools(sc_name),
FOREIGN KEY (domain) REFERENCES Domains(do_name),
FOREIGN KEY (descriptor1) REFERENCES Descriptors(de_name),
FOREIGN KEY (descriptor2) REFERENCES Descriptors(de_name),
FOREIGN KEY (descriptor3) REFERENCES Descriptors(de_name),
FOREIGN KEY (descriptor4) REFERENCES Descriptors(de_name),
FOREIGN KEY (save_stat) REFERENCES Stats(st_name),
FOREIGN KEY (bonus_type) REFERENCES Spell_Types(ty_name)

);''')

connection.commit()
connection.close()
