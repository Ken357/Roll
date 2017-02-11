"""empty message

Revision ID: 8836a45e634a
Revises: 3fff990fdb04
Create Date: 2017-01-10 23:15:54.232000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8836a45e634a'
down_revision = '3fff990fdb04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'students_email_key', 'students', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'students_email_key', 'students', ['email'])
    # ### end Alembic commands ###
