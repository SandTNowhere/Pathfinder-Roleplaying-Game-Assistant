import csv_to_sql
import search_database
from config import csvfiles

for item in csvfiles:
    csv_to_sql.populate_table(item)

test_table="Stats"
test_att = '*'
test_condition=str(' WHERE st_name="Stamina" OR st_descrip="HULK THINK!"')
test_search = search_database.search_db(test_att,test_table,test_condition)

for i in test_search:
    print (i)
