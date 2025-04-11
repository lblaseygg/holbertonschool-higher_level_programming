#!/usr/bin/python3
"""
This module contains the base model class for SQLAlchemy models.
It provides common functionality and configuration for all models in the application.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BaseModel:
    """
    Base model class that provides common functionality for all models.
    This class serves as a foundation for all database models in the application.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize a new model instance.
        
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        
        Returns:
            dict: A dictionary representation of the model instance
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} 