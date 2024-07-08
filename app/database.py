from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from setting import Settings
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
def get_db_context():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()
def get_record_by_id(self, uuid: UUID, model, db: Session):
        record = db.query(model).filter(model.id == uuid).first()

        if not record:
            raise HTTPException(status_code=500, detail="Record not found!")

        return record

engine = create_engine(Settings.SQLALCHEMY_DB_URL)
MetaData().create_all(engine)
LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()