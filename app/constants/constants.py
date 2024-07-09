"""Constant"""
class AuthConstants:
    """Auth Constant"""
    BEARER_TOKEN_TYPE: str = "bearer"
    INVALID_OR_EXPIRED_TOKEN: str = "Invalid or Expired token"
    INVALID_CREDENTIAL: str = "Invalid credential"


class DetailExceptionConstants:
    """Exception constant"""
    INTERNAL_SERVER_ERROR: str = "Internal server error"
    FIELD_ALREADY_EXISTS: str = "{Field} already exists"
    FIELD_NOT_EXISTS: str = "{Field} not exists"
    RECORD_NOT_FOUND: str = "{Record} not found"
