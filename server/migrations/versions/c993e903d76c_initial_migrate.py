"""initial migrate

Revision ID: c993e903d76c
Revises: 
Create Date: 2023-11-28 19:37:19.221138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c993e903d76c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aircrafts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aircraft_type', sa.String(), nullable=True),
    sa.Column('ident', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=3), nullable=True),
    sa.Column('password', sa.String(length=3), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('aircraft_id', sa.Integer(), nullable=True),
    sa.Column('from_to', sa.Text(), nullable=True),
    sa.Column('total_duration', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['aircraft_id'], ['aircrafts.id'], name=op.f('fk_logs_aircraft_id_aircrafts')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_logs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logs')
    op.drop_table('users')
    op.drop_table('aircrafts')
    # ### end Alembic commands ###
