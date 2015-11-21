# creating this so that we can easily switch between test database and live database
# feel free to add other variables that will accomplish similar goals
import sqlite3

database="pathfinder.db"

def csvfinder():
    db=sqlite3.connect(database)
    cur=db.cursor()
    cur.execute('''select name from sqlite_master where type='table';''')
    result= cur.fetchall()
    csvfiles=[]
    for item in result:
        csvfiles.append(item[0])
    db.close()
    return(csvfiles)

#csvfiles=csvfinder()       # will give list of all tables in database
                            #   as a list of strings
csvfiles=['Stats', 'Stats'] # for use when testing

"""for file in csvfiles:  # for creating new csv files enmasse
    temp=open('data\\'+file+'csv','w+')
    temp.close()"""
