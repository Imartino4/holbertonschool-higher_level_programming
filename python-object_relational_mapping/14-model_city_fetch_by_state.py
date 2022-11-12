#!/usr/bin/python3
"""
This script print all City objects from hbtn_0e_14_usa database
username, password and db name must be given as argv arguments
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state_city = session.query(City, State).order_by(City.id)
    for s in state_city:
        print(s)
