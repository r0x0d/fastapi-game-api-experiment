"""add vocation spells table

Revision ID: dc8743764847
Revises: 08503cbf8344
Create Date: 2022-10-27 22:19:22.637150

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "dc8743764847"
down_revision = "08503cbf8344"
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
            "vocation_id",
            UUID(as_uuid=True),
            sa.ForeignKey("vocations.id"),
            nullable=False,
        ),
        sa.Column(
            "spell_id",
            UUID(as_uuid=True),
            sa.ForeignKey("spells.id"),
            nullable=False,
        ),
        sa.Column(
            "spell_order",
            sa.Integer(),
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
    op.create_table("vocation_spells", *columns)


def downgrade() -> None:
    op.drop_table("vocation_spells")
