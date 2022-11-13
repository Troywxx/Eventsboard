"""20221113init the program

Revision ID: 5bdea59838e9
Revises: 
Create Date: 2022-11-13 18:19:24.936000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bdea59838e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zb_jdevice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('devicename', sa.String(length=255), nullable=True),
    sa.Column('info', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('zb_jdevice')
    # ### end Alembic commands ###