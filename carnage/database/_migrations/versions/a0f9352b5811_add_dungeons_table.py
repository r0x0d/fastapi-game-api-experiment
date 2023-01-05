"""add dungeons table.

Revision ID: a0f9352b5811
Revises: 8a31d6b9e7ad
Create Date: 2022-10-28 22:24:29.940836

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

# revision identifiers, used by Alembic.
revision = "a0f9352b5811"
down_revision = "8a31d6b9e7ad"
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
            "dungeon_schema_id",
            UUID(as_uuid=True),
            sa.ForeignKey("dungeon_schemas.id"),
            nullable=False,
        ),
        sa.Column(
            "plot",
            JSONB(none_as_null=False),
            nullable=False,
            default={},
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
    op.create_table("dungeons", *columns)


def downgrade() -> None:
    op.drop_table("dungeons")
