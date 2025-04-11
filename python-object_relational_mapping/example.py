#!/usr/bin/python3
"""
This script demonstrates how to use the SQLAlchemy models to interact with a MySQL database.
It shows basic CRUD operations and database connection setup.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.example import Example

def main():
    """
    Main function that demonstrates basic database operations.
    Creates a new database connection, creates tables, and performs some example operations.
    """
    # Create engine and connect to database
    engine = create_engine('mysql+mysqldb://root:root@localhost:3306/example_db')
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Create a new example
        example = Example(name="Test Example", description="This is a test example")
        session.add(example)
        session.commit()
        
        # Query the example
        result = session.query(Example).filter_by(name="Test Example").first()
        print(f"Found example: {result.to_dict()}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main() 