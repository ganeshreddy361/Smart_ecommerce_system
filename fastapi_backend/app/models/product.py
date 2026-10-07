from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.sql import func

from app.database import Base


class Category(Base):

    __tablename__ = "products_category"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class Product(Base):

    __tablename__ = "products_product"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(200),
        nullable=False,
        index=True
    )

    description = Column(
        Text,
        nullable=False
    )

    price = Column(
        Numeric(12, 2),
        nullable=False
    )

    stock = Column(
        Integer,
        nullable=False,
        default=0
    )

    category_id = Column(
        Integer,
        ForeignKey("products_category.id"),
        nullable=True
    )

    image = Column(
        String(100),
        nullable=True
    )

    rating = Column(
        Numeric(3, 2),
        default=0
    )

    total_sold = Column(
        Integer,
        default=0
    )

    is_active = Column(
        Boolean,
        default=True
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
