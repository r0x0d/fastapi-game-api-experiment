"""add global chats table

Revision ID: fafbc5ff017f
Revises: df361914ac23
Create Date: 2022-11-21 19:47:27.807211

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "fafbc5ff017f"
down_revision = "df361914ac23"
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
            "from_account_id",
            UUID(as_uuid=True),
            sa.ForeignKey("accounts.id"),
            nullable=False,
        ),
        sa.Column("message", sa.String(), nullable=False),
        sa.Column(
            "channel_chat_id",
            UUID(as_uuid=True),
            sa.ForeignKey("channel_chats.id"),
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
    op.create_table("global_chats", *columns)


def downgrade() -> None:
    op.drop_table("global_chats")
