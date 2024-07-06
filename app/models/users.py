import uuid
from sqlalchemy import Column, String, Uuid, Boolean, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from database import Base
class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    company_id = Column(Uuid, ForeignKey("company.company_id"), nullable=True)
    task = relationship("Task", back_populates="user")
    company = relationship("Company", back_populates="user")