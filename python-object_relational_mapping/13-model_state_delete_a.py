#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter a
from db hbtn0e_6_usa
user | password | database must be given as argv
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

session.query(State).filter(
        State.name.contains("a")).delete()
session.commit()
