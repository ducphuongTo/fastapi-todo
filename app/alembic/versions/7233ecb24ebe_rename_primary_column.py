"""rename primary column

Revision ID: 7233ecb24ebe
Revises: bea882768f02
Create Date: 2024-06-09 15:15:10.638808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7233ecb24ebe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('task', 'id', new_column_name='task_id')
    op.alter_column('user', 'id', new_column_name='user_id')
    op.alter_column('company', 'id', new_column_name='company_id')


def downgrade() -> None:
    op.alter_column('task', 'id', new_column_name='task_id')
    op.alter_column('user', 'id', new_column_name='user_id')
    op.alter_column('company', 'id', new_column_name='company_id')
