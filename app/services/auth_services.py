from passlib.context import CryptContext
from constants.constants import AuthConstants
from services.exceptionService import ExceptionService
from sqlalchemy.orm import Session
from models.users import User
from services.exceptionService import ExceptionService
from typing import Optional
from datetime import timedelta, datetime
from jose import jwt, JWTError
from setting import Settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from starlette import status
import logging
logger = logging.getLogger(__name__)
oa2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")


class AuthService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.token_type = AuthConstants.BEARER_TOKEN_TYPE
        self.exception_service = ExceptionService

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def get_login_user(self, username: str, password: str, db: Session):

        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise self.exception_service.NotFoundException("User")
        if not self.verify_password(password, user.hashed_password):
            raise self.exception_service.InvalidCredential()
        return user
    
    def create_access_token(self, user: User, expires: Optional[timedelta] = None):
        
        expires = (
            datetime.utcnow() + expires
            if expires
            else datetime.utcnow()
            + timedelta(minutes=5)
        )
        claims = {
            "user_id": str(user.user_id),
            "email": user.email,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_admin": user.is_admin,
            "exp": expires,
        }
        
        token = jwt.encode(claims, Settings.JWT_SECRET, Settings.JWT_ALGORITHM)

        return {"access_token": token, "token_type": self.token_type}
    
    def token_interceptor(self, token: str = Depends(oa2_bearer)):
        try:
            payload = jwt.decode(token, Settings.JWT_SECRET, algorithms=[Settings.JWT_ALGORITHM])
            user = User()
            user.user_id = payload.get("user_id")
            user.email = payload.get("email")
            user.username = payload.get("username")
            user.first_name = payload.get("first_name")
            user.last_name = payload.get("last_name")
            user.is_admin = payload.get("is_admin")
            
            if user.username is None or user.id is None:
                self.token_exception
            return user
        except JWTError:
            self.token_exception

    def token_exception(self):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credential",
            headers={"WWW-Authenticate": self.token_type},
        )