#!/usr/bin/python3
"""
This module contains an example model class that demonstrates how to create
SQLAlchemy models using the base model class.
"""

from sqlalchemy import Column, Integer, String
from models.base import Base, BaseModel

class Example(Base, BaseModel):
    """
    Example model class that represents a simple entity in the database.
    This class demonstrates the basic structure of a SQLAlchemy model.
    """
    
    __tablename__ = 'examples'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Example instance.
        
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs) 