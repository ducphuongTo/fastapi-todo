"""Merge heads

Revision ID: c61b744f757d
Revises: 116e9337de0b, 7934cc952d8d
Create Date: 2024-06-07 11:43:02.238899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c61b744f757d'
down_revision: Union[str, None] = ('116e9337de0b', '7934cc952d8d')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
