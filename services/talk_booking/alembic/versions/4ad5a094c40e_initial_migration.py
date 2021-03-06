"""Initial migration

Revision ID: 4ad5a094c40e
Revises:
Create Date: 2022-04-17 13:31:41.856443

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "4ad5a094c40e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "talk_request",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("event_time", sa.DateTime(), nullable=True),
        sa.Column("address", sa.JSON(), nullable=False),
        sa.Column("topic", sa.String(), nullable=False),
        sa.Column("duration_in_minutes", sa.SmallInteger(), nullable=False),
        sa.Column("requester", sa.String(length=120), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_talk_request_id"), "talk_request", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_talk_request_id"), table_name="talk_request")
    op.drop_table("talk_request")
    # ### end Alembic commands ###
