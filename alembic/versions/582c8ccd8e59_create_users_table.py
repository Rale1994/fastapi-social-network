"""create users table

Revision ID: 582c8ccd8e59
Revises: 2fd93b6e2b24
Create Date: 2022-09-01 19:33:10.604894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '582c8ccd8e59'
down_revision = '2fd93b6e2b24'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
