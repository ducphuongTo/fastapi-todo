"""generate table

Revision ID: 97adb7c305b9
Revises: 
Create Date: 2024-06-06 16:21:04.215068

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid
from services.auth_services import AuthService
from setting import settings
# revision identifiers, used by Alembic.
revision: str = '97adb7c305b9'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    user_table = op.create_table(
        "user",
        sa.Column(
            "id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True
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
            "company_id", UUID(as_uuid=True), sa.ForeignKey("company.id"), nullable=True
        )
    )
    
    op.bulk_insert(
        user_table,
        [
            {
                "id": uuid.uuid4(),
                "email": "phuong@gmail.com",
                "username": "phuong_admin",
                "first_name": "Phuong",
                "last_name": "To",
                "hashed_password": AuthService().get_password_hash(settings.ADMIN_DEFAULT_PASSWORD),
                "is_active": True,
                "is_admin": True,
            }
        ],
    )


def downgrade() -> None:
    op.drop_table("user")
