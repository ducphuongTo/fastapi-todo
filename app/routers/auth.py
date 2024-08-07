"""Auth routers"""
from app.constants.routers import ROUTE_AUTH, ROUTE_TOKEN
from app.database import get_db_context
from app.services.auth_services import AuthService
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(prefix=ROUTE_AUTH, tags=['Auth'])
auth_service = AuthService()

@router.post(ROUTE_TOKEN)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db_context)
    ):
    """login for access token"""
    user = auth_service.get_login_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return auth_service.create_access_token(user)
