"""Update solutions.status

Revision ID: 0bc1aeea3c4d
Revises: 6fd9190f21c5
Create Date: 2023-12-10 18:42:29.839235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bc1aeea3c4d'
down_revision: Union[str, None] = '6fd9190f21c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solutions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('changed_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('code_url', sa.String(), nullable=False),
    sa.Column('language', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('testing_task_id', sa.Integer(), nullable=True),
    sa.Column('correct', sa.Boolean(), nullable=True),
    sa.Column('incorrect_log', sa.String(), nullable=True),
    sa.Column('extra_params', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('solutions')
    # ### end Alembic commands ###
