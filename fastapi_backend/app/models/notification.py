from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class Notification(Base):

    __tablename__ = "notifications_notification"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users_user.id"),
        nullable=False
    )

    type = Column(
        String(50),
        default="general"
    )

    message = Column(
        Text,
        nullable=False
    )

    is_read = Column(
        Boolean,
        default=False
    )

    timestamp = Column(
        DateTime,
        server_default=func.now()
    )
