"""add map schemas table

Revision ID: 8a31d6b9e7ad
Revises: dc8743764847
Create Date: 2022-10-28 21:13:43.104909

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

# revision identifiers, used by Alembic.
revision = "8a31d6b9e7ad"
down_revision = "105b44e2cd80"
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
            "schema",
            JSONB(none_as_null=False),
            nullable=False,
            defalut={},
        ),
        sa.Column(
            "map_difficulty_id",
            UUID(as_uuid=True),
            sa.ForeignKey("map_difficulties.id"),
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
    op.create_table("map_schemas", *columns)


def downgrade() -> None:
    op.drop_table("map_schemas")
