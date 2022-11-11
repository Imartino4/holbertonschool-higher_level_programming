"""
This file contains the class definition of State and an instance
Base
Using SQLAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

""" Conectar database con aplicación
    user | password | database_name 
"""
engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    