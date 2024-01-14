#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    my_cursor = my_db.cursor()

    my_cursor.execute(
        """SELECT cities.id, cities.name, states.name 
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id ASC;"""
        )

    results = my_cursor.fetchall()

    for row in results:
        print(row)

    my_cursor.close()
    my_db.close()
