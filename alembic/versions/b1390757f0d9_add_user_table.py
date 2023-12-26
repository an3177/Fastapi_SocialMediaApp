"""add user table

Revision ID: b1390757f0d9
Revises: 87fc7c0da73f
Create Date: 2023-12-26 11:06:19.888905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1390757f0d9'
down_revision: Union[str, None] = '87fc7c0da73f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
