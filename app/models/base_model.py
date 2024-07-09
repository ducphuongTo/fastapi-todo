"""Base model"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Uuid
from sqlalchemy.orm import Session

class BaseModel:
    """Class base"""
    id = Column(Uuid, primary_key=True, default=uuid.uuid4, unique=True)
    created_at = Column(DateTime, nullable=True, default=datetime.utcnow().isoformat())
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow().isoformat())

    def save(self, db: Session):
        """Save model"""
        db.add(self)
        db.commit()
        db.refresh(self)

    def delete(self, db: Session):
        """Delete model"""
        db.delete(self)
        db.commit()
