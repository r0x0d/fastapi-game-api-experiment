"""add spell range types table

Revision ID: 1ce1c2b396e4
Revises: cb4455d1fe66
Create Date: 2022-10-25 20:13:32.703506

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "1ce1c2b396e4"
down_revision = "cb4455d1fe66"
branch_labels = None
depends_on = None


def upgrade() -> None:
    columns = [
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
        ),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            default=datetime.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            default=datetime.now(),
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(), default=None, nullable=True),
    ]
    op.create_table("spell_range_types", *columns)


def downgrade() -> None:
    op.drop_table("spell_range_types")
