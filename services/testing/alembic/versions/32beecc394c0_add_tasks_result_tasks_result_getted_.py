"""Add tasks.result & tasks.result_getted_time

Revision ID: 32beecc394c0
Revises: 41881385697e
Create Date: 2023-12-07 14:47:37.157983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32beecc394c0'
down_revision: Union[str, None] = '41881385697e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('result', sa.String(), nullable=True))
    op.add_column('tasks', sa.Column('result_getted_time', sa.TIMESTAMP(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'result_getted_time')
    op.drop_column('tasks', 'result')
    # ### end Alembic commands ###
