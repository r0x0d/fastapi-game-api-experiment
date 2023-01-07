"""add vocations table.

Revision ID: 08503cbf8344
Revises: 473845e5b331
Create Date: 2022-10-27 22:19:17.320581

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "08503cbf8344"
down_revision = "473845e5b331"
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
        sa.Column("hitpoints", sa.Integer(), nullable=False),
        sa.Column("strength", sa.Integer()),
        sa.Column("dexterity", sa.Integer()),
        sa.Column("intelligence", sa.Integer()),
        sa.Column("luck", sa.Integer()),
        sa.Column("base_damage", sa.Integer()),
        sa.Column("base_magical_damage", sa.Integer()),
        sa.Column("base_armor_resistance", sa.Integer()),
        sa.Column("base_magical_resistance", sa.Integer()),
        sa.Column("attack_threshold", sa.Float(), nullable=False),
        sa.Column("critical_attack_threshold", sa.Float(), nullable=False),
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
    op.create_table("vocations", *columns)


def downgrade() -> None:
    op.drop_table("vocations")
