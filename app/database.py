"""database config"""
from app.setting import Settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


def get_db_context():
    """get context"""
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()

engine = create_engine(Settings.SQLALCHEMY_DB_URL)
LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
