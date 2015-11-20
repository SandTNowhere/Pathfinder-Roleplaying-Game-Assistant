# Creates sqlite3 tables for Spells and other, related tables.
# tables are based on class objects but are not exact matches to those
#   objects as instances of class objects are meant to be customizable
#   versions of entries found in the tables.
# Will expand later to create all tables needed for the project.

import sqlite3
from config import database

connection = sqlite3.connect(database)
cursor = connection.cursor()

#Classes.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Classes(
cl_id INTEGER PRIMARY KEY,
cl_name VARCHAR(30),
prereqs VARCHAR(30),   -- expand to something that the sys can understnad?
hit_dice INTEGER,      -- reference a list?
basic_atk_bonus REAL,  -- make INT? reference list?
save_reflex BOOLEAN,   -- FALSE = bad, TRUE=good
save_fortitude BOOLEAN,
save_will BOOLEAN,
rank_per_level INTEGER,
proficencies TEXT,  -- bows, exotics, two-handed, etc
description TEXT,   -- book description of class
-- features also left out and put in their own table.
initial_gp REAL     -- starting money
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

#Features. Not really sure what should these two tables
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
active BOOLEAN,
description TEXT -- book description
);''')

# feature/class relations
cursor.execute('''
CREATE TABLE IF NOT EXISTS Features_by_Class(
fetbc_id INTEGER PRIMARY KEY,
fet_name VARCHAR(30),
class VARCHAR(30),
FOREIGN KEY (class) REFERENCES Classes(cl_name),
FOREIGN KEY (fet_name) REFERENCES Features(fet_name)
);''')

#Archetypes. Can more than one base class have the same archetype? Assuming no atm.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Archetypes(
ar_id INTEGER PRIMARY KEY,
ar_name VARCHAR(30),
description TEXT,
class VARCHAR(30),
FOREIGN KEY (class) REFERENCES CLASSES(cl_name)
);''')

#Enchantments.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Enchantments(
ec_id INTEGER PRIMARY KEY,
ec_name VARCHAR(30),
base_price REAL,  -- price of enchanting
price_mod REAL,   -- price adjustment to enchanted item
aura VARCHAR(30), -- reference list?
caster_level INTEGER DEFAULT 0,
available_for VARCHAR(30), -- reference items, equipment ,armour,weapons,null?
description TEXT, -- book description
summary TEXT      -- boiled down description (+2 fire damage or whatever)
);''')

# Items
cursor.execute('''
CREATE TABLE IF NOT EXISTS Items(
it_id INTEGER PRIMARY KEY,
it_name VARCHAR(30),
it_type VARCHAR(30), -- reference another table?
price VARCHAR(20), -- should this be Real or Int? Break it into coin types?
weight REAL,
descritption TEXT,
enchantment VARCHAR(30), -- reference another table? allow multi-enchant?
charges INTEGER,
rechargeable BOOLEAN,
source VARCHAR(30) -- reference another table?
);''')

# Equipment. Not Armor or Weapons. These are the base versions and may
# not be the same as what appears in a given character sheet or campaign.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Equipment(
eq_id INTEGER PRIMARY KEY,
eq_name VARCHAR(30),
aura VARCHAR(20),  -- leave empty if not applicable
caster Level INT,  -- 0 if not applicable
slot VARCHAR(20),  -- reference another table or list?
-- Slot refers to equipment slot. Back, head, neck, right index finger, etc
price VARCHAR(20), -- Real or Int? Coin types?
weight REAL,
craft_requirements TEXT,
enchantments TEXT
-- reference another table? allow multi-enchant? leave out altogether?
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
category VARCHAR(30),   -- reference a list?
handedness VARCHAR(30), -- reference a list?
base_price REAL,        -- real or 3+ ints?
damage_dt INTEGER,      -- die type
damage_dn INTEGER,      -- number of dice
size VARCHAR(20),       -- reference a list?
crit_rng INTEGER,       -- critical range
crit_m INTEGER,         -- critical multiplier
range INTEGER DEFAULT -1,  -- -1 if not meant to be thrown
weight REAL,
dam_type VARCHAR(30),   -- reference list?
description TEXT        -- from book
);''')

# Character stats that exist in the game(strength, intelligence, etc)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Stats(
st_id INTEGER PRIMARY KEY,
st_name VARCHAR(20),
st_descrip TEXT -- explanation of what the stat does.
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
