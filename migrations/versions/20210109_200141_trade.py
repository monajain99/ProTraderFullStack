"""Trade

Revision ID: c899560c13fa
Revises: 69f2c4f81334
Create Date: 2021-01-09 20:01:41.454268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c899560c13fa'
down_revision = '69f2c4f81334'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('trades_ticker_key', 'trades', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('trades_ticker_key', 'trades', ['ticker'])
    # ### end Alembic commands ###
