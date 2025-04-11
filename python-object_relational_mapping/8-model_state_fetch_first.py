#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query first state
    state = session.query(State).order_by(State.id).first()

    # Print result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close session
    session.close() 