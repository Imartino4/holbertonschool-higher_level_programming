"""
This script print the first State object from db hbtn0e_6_usa
user | password | database must be given as argv
Not allowed to fetch all states before display results
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(engine)
    session = Session()
    
    user = session.query(State).filter(states.id == 1).first()
    
    if user:
        print(f"{states.id}: {states.name}")
    else:
        print(Nothing)
        