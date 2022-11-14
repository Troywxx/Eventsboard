"""Mention init

Revision ID: 5a1f146db08e
Revises: 5bdea59838e9
Create Date: 2022-11-13 21:47:27.810000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a1f146db08e'
down_revision = '5bdea59838e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mention',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workname', sa.String(length=255), nullable=True),
    sa.Column('workcontent', sa.String(length=255), nullable=True),
    sa.Column('workinfo', sa.String(length=255), nullable=True),
    sa.Column('workstatus', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('zb_jdevice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zb_jdevice',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('devicename', sa.VARCHAR(length=255), nullable=True),
    sa.Column('info', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('mention')
    # ### end Alembic commands ###
