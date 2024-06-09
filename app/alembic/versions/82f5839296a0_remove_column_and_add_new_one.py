"""remove column and add new one

Revision ID: 82f5839296a0
Revises: 368a3122c2f8
Create Date: 2024-06-09 14:31:26.116903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '82f5839296a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('task', 'user_id')
    op.add_column(
        "task",
        sa.Column(
            "user_id", UUID(as_uuid=True), sa.ForeignKey("user.id"), nullable=True
        ),
    )


def downgrade() -> None:
    pass
