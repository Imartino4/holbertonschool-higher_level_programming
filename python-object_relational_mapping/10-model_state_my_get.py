#!/usr/bin/python3
"""
This script print the id of State object passed as argument
from db hbtn0e_6_usa 
user | password | database state name must be given as argv
SQL injection free
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

    try:
        state = session.query(State).filter(
                State.name = argv[4]).one()

        print(f"{s.id}")

    except NoResultFound as err:
		print("Not found")

