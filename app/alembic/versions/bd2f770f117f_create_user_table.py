"""create_user_table

Revision ID: bd2f770f117f
Revises: 2d794836d9bd
Create Date: 2024-07-06 22:50:09.631132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
# revision identifiers, used by Alembic.
revision: str = 'bd2f770f117f'
down_revision: Union[str, None] = '2d794836d9bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column(
            "user_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
        ),
        sa.Column("email", sa.String, unique=True, nullable=False, index=True),
        sa.Column("username", sa.String, unique=True, nullable=False, index=True),
        sa.Column("first_name", sa.String, nullable=True),
        sa.Column("last_name", sa.String, nullable=True),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, default=False),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column(
            "created_at", sa.DateTime(), nullable=True, default=datetime.utcnow()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=True, onupdate=datetime.utcnow()
        ),
        sa.Column(
            "company_id", UUID(as_uuid=True), sa.ForeignKey("company.company_id"), nullable=True
        ),
    )



def downgrade() -> None:
    op.drop_table("user")
