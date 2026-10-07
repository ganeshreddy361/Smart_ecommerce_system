from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class User(Base):

    __tablename__ = "users_user"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String(150),
        unique=True,
        nullable=False
    )

    email = Column(
        String(254),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(128),
        nullable=False
    )

    first_name = Column(
        String(150),
        nullable=False,
        default=""
    )

    last_name = Column(
        String(150),
        nullable=False,
        default=""
    )

    role = Column(
        String(20),
        nullable=False,
        default="customer"
    )

    phone = Column(
        String(20),
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
    )

    is_staff = Column(
        Boolean,
        default=False
    )

    date_joined = Column(
        DateTime,
        server_default=func.now()
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
