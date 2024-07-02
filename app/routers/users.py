from fastapi import APIRouter, Depends, HTTPException
from app.constants.routers import ROUTE_USER, ROUTE_CREATE, ROUTE_GET_BY_ID, ROUTE_UPDATE_BY_ID, ROUTE_DELETE_BY_ID
from sqlalchemy.orm import Session
from app.schemas.users import UserView, UserModel, UserUpdateInformation
from app.models.users import User
from starlette import status
from app.database import get_db_context
from app.services.user_service import UserSerivce
from uuid import UUID

router = APIRouter(prefix=ROUTE_USER, tags=["User"])
user_service = UserSerivce()


@router.get("", response_model=list[UserView])
async def get_all_users( db: Session=Depends(get_db_context)):
    return db.query(User).all()

@router.post(ROUTE_CREATE, response_model=UserView, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserModel,  db: Session=Depends(get_db_context)) -> UserView:
    try:
        user = user_service.create_new_user(user, db)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.put(ROUTE_UPDATE_BY_ID, response_model=UserView)
async def update_user(request: UserUpdateInformation, user_id: UUID, db: Session=Depends(get_db_context)):
    try:
        result = user_service.update_user(request, user_id, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(ROUTE_DELETE_BY_ID)
def delete_user(uuid: UUID, db: Session=Depends(get_db_context)) -> None:
    user_service.delete_user(uuid, db)