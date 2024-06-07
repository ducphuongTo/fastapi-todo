"""Merge heads

Revision ID: 116e9337de0b
Revises: 619dbbccaebf, 97adb7c305b9, fe77052b4f5f
Create Date: 2024-06-07 11:38:59.985630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '116e9337de0b'
down_revision: Union[str, None] = ('619dbbccaebf', '97adb7c305b9', 'fe77052b4f5f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
