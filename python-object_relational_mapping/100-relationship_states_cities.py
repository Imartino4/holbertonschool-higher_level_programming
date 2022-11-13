#!/usr/bin/python3
"""
 creates the State “California” with the City “San Francisco”
 from the database hbtn_0e_100_usa
 user | password | database_name given as argv
 use cities relationship for all State objects
 """
from sys import argv
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    new_city = City(name='San Francisco', _State_=new_state)
    session.add(new_city)

    session.commit()
