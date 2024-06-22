#!/usr/bin/python3
"""
 script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

# The code not be executed when imported
if __name__ == '__main__':

    # connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # same connection to the database.
    cur = db.cursor()
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nmeSr)

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
