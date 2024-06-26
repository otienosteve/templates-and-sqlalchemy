"""Add BioData Model

Revision ID: 579ed7677d6a
Revises: 2c52e184179e
Create Date: 2024-06-26 10:38:32.861447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579ed7677d6a'
down_revision = '2c52e184179e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bio_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hometown', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bio_data')
    # ### end Alembic commands ###
