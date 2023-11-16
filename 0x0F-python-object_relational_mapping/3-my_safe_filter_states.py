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

    host = "localhost"
    user = argv[1]
    port = 3306
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
        host=host, user=user, port=port, passwd=password, db=db)

    cursor = conn.cursor()

    statement = "SELECT * FROM states WHERE name = %s"
    arg = argv[4]

    cursor.execute(statement, (arg,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)
