#!/usr/bin/python3
"""
This module contains the City class definition for SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

class City(Base):
    """
    City class that represents a city in the database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False) 