"""Merge heads

Revision ID: bea882768f02
Revises: 368a3122c2f8, 82f5839296a0
Create Date: 2024-06-09 15:15:07.099942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bea882768f02'
down_revision: Union[str, None] = ('368a3122c2f8', '82f5839296a0')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
