"""User routers"""
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.constants.routers import ROUTE_USER, ROUTE_CREATE, ROUTE_UPDATE_BY_ID, ROUTE_DELETE_BY_ID
from app.schemas.users import UserView, UserModel, UserUpdateInformation
from app.models.users import User
from app.database import get_db_context
from app.services.user_service import UserSerivce

router = APIRouter(prefix=ROUTE_USER, tags=["User"])
user_service = UserSerivce()

@router.get("", response_model=list[UserView])
async def get_all_users( db: Session=Depends(get_db_context)):
    """Get all Users"""
    return db.query(User).all()

@router.post(ROUTE_CREATE, response_model=UserView, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserModel,  db: Session=Depends(get_db_context)) -> UserView:
    """Create User"""
    try:
        user = user_service.create_new_user(user, db)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
@router.put(ROUTE_UPDATE_BY_ID, response_model=UserView)
async def update_user(request: UserUpdateInformation, user_id: UUID, db: Session=Depends(get_db_context)):
    """Update User"""
    try:
        result = user_service.update_user(request, user_id, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete(ROUTE_DELETE_BY_ID)
def delete_user(uuid: UUID, db: Session=Depends(get_db_context)) -> None:
    """Delete User"""
    user_service.delete_user(uuid, db)
