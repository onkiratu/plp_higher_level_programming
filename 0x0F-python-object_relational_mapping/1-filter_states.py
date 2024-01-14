#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    my_cursor = my_db.cursor()

    my_cursor.execute(
        """SELECT * FROM states WHERE name LIKE
        BINARY 'N%' ORDER BY states.id ASC;
        """
        )

    results = my_cursor.fetchall()

    for row in results:
        print(row)

    my_cursor.close()
    my_db.close()
