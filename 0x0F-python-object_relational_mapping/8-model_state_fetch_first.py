#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Defines the connection and the sessionmaker
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    first = session.query(State).order_by(State.id)
    if first.first() is None:
        print()
    else:
        print("{}: {}".format(first[0].id, first[0].name))
