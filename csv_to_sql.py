# Imports csv file located in data folder into database
# Assumes that the csv file and the table have the same name
# Should throw an error if a line of the csv is improperly formated.
# This will not catch instances of bad data of the correct type
#  (i.e.: typing 1,2 instead of 2,1 when recording two integer
#   columns in the csv)
# leave spaces for empty strings, and 0s for non-applicable numbers
#   unless noted otherwise in database_creator.

import csv
import sqlite3
from config import database

def populate_table(table_name):

    # open database
    db = sqlite3.connect(database)
    cursor=db.cursor()

    #for testing only
    db.execute('delete from '+table_name)
    
    #find last entry
    command = 'SELECT max(rowid) FROM ' + table_name
    cursor.execute(command)
    last=cursor.fetchone()[0]
    if last is None:
        last=0  
    
    # open csv file
    csvfile = open(('data\\' + table_name + '.csv'),'r')
    creader = csv.reader(csvfile)
    
    # setting up sql command dynamically
    # NULL is for the ID which will be auto-allocated by the system    
    command = 'INSERT INTO '+ table_name + ' VALUES (?' 
    try:
        for i in next(creader): #eliminating csv header
            command += ',?'
        command +=');'

    # copy csv file
        for j in creader:
            last+=1
            row = [last]+j
            try:
                db.execute(command,row)
            except:
                try:
                    row=row[:len(row)-1] #in case of trailing comma
                    db.execute(command,row)
                except:
                    print(str(row) + " could not be added to " + table_name + ".")
                    last-=1
    except:
        print(table_name + ' is empty')
    # save changes and close
    csvfile.close()
    db.commit()
    db.close()
    return
