#!/usr/bin/python3
"""
    Adds a new state objects to the State table
    in hbtn_0e_6_usa database
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

    state = State()
    state.id = 6
    state.name = "Louisiana"
    session.add(state)
    session.commit()
    print(state.id)
