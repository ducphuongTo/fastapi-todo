"""Company schema"""
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from app.models.company import CompanyMode

class CompanyView(BaseModel):
    """Company Class"""
    company_id: UUID
    name: str
    description: Optional[str] = None
    mode: CompanyMode = Field(default=CompanyMode.Active)
    rating: Optional[int] = Field(default=0, ge=0, le=5)

    class Config:
        orm_mode = True

class CompanyModel(BaseModel):
    name: str = Field(max_length=255)
    description: Optional[str] = Field(default=None)
    mode: Optional[CompanyMode] = Field(default=CompanyMode.Active)
    rating: Optional[int] = Field(default=0, ge=0, le=5)
