"""Renaming students to scholars

Revision ID: f4736da5709f
Revises: 791279dd0760
Create Date: 2023-12-09 13:50:16.445004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4736da5709f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
