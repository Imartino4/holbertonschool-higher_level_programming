#!/usr/bin/python3
"""
This script print all City objects from hbtn_0e_14_usa database
username, password and db name must be given as argv arguments
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state_city = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id)
    """ state_city: Tupla (State_object, City_object)"""
    for state, city in state_city:
        print(f"{state.name}: ({city.id}) {city.name}")
