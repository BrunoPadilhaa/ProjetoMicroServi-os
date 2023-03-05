"""making changes

Revision ID: 7c679ad51a54
Revises: d650a6c80114
Create Date: 2023-03-01 10:38:15.359191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c679ad51a54'
down_revision = 'd650a6c80114'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('telemetryData',
    sa.Column('data_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('data_hora', sa.DateTime(), nullable=True),
    sa.Column('latitude', sa.Numeric(), nullable=True),
    sa.Column('longitude', sa.Numeric(), nullable=True),
    sa.Column('altimeter', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('data_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('telemetryData')
    # ### end Alembic commands ###
