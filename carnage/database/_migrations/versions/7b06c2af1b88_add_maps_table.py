"""add maps table

Revision ID: 7b06c2af1b88
Revises: 8a31d6b9e7ad
Create Date: 2022-10-28 21:13:45.686149

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

# revision identifiers, used by Alembic.
revision = "7b06c2af1b88"
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
            "map_schema_id",
            UUID(as_uuid=True),
            sa.ForeignKey("map_schemas.id"),
            nullable=False,
        ),
        sa.Column(
            "plot",
            JSONB(none_as_null=False),
            nullable=False,
            defalut={},
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
    op.create_table("maps", *columns)


def downgrade() -> None:
    op.drop_table("maps")
