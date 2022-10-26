"""add spells table

Revision ID: 95dedd7a6ff7
Revises: 270b23de31a6
Create Date: 2022-10-25 21:36:42.198919

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "95dedd7a6ff7"
down_revision = "270b23de31a6"
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
            "spell_duration_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("spell_duration_types.id"),
            nullable=False,
        ),
        sa.Column(
            "spell_range_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("spell_range_types.id"),
            nullable=False,
        ),
        sa.Column(
            "spell_school_id",
            UUID(as_uuid=True),
            sa.ForeignKey("spell_schools.id"),
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
    op.create_table("spells", *columns)


def downgrade() -> None:
    op.drop_table("spells")
