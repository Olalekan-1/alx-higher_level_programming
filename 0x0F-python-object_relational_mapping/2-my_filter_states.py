#!/usr/bin/python3

"""
     Lists the state passed as argument present
     in the 'hbtn_0e_0_usa' database

"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
       Connects to the local host mysql server
       and perform the queries.
    """

    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print(row)
