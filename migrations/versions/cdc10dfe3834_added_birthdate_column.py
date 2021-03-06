"""added birthdate column

Revision ID: cdc10dfe3834
Revises: 03fb8041e4f6
Create Date: 2021-03-04 11:54:25.742463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdc10dfe3834'
down_revision = '03fb8041e4f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###
