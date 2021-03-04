"""password hashead

Revision ID: 5aa9c3b2413e
Revises: cdc10dfe3834
Create Date: 2021-03-04 14:48:44.337283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aa9c3b2413e'
down_revision = 'cdc10dfe3834'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('user', 'password')
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
