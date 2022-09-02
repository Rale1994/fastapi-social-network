"""create content column

Revision ID: 2fd93b6e2b24
Revises: ce0353fda9de
Create Date: 2022-09-01 19:25:02.682642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd93b6e2b24'
down_revision = 'ce0353fda9de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
