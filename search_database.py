# Program for accessing database
# att = attribute you want returned (name, description, value, etc)
#   send * to get all attributes
# table = table name
# condition = conditional used to filter the table (must be legal in SQLite)
#   condition should include WHERE (or other appropriate keyword) at the start
#   this was left out to all the selection of all entries if condition was left
#   as ''.

import sqlite3
from config import database

def search_db(att, table, condition):
    connection = sqlite3.connect(database)
    connection.text_factory=str
    cursor = connection.cursor()

    command = 'SELECT ' + att + ' FROM ' + table + ' ' + condition
    try:
        cursor.execute(command)
        response = cursor.fetchall()
    except:
        print("couldn't execute command: " + command)
        connection.close()
        return

    connection.close()
    return response

