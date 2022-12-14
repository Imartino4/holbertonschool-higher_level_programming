#!/usr/bin/python3
"""
This script print the first State object from db hbtn0e_6_usa
user | password | database must be given as argv
Not allowed to fetch all states before display results
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

    state = session.query(State).filter(State.id == 1).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
