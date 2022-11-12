#!/usr/bin/python3
"""
This script add State object Louisiana to the database hbtn0e_6_usa 
user | password | database must be given as argv
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
    
    Louisiana = State(name='Louisiana')
    
    session.add(Louisiana)
    session.commit()
    
    print(f"{Louisiana.id}")
