"""add races table.

Revision ID: 473845e5b331
Revises: 47f45d3c3177
Create Date: 2022-10-27 21:39:50.058396

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "473845e5b331"
down_revision = "47f45d3c3177"
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
            "size_id",
            UUID(as_uuid=True),
            sa.ForeignKey("sizes.id"),
            nullable=False,
        ),
        sa.Column(
            "aligment_id",
            UUID(as_uuid=True),
            sa.ForeignKey("aligments.id"),
            nullable=False,
        ),
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
    op.create_table("races", *columns)


def downgrade() -> None:
    op.drop_table("races")
