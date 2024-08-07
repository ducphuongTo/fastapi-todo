"""create_task_table

Revision ID: b858fa4bb7ae
Revises: bd2f770f117f
Create Date: 2024-07-06 22:53:00.644448

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.models.data_enum import TaskPriority, TaskStatus

# revision identifiers, used by Alembic.
revision: str = 'b858fa4bb7ae'
down_revision: Union[str, None] = 'bd2f770f117f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "task",
        sa.Column(
            "task_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
        ),
        sa.Column("summary", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column(
            "status", sa.Enum(TaskStatus), nullable=False, default=TaskStatus.NotStarted
        ),
        sa.Column("priority", sa.Enum(TaskPriority), nullable=True),
        sa.Column(
            "user_id", UUID(as_uuid=True), sa.ForeignKey("user.user_id"), nullable=True
        ),
        sa.Column(
                "created_at", sa.DateTime(), nullable=True, default=datetime.utcnow()
            ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=True, onupdate=datetime.utcnow()
        ),
    )



def downgrade() -> None:
    op.drop_table("task")
