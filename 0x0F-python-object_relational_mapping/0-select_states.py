#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
a script that lists all states from the database hbtn_0e_0_usa:
"""

my_db = MySQLdb.connect(host='localhost',
                        user=argv[1],
                        password=argv[2],
                        db=argv[3],
                        port=3306)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM states ORDER BY stated.id ASC;")

results = my_cursor.fetchall()

for row in results:
    print(row)

my_cursor.close()
my_db.close()
