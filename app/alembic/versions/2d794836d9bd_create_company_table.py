"""create_company_table

Revision ID: 2d794836d9bd
Revises: 
Create Date: 2024-07-06 22:45:36.207243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from models.data_enum import CompanyMode
# revision identifiers, used by Alembic.
revision: str = '2d794836d9bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'company',
        sa.Column(
            "company_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
        ),
	sa.Column(
            "user_id", UUID(as_uuid=True), sa.ForeignKey("company.company_id"), nullable=True
        ),
        sa.Column("name", sa.String, unique=True, nullable=False, index=True),
        sa.Column("description", sa.String, unique=True, nullable=False, index=True),
        sa.Column(
            "mode", sa.Enum(CompanyMode), nullable=False, default=CompanyMode.Active
        ),
        sa.Column("rating", sa.SmallInteger, default=0),
        sa.Column(
            "created_at", sa.DateTime(), nullable=True, default=datetime.utcnow()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=True, onupdate=datetime.utcnow()
        )
    )



def downgrade() -> None:
    op.drop_table("company")
