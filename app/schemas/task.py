from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import Query
from pydantic import ConfigDict, BaseModel, Field

from models.data_enum import TaskPriority, TaskStatus

class TaskView(BaseModel):
    task_id: UUID
    summary: str
    description: Optional[str] = None
    status: TaskStatus = Field(default=TaskStatus.NotStarted)
    priority: TaskPriority = Field(default=None)
    user_id: Optional[UUID] = None

    class Config(ConfigDict):
        orm_mode = True

class TaskCreate(BaseModel):
    summary: str = Field(max_length=2000)
    description: Optional[str] = Field(default=None)
    status: TaskStatus = Field(default=TaskStatus.NotStarted)
    priority: Optional[TaskPriority] = Field(default=None)
    user_id: Optional[UUID] = None

    class Config(ConfigDict):
        schema_extra = {
            "example": {
                "summary": "New task",
                "description": "New task description",
                "status": TaskStatus.NotStarted.value,
                "priority": TaskPriority.LowPriority.value,
                "user_id": uuid4(),
            }
        }


class TaskUpdate(BaseModel):
    summary: Optional[str] = Field(default=None, max_length=2000)
    description: Optional[str] = Field(default=None)
    status: Optional[TaskStatus] = Field(default=None)
    priority: Optional[TaskPriority] = Field(default=None)
    user_id: Optional[UUID] = None

    class Config(ConfigDict):
        schema_extra = {
            "example": {
                "summary": "Update summary",
                "description": "Update description",
                "status": TaskStatus.InProgress.value,
                "priority": TaskPriority.MediumPriority.value,
                "user_id": uuid4(),
            }
        }
