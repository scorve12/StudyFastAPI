"""empty message

Revision ID: 9c264742209f
Revises: 9a1d81a7a4e2
Create Date: 2024-07-02 15:04:34.939172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c264742209f'
down_revision: Union[str, None] = '9a1d81a7a4e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('question_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'answer', 'question', ['question_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.drop_column('answer', 'question_id')
    # ### end Alembic commands ###
