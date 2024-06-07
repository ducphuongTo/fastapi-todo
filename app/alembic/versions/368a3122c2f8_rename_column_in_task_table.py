"""Rename column in task table

Revision ID: 368a3122c2f8
Revises: ef473e6ca9d1
Create Date: 2024-06-07 17:43:11.240509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '368a3122c2f8'
down_revision: Union[str, None] = 'ef473e6ca9d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('task', 'staus', new_column_name='status')

def downgrade():
    op.alter_column('task', 'status', new_column_name='staus')
