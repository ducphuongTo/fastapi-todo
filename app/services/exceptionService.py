from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException
from starlette import status

from constants.constants import (
    AuthConstants,
    DetailExceptionConstants,
    UserMsgConstants,
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