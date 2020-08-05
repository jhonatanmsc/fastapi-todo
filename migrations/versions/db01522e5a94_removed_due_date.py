"""removed due date

Revision ID: db01522e5a94
Revises: d9d0ad724ab2
Create Date: 2020-08-04 11:28:46.579835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db01522e5a94'
down_revision = 'd9d0ad724ab2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'due_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('due_date', sa.DATE(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###