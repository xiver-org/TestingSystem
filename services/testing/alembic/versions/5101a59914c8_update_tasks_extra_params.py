"""Update tasks.extra_params

Revision ID: 5101a59914c8
Revises: d8ae369ec3bd
Create Date: 2023-12-09 18:36:14.412506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5101a59914c8'
down_revision: Union[str, None] = 'd8ae369ec3bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'extra_params',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'extra_params',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    # ### end Alembic commands ###