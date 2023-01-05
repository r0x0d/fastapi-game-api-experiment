"""add accounts table.

Revision ID: 9c1fb4c99354
Revises: 1e5ec8a69d2a
Create Date: 2022-10-22 23:28:45.897278

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.account import ProviderEnum

# revision identifiers, used by Alembic.
revision = "9c1fb4c99354"
down_revision = "1e5ec8a69d2a"
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
        sa.Column("username", sa.String(length=100), nullable=False),
        sa.Column("nickname", sa.String(length=100), nullable=False),
        sa.Column("provider", sa.Enum(ProviderEnum)),
        sa.Column("secret_key", sa.String(length=100)),
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
    op.create_table("accounts", *columns)


def downgrade() -> None:
    op.drop_table("accounts")
