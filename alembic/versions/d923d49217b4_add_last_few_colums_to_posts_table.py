"""add last few colums to posts table

Revision ID: d923d49217b4
Revises: cff71fa59377
Create Date: 2022-09-02 10:43:52.692327

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd923d49217b4'
down_revision = 'cff71fa59377'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),
        op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
            timezone=True), nullable=False, server_default=sa.text('NOW()')),))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

    pass
