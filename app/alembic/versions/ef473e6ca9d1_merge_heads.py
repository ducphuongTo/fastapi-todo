"""Merge heads

Revision ID: ef473e6ca9d1
Revises: 72612e02b9b9, c61b744f757d
Create Date: 2024-06-07 17:43:04.387852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef473e6ca9d1'
down_revision: Union[str, None] = ('72612e02b9b9', 'c61b744f757d')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
