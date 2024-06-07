"""Add new fields to Company model

Revision ID: 7934cc952d8d
Revises: 116e9337de0b
Create Date: 2024-06-07 11:39:29.571503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
# revision identifiers, used by Alembic.
revision: str = '7934cc952d8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "task",
        sa.Column(
            "user_id", UUID(as_uuid=True), sa.ForeignKey("company.id"), nullable=True
        ),
    )


def downgrade() -> None:
    pass
