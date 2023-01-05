"""Add aligments table.

Revision ID: faffe495bb96
Revises: 3952c0015b7e
Create Date: 2022-10-12 02:28:34.343134

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "faffe495bb96"
down_revision = "3952c0015b7e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    columns = [
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
        ),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String()),
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
    op.create_table("aligments", *columns)


def downgrade() -> None:
    op.drop_table("aligments")
