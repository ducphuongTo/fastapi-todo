from typing import List, Optional
from uuid import UUID

from fastapi import Query
from sqlalchemy import and_, select
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BooleanClauseList
from models.data_enum import TaskPriority, TaskStatus
from models.task import Task
from schemas.task import TaskCreate, TaskUpdate, TaskView
from services.exceptionService import ExceptionService
from models.users import User

class TaskService:
    def __init__(self):
        self.task_model = Task
        self.exception_service = ExceptionService()

    def get_all_tasks(self, db: Session):
        return db.query(self.task_model).all()

    def create_new_task(self, task: TaskCreate, db: Session) -> TaskView | None:
        if task.user_id:
            user = db.query(User).filter(User.id == task.user_id).first()
            if not user:
                raise ValueError("User ID does not exist")

        new_task = self.task_model(
            summary=task.summary,
            description=task.description,
            status=task.status,
            priority=task.priority,
            user_id=task.user_id
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task

    def update_task_by_task_id(
        self, task_request: TaskUpdate, uuid: UUID, db: Session
    ) -> TaskView | None:
        task = db.query(self.task_model).filter(self.task_model.id == uuid).first()

        for key, value in task_request.dict(exclude_unset=True).items():
            setattr(task, key, value)

        task.save(db)

        return task

    def delete_task(self, uuid: UUID, db: Session) -> None:
        task = db.query(self.task_model).filter(self.task_model.id == uuid).first()
        if not task:
            raise self.exception_service.NotFoundException(self.task_model)
        db.delete(task)
        db.commit()
