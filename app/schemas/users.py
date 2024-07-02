from typing import Optional
from uuid import UUID
from app.schemas.company import CompanyView
from pydantic import ConfigDict, BaseModel, EmailStr, Field, validator
import re

class UserView(BaseModel):
    user_id: UUID
    email: EmailStr
    username: str
    is_admin: bool
    is_active: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company: Optional[CompanyView] = None

    class Config:
        orm_mode = True
        


class UserBaseAuth(BaseModel):
    password: str = Field(alias="new_password")
    re_password: str

    class Config(ConfigDict):
        allow_population_by_field_name = True

    @validator("password")
    def verify_password_strength(cls, value):
        pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$"

        if not re.match(pattern, value):
            raise ValueError("Password is not strong enough, please check again")

        return value

    @validator("re_password")
    def verify_password_match(cls, value, values):
        if "password" in values and value != values["password"]:
            raise ValueError("Passwords do not match, please check again")

        return value

class UserModel(UserBaseAuth):
    email: EmailStr
    username: str
    first_name: Optional[str] = Field(default=None, max_length=255)
    last_name: Optional[str] = Field(default=None, max_length=255)
    is_active: Optional[bool]
    is_admin: Optional[bool]
    company_id: Optional[UUID] = None
    
class UserBaseInformation(BaseModel):
    first_name: Optional[str] = Field(default=None, max_length=255)
    last_name: Optional[str] = Field(default=None, max_length=255)
    is_active: Optional[bool]
    is_admin: Optional[bool]
    company_id: Optional[UUID] = None

class UserUpdateInformation(UserBaseInformation):
    email: Optional[EmailStr] = None
    username: Optional[str] = None