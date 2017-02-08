"""empty message

Revision ID: 1a4075e3c316
Revises: b333ca011fea
Create Date: 2016-12-21 23:16:52.467000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a4075e3c316'
down_revision = 'b333ca011fea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.Column('telephone', sa.Integer(), nullable=True),
    sa.Column('email', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parents')
    # ### end Alembic commands ###
