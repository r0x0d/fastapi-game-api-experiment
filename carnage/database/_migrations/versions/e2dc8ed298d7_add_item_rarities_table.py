"""add item rarities table

Revision ID: e2dc8ed298d7
Revises: 95dedd7a6ff7
Create Date: 2022-10-25 22:12:36.608580

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "e2dc8ed298d7"
down_revision = "95dedd7a6ff7"
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
    op.create_table("item_rarities", *columns)


def downgrade() -> None:
    op.drop_table("item_rarities")
