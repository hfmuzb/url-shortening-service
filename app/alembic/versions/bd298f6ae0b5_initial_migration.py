"""initial_migration

Revision ID: bd298f6ae0b5
Revises: 
Create Date: 2023-01-21 19:25:33.041913

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bd298f6ae0b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('original_url', sa.String(), nullable=True),
    sa.Column('shortened_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DATE(), nullable=True),
    sa.Column('valid_days', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###
