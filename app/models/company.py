import uuid
from sqlalchemy import Column, String, Uuid, Enum, SmallInteger
from sqlalchemy.orm import relationship
from models.data_enum import CompanyMode
from database import Base

class Company(Base):
    __tablename__ = 'company'
    
    company_id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, unique=False, nullable=True)
    mode = Column(Enum(CompanyMode), nullable=False, default=CompanyMode.Active)
    rating = Column(SmallInteger, default=0)
    user = relationship("User", back_populates="company")