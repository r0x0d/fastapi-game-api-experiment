"""add players table.

Revision ID: 23800d534c41
Revises: a0f9352b5811
Create Date: 2022-10-28 22:24:33.022942

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "23800d534c41"
down_revision = "a0f9352b5811"
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
        sa.Column("is_alive", sa.Boolean(), nullable=False, default=True),
        sa.Column(
            "dungeon_id",
            UUID(as_uuid=True),
            sa.ForeignKey("dungeons.id"),
            nullable=False,
        ),
        sa.Column(
            "vocation_id",
            UUID(as_uuid=True),
            sa.ForeignKey("vocations.id"),
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
    op.create_table("players", *columns)


def downgrade() -> None:
    op.drop_table("players")
