#!/usr/bin/python3
"""
Adds State 'Louisiana' to the database hbtn_0e_6_usa
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)
