# Imports csv file into database
# att_num = number of attributes in the table (disregarding ID)
#   this may not be needed if I can figure out how to check the number
#   of elements in the first line of the csv

import csv
import sqlite3
from config import database

def populate_table(table_name, csv_file, att_num):

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
        
    # setting up sql command dynamically
    # NULL is for the ID which will be auto-allocated by the system
    command = 'INSERT INTO '+ table_name + ' VALUES (?' 
    for i in range(att_num):
        command += ',?'
    command +=');'
    
    # open csv file
    csvfile = open(csv_file,'r')
    creader = csv.reader(csvfile)
    next(creader)

    # copy csv file
    for j in creader:
        last+=1
        row = [last]+j
        db.execute(command,row)

    # save changes and close
    csvfile.close()
    db.commit()
    db.close()
    return
