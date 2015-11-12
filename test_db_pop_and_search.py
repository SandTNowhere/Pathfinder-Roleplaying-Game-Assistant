import csv_to_sql
import search_database

csv_to_sql.populate_table("Stats","test.csv",2)
print "table populated"
test_table="Stats"
test_att = '*'
test_condition=str('st_name="Strength" OR st_descrip="HULK THINK!"')
test_search = search_database.search_db(test_att,test_table,test_condition)

for i in test_search:
    print i
