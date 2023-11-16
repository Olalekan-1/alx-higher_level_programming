#!/usr/bin/python3

"""
     Lists the cities associted with their state
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

    statement = "SELECT cities.id, cities.name,  states.name \
                FROM cities \
                JOIN states ON states.id = cities.state_id \
                ORDER BY cities.id ASC"

    cursor.execute(statement)

    [print(city) for city in cursor.fetchall()]
