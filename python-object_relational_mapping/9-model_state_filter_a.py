#!/usr/bin/python3
"""List all State objects containing the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

