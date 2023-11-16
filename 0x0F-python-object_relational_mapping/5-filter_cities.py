#!/usr/bin/python3

"""
     Lists the cities associted with a state passed as
      argument in the 'hbtn_0e_0_usa' database

"""
import sys
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

    arg = argv[4]

    statement = "SELECT cities.name  AS city\
                FROM cities \
                JOIN states ON states.id = cities.state_id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC"

    cursor.execute(statement, (arg,))
    cities = []
    for c in cursor.fetchall():
        for city in c:
            cities.append(city)

    print(", ".join(cities))
