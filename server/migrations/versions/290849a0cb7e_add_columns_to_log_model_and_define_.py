"""add columns to Log model and define Aircraft model

Revision ID: 290849a0cb7e
Revises: c993e903d76c
Create Date: 2023-11-29 14:30:26.306560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290849a0cb7e'
down_revision = 'c993e903d76c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('remarks_and_endorsements', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('takeoffs', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('landings', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('single_engine_land', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('multi_engine_land', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('night', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('actual_instrument', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('simulated_instrument', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('cross_country', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('flight_instructor', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('dual_received', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('pilot_in_command', sa.Float(), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    with op.batch_alter_table('logs', schema=None) as batch_op:
        batch_op.drop_column('pilot_in_command')
        batch_op.drop_column('dual_received')
        batch_op.drop_column('flight_instructor')
        batch_op.drop_column('cross_country')
        batch_op.drop_column('simulated_instrument')
        batch_op.drop_column('actual_instrument')
        batch_op.drop_column('night')
        batch_op.drop_column('multi_engine_land')
        batch_op.drop_column('single_engine_land')
        batch_op.drop_column('landings')
        batch_op.drop_column('takeoffs')
        batch_op.drop_column('remarks_and_endorsements')
        batch_op.drop_column('date')

    # ### end Alembic commands ###
