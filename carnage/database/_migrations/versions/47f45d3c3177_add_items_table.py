"""add items table

Revision ID: 47f45d3c3177
Revises: 87b7c15b5878
Create Date: 2022-10-25 22:12:51.708282

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "47f45d3c3177"
down_revision = "87b7c15b5878"
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
        sa.Column("strength", sa.Integer()),
        sa.Column("dexterity", sa.Integer()),
        sa.Column("intelligence", sa.Integer()),
        sa.Column("base_damage", sa.Integer()),
        sa.Column("base_magical_damage", sa.Integer()),
        sa.Column("base_armor_resistance", sa.Integer()),
        sa.Column("base_magical_resistance", sa.Integer()),
        sa.Column(
            "item_rarity_id",
            UUID(as_uuid=True),
            sa.ForeignKey("item_rarities.id"),
            nullable=False,
        ),
        sa.Column(
            "item_base_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("item_base_types.id"),
            nullable=False,
        ),
        sa.Column(
            "item_magical_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("item_magical_types.id"),
            nullable=True,
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
    op.create_table("items", *columns)


def downgrade() -> None:
    op.drop_table("items")
