#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
             f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
             pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session='fetch')

    session.commit()
