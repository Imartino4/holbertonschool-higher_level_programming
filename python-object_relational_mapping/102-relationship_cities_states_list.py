#!/usr/bin/python3
"""
 lists all City objects contained in the database hbtn_0e_101_usa
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

    cities_ = session.query(City).order_by(City.id)
    for c in cities_:
        print(f"{c.id}: {c.name} -> {c.states}")