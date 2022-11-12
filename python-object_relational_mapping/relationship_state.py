#!/usr/bin/python3
"""
This file contains the class definition of State and an instance
Base
Using SQLAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State class/table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    """ backref para que el hijo sepa quien es el padre"""
    cities = relationship("City", backref='parent')
