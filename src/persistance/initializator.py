"""This module initializes the database by creating tables"""

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..domain.person import Person
from . import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from .creator import Base


def initialize_database() -> None:
    # Create an engine that connects to the newly created database
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    try:
        # Create all tables in the engine. This is equivalent to "Create Table"
        # statements in raw SQL.
        Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        Base.session = Session()
    except Exception as e:
        logging.error("Error while initializing the database: %s", e)
