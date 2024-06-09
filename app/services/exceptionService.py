from fastapi import HTTPException
from starlette import status

from constants.constants import (
    AuthConstants,
    DetailExceptionConstants
)

class ExceptionService:
    class NotFoundException(HTTPException):
        def __init__(self, table_name: str) -> None:
            super().__init__(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=DetailExceptionConstants.RECORD_NOT_FOUND.replace(
                    "{Record}", table_name
                ),
            )
    class InvalidCredential(HTTPException):
        def __init__(self):
            super().__init__(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=AuthConstants.INVALID_CREDENTIAL,
            )