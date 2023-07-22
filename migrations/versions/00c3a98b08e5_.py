"""empty message

Revision ID: 00c3a98b08e5
Revises: 27829d14272e
Create Date: 2023-07-22 10:35:17.559265

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '00c3a98b08e5'
down_revision = '27829d14272e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'formation_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'formation_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
