"""Add uselist=False to CourseData

Revision ID: c9ac63181d93
Revises: 664c9a819916
Create Date: 2023-11-29 18:16:03.141731

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9ac63181d93'
down_revision: Union[str, None] = '664c9a819916'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses_data', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses_data', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###