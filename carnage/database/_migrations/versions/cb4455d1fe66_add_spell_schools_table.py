"""add spell schools table

Revision ID: cb4455d1fe66
Revises: 9c1fb4c99354
Create Date: 2022-10-25 20:13:25.992391

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "cb4455d1fe66"
down_revision = "9c1fb4c99354"
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
    op.create_table("spell_schools", *columns)


def downgrade() -> None:
    op.drop_table("spell_schools")
