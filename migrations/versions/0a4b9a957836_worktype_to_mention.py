"""+ worktype to Mention

Revision ID: 0a4b9a957836
Revises: a8ba7e4d38bf
Create Date: 2022-11-14 22:07:02.674000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a4b9a957836'
down_revision = 'a8ba7e4d38bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mention', sa.Column('worktype', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mention', 'worktype')
    # ### end Alembic commands ###
