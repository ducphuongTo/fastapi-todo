"""Task Router"""
from fastapi import APIRouter, Depends, HTTPException
from constants.routers import (
    ROUTE_TASK,
    ROUTE_CREATE,
    ROUTE_UPDATE_BY_ID,
    ROUTE_DELETE_BY_ID
)
from sqlalchemy.orm import Session
from starlette import status
from uuid import UUID
from schemas.task import TaskCreate, TaskUpdate, TaskView
from services.task_service import TaskService
from database import get_db_context
from models.users import User
from services.auth_services import AuthService

router = APIRouter(prefix=ROUTE_TASK, tags=["Task"])
task_service = TaskService()
auth_service = AuthService()

@router.get("")
async def get_all_task(user: User = Depends(auth_service.token_interceptor), db: Session=Depends(get_db_context)):
    """Get all task"""
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin reuiqred")
    return task_service.get_all_tasks(db)

@router.post(ROUTE_CREATE, response_model=TaskView, status_code=status.HTTP_201_CREATED)
async def create_new_task(request: TaskCreate, db: Session=Depends(get_db_context)):
    """Create new Task"""
    try:
        result = task_service.create_new_task(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.put(ROUTE_UPDATE_BY_ID, response_model=TaskView)
async def update_task(
        request: TaskUpdate,
        TaskService_id: UUID,
        db: Session=Depends(get_db_context)
    ):
    """Update Task"""
    try:
        result = task_service.update_task_by_task_id(request, TaskService_id, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete(ROUTE_DELETE_BY_ID)
def delete_task(uuid: UUID, db: Session=Depends(get_db_context)) -> None:
    """Delete Task"""
    try:
        task_service.delete_task(uuid, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
