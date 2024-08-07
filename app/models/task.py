"""Task model"""
import uuid
from sqlalchemy import Column, String, Uuid, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.models.data_enum import TaskStatus, TaskPriority
from app.database import Base

class Task(Base):
    """Task class"""
    __tablename__ = 'task'
    task_id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    summary = Column(String, unique=False, nullable=True)
    description = Column(String, unique=False, nullable=True)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.NotStarted)
    priority = Column(Enum(TaskPriority), nullable=False, default=TaskPriority.LowPriority)
    user_id = Column(Uuid, ForeignKey("user.user_id"), nullable=True)
    user = relationship("User", back_populates="task")
