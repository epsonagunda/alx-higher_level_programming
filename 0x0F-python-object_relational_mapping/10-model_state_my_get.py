#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # start a Session
    session = Session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).filter(State.name == argv[4]).first()

    if s_tate:
        print("{}".format(s_tate.id))
    else:
        print("Not found")
    session.close()
