"""Add new fields to table

Revision ID: 72612e02b9b9
Revises: c61b744f757d
Create Date: 2024-06-07 11:43:06.087570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '72612e02b9b9'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column(
        "company",
        sa.Column(
            "user_id", UUID(as_uuid=True), sa.ForeignKey("company.id"), nullable=True
        ),
    )


def downgrade() -> None:
    pass
