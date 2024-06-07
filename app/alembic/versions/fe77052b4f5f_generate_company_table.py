"""generate company table

Revision ID: fe77052b4f5f
Revises: 97adb7c305b9
Create Date: 2024-06-06 16:33:43.474956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models.data_enum import CompanyMode
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
# revision identifiers, used by Alembic.
revision: str = 'fe77052b4f5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    company_table = op.create_table(
        'company',
        sa.Column(
            "id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
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
    
    op.bulk_insert(
        company_table,
        [
            {
                "id": uuid.uuid4(),
                "name": "ToDo Company",
                "description": "ToDo Company Description",
                "mode": CompanyMode.Active,
                "rating": 5,
            }
        ],
    )
    


def downgrade() -> None:
    op.drop_table("company")
    op.execute("DROP TYPE mode;")
