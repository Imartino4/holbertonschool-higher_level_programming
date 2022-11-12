#!/usr/bin/python3
"""
This file contains the class definition of City
Using SQLAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Citiy(Base):
    """City class/table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id(Integer, ForeignKey('state.id'))
