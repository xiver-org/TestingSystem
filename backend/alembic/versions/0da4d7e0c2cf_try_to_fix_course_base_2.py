"""Try to fix course base 2

Revision ID: 0da4d7e0c2cf
Revises: 9f2c696a8a7d
Create Date: 2023-11-26 21:50:21.208877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0da4d7e0c2cf'
down_revision: Union[str, None] = '9f2c696a8a7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('courses_course_data_fkey', 'courses', type_='foreignkey')
    op.drop_column('courses', 'course_data')
    op.add_column('courses_data', sa.Column('course_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'courses_data', 'courses', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'courses_data', type_='foreignkey')
    op.drop_column('courses_data', 'course_id')
    op.add_column('courses', sa.Column('course_data', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('courses_course_data_fkey', 'courses', 'courses_data', ['course_data'], ['id'])
    # ### end Alembic commands ###