"""generate task table

Revision ID: 619dbbccaebf
Revises: fe77052b4f5f
Create Date: 2024-06-06 16:47:51.943411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models.data_enum import TaskPriority, TaskStatus
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
# revision identifiers, used by Alembic.
revision: str = '619dbbccaebf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    task_table = op.create_table(
        'task',
        sa.Column(
            "id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
        ),
        sa.Column("summary", sa.String, unique=True, nullable=False, index=True),
        sa.Column("description", sa.String, unique=True, nullable=False, index=True),
        sa.Column(
            "staus", sa.Enum(TaskStatus), nullable=False, default=TaskStatus.NotStarted
        ),
        sa.Column(
            "priority", sa.Enum(TaskPriority), nullable=False, default=TaskPriority.LowPriority
        ),
        sa.Column(
            "created_at", sa.DateTime(), nullable=True, default=datetime.utcnow()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=True, onupdate=datetime.utcnow()
        )
    )

def downgrade() -> None:
    op.drop_table("task")
    op.execute("DROP TYPE status;")
    op.execute("DROP TYPE priority;")

