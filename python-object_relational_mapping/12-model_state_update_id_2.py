#!/usr/bin/python3
"""
This script change the name of a State object
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

    new_mex = session.query(State).filter(State.id==2).first()
    new_mex.name = 'New Mexico'

    session.add(new_mex)
    session.commit()