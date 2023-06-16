from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

import time


DATABASE_URL = 'postgresql://SVN_Admin:SVN_logistics_2022@db:5432/SVN'


def wait_for_db(db_uri = DATABASE_URL):
    """checks if database connection is established"""

    _local_engine = create_engine(db_uri)

    _LocalSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=_local_engine
    )

    up = False
    while not up:
        try:
            # Try to create session to check if DB is awake
            db_session = _LocalSessionLocal()
            # try some basic query
            db_session.execute(text("SELECT 1"))
            db_session.commit()
        except Exception as err:
            print(f"Connection error: {err}")
            up = False
        else:
            up = True
        
        time.sleep(2)

wait_for_db()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()