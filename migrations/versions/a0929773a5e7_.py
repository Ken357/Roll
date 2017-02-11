"""empty message

Revision ID: a0929773a5e7
Revises: ab3a857687b6
Create Date: 2016-12-28 19:58:45.726000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0929773a5e7'
down_revision = 'ab3a857687b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'parents_child_id_fkey', 'parents', type_='foreignkey')
    op.drop_column('parents', 'child_id')
    op.add_column('students', sa.Column('group_id', sa.Integer(), nullable=True))
    op.add_column('students', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'students', 'group', ['group_id'], ['id'])
    op.create_foreign_key(None, 'students', 'parents', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_column('students', 'parent_id')
    op.drop_column('students', 'group_id')
    op.add_column('parents', sa.Column('child_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'parents_child_id_fkey', 'parents', 'students', ['child_id'], ['id'])
    # ### end Alembic commands ###
