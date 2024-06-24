#!/usr/bin/python3
"""
Script to delete all records of a tablet
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    #connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # create a cursor object
    # execute the SQL query.
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean close the cursor and the connection
    cur.close()
    db.close()
