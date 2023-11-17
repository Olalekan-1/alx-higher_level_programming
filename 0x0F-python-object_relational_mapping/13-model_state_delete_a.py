#!/usr/bin/python3
""" deletes all State  objects with `a` from the database hbtn_0e_6_usa """

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

    state = session.query(State).filter(State.name.like('%a%')).order_by(
        State.id)

    for s in state:
        session.delete(s)

    session.commit()
