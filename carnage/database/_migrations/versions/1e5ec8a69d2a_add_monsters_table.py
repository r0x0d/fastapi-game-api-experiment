"""Add monsters table

Revision ID: 1e5ec8a69d2a
Revises: faffe495bb96
Create Date: 2022-10-12 02:29:14.502293

"""
import uuid
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "1e5ec8a69d2a"
down_revision = "faffe495bb96"
branch_labels = None
depends_on = None


def upgrade() -> None:
    columns = [
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4(),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("hitpoints", sa.Integer(), nullable=False),
        sa.Column("strength", sa.Integer()),
        sa.Column("dexterity", sa.Integer()),
        sa.Column("intelligence", sa.Integer()),
        sa.Column("base_damage", sa.Integer()),
        sa.Column("base_magical_damage", sa.Integer()),
        sa.Column("base_armor_resistance", sa.Integer()),
        sa.Column("base_magical_resistance", sa.Integer()),
        sa.Column(
            "monster_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("monster_types.id"),
            nullable=False,
        ),
        sa.Column(
            "size_id",
            UUID(as_uuid=True),
            sa.ForeignKey("sizes.id"),
            nullable=False,
        ),
        sa.Column(
            "aligment_id",
            UUID(as_uuid=True),
            sa.ForeignKey("aligments.id"),
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
    op.create_table("monsters", *columns)


def downgrade() -> None:
    op.drop_table("monsters")
