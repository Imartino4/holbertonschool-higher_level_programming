#!/usr/bin/python3
"""
This script list all State objects from 
database hbtn_0e_6_usa
username, password and db name must be given
as argv arguments
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    
    """Conecto db con la aplicacion"""
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    
    """Creo las tablas"""
    Base.metadata.create_all(engine)
    
    """Relacionar conexion y modelos"""
    Session = sessionmaker(engine)
    session = Session()
   
    """Consulto la base de datos"""
    states = session.query(State).order_by(State.id)
    for s in states:
        print(f"{s.id}: {s.name}")
