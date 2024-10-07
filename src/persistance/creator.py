"""Module to create the database if it doesn't exist."""

import logging

import pymysql
from sqlalchemy.orm import DeclarativeBase

from . import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

class Base(DeclarativeBase):
    """Base class for the ORM."""
    pass


# Create the database if it doesn't exist
def create_database() -> None:
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        logging.info("Database %s created successfully.", DB_NAME)
    except Exception as e:
        logging.error("Error while creating the database: %s", e)
    finally:
        conn.close()
