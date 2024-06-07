from passlib.context import CryptContext
from constants.constants import AuthConstants
from services.exceptionService import ExceptionService

class AuthService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.token_type = AuthConstants.BEARER_TOKEN_TYPE
        self.exception_service = ExceptionService
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)