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
traits TEXT,  -- should this reference a list?
notes TEXT,
FOREIGN KEY (size) REFERENCES Racial_Sizes(rs_name),
FOREIGN KEY (type) REFERENCES Racial_Types(rt_name),
FOREIGN KEY (sub_type) REFERENCES Racial_Sub_Types(rst_name)
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

#Features.
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
active BOOLEAN, -- true if it needs to be activated, false otherwise
-- do any features have both an active and a passive component?
--   if so, how should we handle them?
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
cursor.execute('''
CREATE TABLE IF NOT EXISTS Archetypes(
ar_id INTEGER PRIMARY KEY,
ar_name VARCHAR(30),
description TEXT,
class VARCHAR(30),
FOREIGN KEY (class) REFERENCES CLASSES(cl_name)
);''')

#Feats
cursor.execute('''
CREATE TABLE IF NOT EXISTS Feats(
fe_id INTEGER PRIMARY KEY,
fe_name VARCHAR(30),
class VARCHAR(30),
arche VARCHAR(30),
min_level INTEGER DEFAULT 0,
-- should slot be included? Not sure what it is
bonus_feat VARCHAR(30),  -- should this be a foreign key refernces feats?
                         -- can there be more than one bonus feat?
                         -- can a feat be a bonus feat of more than one feat?
-- not sure exactly what feat limits is.
--   does having a feat limit what other feats you can take?
--   or is this something else?
active BOOLEAN,  -- True=activate to use, False= always active
-- not sure what to do with Bonus stuff
points_static INTEGER,
points_dynam INTEGER,
points_stat VARCHAR(30),
points_mod INTEGER,
-- I assume this is an int, change to whatever is appropriate if I'm wrong
descrption TEXT,
FOREIGN KEY (class) REFERENCES CLASSES(cl_name),
FOREIGN KEY (arche) REFERENCES Archetypes(ar_name),
FOREIGN KEY (points_stat) REFERENCES Stats(st_name)
);''')

#Traits
cursor.execute('''
CREATE TABLE IF NOT EXISTS Traits(
tr_id INTEGER PRIMARY KEY,
tr_name VARCHAR(30),
-- still not sure what's up with slots
feat VARCHAR(30),  --associated feat. can there be more than one?
daily_uses INTEGER DEFAULT -1,
FOREIGN KEY (feat) REFERENCES Feats(fe_name)
-- still not sure about bonus stuff either
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
