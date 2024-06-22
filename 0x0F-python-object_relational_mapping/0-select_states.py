#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # connect to the MYSQL server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    # create a cursor object
    cur = db.cursor()
    #execute the SQL query
    cur.execute("SELECT * FROM states")

    #print the rows
    rows = cur.fetchall()
    for i in rows:
        print(i)
    # close the cursor and the connection
    cur.close()
    db.close()
