from fastapi import APIRouter, Depends, HTTPException
from constants.routers import ROUTE_TASK, ROUTE_CREATE, ROUTE_GET_BY_ID, ROUTE_UPDATE_BY_ID, ROUTE_DELETE_BY_ID
from services.dbServices import DatabaseService
from sqlalchemy.orm import Session
from schemas.task import TaskCreate, TaskPriority, TaskStatus, TaskUpdate, TaskView
from starlette import status
from services.task_service import TaskService
from uuid import UUID
from database import get_db_context

router = APIRouter(prefix=ROUTE_TASK, tags=["Task"])
dbService = DatabaseService()
task_service = TaskService()

@router.get("")
async def get_all_task(db: Session=Depends(get_db_context)):
    return task_service.get_all_tasks(db)

@router.post(ROUTE_CREATE, response_model=TaskView, status_code=status.HTTP_201_CREATED)
async def create_new_task(request: TaskCreate, db: Session=Depends(get_db_context)):
    try:
        result = task_service.create_new_task(request, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put(ROUTE_UPDATE_BY_ID, response_model=TaskView)
async def update_task(request: TaskUpdate, TaskService_id: UUID, db: Session=Depends(get_db_context)):
    result = task_service.update_task_by_task_id(request, TaskService_id, db)
    return result

@router.delete(ROUTE_DELETE_BY_ID)
def delete_task(uuid: UUID, db: Session=Depends(get_db_context)) -> None:
    task_service.delete_task(uuid, db)