import pymysql
from sqlalchemy.orm import declarative_base

from . import DB_HOST, DB_PORT, DB_NAME, DB_PASS, DB_USER

Base = declarative_base()


# Create the database if it doesn't exist
def create_database() -> None:
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")
    finally:
        conn.close()
