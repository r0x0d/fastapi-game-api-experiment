"""add dungeon histories table

Revision ID: 8f12a0e9d6b9
Revises: fafbc5ff017f
Create Date: 2022-11-24 23:19:45.397742

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "8f12a0e9d6b9"
down_revision = "fafbc5ff017f"
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
        sa.Column("last_level", sa.Integer(), nullable=False),
        sa.Column("last_room", sa.Integer(), nullable=False),
        sa.Column("is_player_alive", sa.Boolean(), nullable=False),
        sa.Column("is_dungeon_complete", sa.Boolean(), nullable=False),
        sa.Column(
            "player_id",
            UUID(as_uuid=True),
            sa.ForeignKey("players.id"),
            nullable=False,
        ),
        sa.Column(
            "dungeon_id",
            UUID(as_uuid=True),
            sa.ForeignKey("dungeons.id"),
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
    op.create_table("dungeon_histories", *columns)


def downgrade() -> None:
    op.drop_table("dungeon_histories")
