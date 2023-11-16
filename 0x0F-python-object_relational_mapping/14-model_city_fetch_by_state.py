#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Defines the connection and the sessionmaker
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    cities = session.query(State, City).join(City).filter(
        State.id == City.state_id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
