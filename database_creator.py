# Creates sqlite3 tables for Spells and other, related tables. Will expand later to create all tables needed for the project.
# Will use a CSV (comma seperated values) file to populate the tables later. If someone else wants to do it for some reason: 
# http://www.dreamincode.net/forums/topic/190453-importing-csv-into-sqlite3-db/

import sqlite3
connection = sqlite3.connect("pathfinder.db")
cursor = connection.cursor()

# Character stats that exist in the game(strength, intelligence, etc)
cursor.execute('''
CREATE TABLE Stats(
st_id INTEGER PRIMARY KEY AUTOINCREMENT,
st_name VARCHAR(20),
st_descrip TEXT -- explanation of what the stat does.
);''')

# Powers granted by domains
cursor.execute('''
CREATE TABLE Granted_Powers(
gp_id INTEGER PRIMARY KEY AUTOINCREMENT,
gp_name VARCHAR(20),
effect TEXT -- may expand this later to be more similar to spells
);''')

# Wizardry Schools, not Hogwarts
cursor.execute('''
CREATE TABLE Schools(
sc_id INTEGER PRIMARY KEY AUTOINCREMENT,
sc_name VARCHAR(20)
);''')

# Cleric Domains
cursor.execute('''
CREATE TABLE Domains(
do_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
CREATE TABLE Descriptors(
de_id INTEGER PRIMARY KEY AUTOINCREMENT,
de_name VARCHAR(20)
);''')

#Spell types. Enhancement, attack, etc
cursor.execute('''
CREATE TABLE Spell_Types(
ty_id INTEGER PRIMARY KEY AUTOINCREMENT,
ty_name VARCHAR(20)
);''')

# Spells
cursor.execute('''
CREATE TABLE Spells (
id INTEGER PRIMARY KEY AUTOINCREMENT,
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

print("done")
