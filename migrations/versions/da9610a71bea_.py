"""empty message

Revision ID: da9610a71bea
Revises: 
Create Date: 2016-11-22 11:44:00.790572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da9610a71bea'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('class_in_session', sa.Boolean(), nullable=True),
    sa.Column('class_start_time', sa.DateTime(), nullable=True),
    sa.Column('class_end_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TrackStudent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('check_in_time', sa.DateTime(), nullable=True),
    sa.Column('check_out_time', sa.DateTime(), nullable=True),
    sa.Column('reason', sa.String(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TrackStudent')
    op.drop_table('student')
    op.drop_table('class')
    ### end Alembic commands ###