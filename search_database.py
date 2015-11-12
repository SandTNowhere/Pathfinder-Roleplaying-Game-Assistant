# Program for accessing database
# att = attribute you want returned (name, description, value, etc)
#   send * to get all attributes
# table = table name
# condition = conditional used to filter the table (must be legal in SQLite)

import sqlite3

def search_db(att, table, condition):
    connection = sqlite3.connect("pathfinder.db")
    cursor = connection.cursor()
    # ?'s get replaced by the values after the ' in order
    command = 'SELECT ' + att + ' FROM ' + table + ' WHERE ' + condition
    cursor.execute(command)
    response = cursor.fetchall()

    connection.close()
    return response

