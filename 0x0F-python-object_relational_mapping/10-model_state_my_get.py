#!/usr/bin/python3
"""
    lists State objects with passed as an argument
     from the database hbtn_0e_6_usa
     """

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

    arg = argv[4]

    state = session.query(State).filter(State.name == '{}'.format(arg))
    if state.first() is None:
        print('Not found')
    else:
        for s in state:
            print(s.id)
