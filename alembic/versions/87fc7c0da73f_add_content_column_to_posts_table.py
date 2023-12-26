"""add content column to posts table

Revision ID: 87fc7c0da73f
Revises: db635977e0f5
Create Date: 2023-12-26 10:20:33.729105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87fc7c0da73f'
down_revision: Union[str, None] = 'db635977e0f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
