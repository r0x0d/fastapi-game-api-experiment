"""add dungeon difficulties table.

Revision ID: 105b44e2cd80
Revises: dc8743764847
Create Date: 2022-10-28 21:23:59.754318

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "105b44e2cd80"
down_revision = "dc8743764847"
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
        sa.Column(
            "level",
            sa.String(length=100),
            nullable=False,
            default="easy",
        ),
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
    op.create_table("dungeon_difficulties", *columns)


def downgrade() -> None:
    op.drop_table("dungeon_difficulties")
