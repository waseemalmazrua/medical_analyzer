import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, SQLModel


# تعريف خارجي مختصر لجدول Supabase Auth.
# نحن لا ننشئه ولا نديره.
auth_users = Table(
    "users",
    SQLModel.metadata,
    Column(
        "id",
        PG_UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
    ),
    schema="auth",
    info={
        "skip_autogenerate": True,
    },
)


class Profile(SQLModel, table=True):
    __tablename__ = "profiles"

    id: uuid.UUID = Field(
        sa_column=Column(
            PG_UUID(as_uuid=True),
            ForeignKey(
                "auth.users.id",
                ondelete="CASCADE",
            ),
            primary_key=True,
            nullable=False,
        )
    )

    full_name: str | None = Field(
        default=None,
        max_length=120,
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        ),
    )