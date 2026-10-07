from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.sql import func

from app.database import Base


class Order(Base):

    __tablename__ = "orders_order"

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

    total = Column(
        Numeric(12, 2),
        nullable=False
    )

    payment_status = Column(
        String(20),
        default="pending"
    )

    order_status = Column(
        String(30),
        default="placed"
    )

    shipping_address = Column(
        Text,
        nullable=True
    )

    timestamp = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )


class OrderItem(Base):

    __tablename__ = "orders_orderitem"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders_order.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products_product.id"),
        nullable=True
    )

    product_name = Column(
        String(200),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    price = Column(
        Numeric(12, 2),
        nullable=False
    )

    subtotal = Column(
        Numeric(12, 2),
        nullable=False
    )


class Payment(Base):

    __tablename__ = "orders_payment"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders_order.id"),
        nullable=False,
        unique=True
    )

    amount = Column(
        Numeric(12, 2),
        nullable=False
    )

    payment_method = Column(
        String(50),
        default="stripe"
    )

    transaction_id = Column(
        String(255),
        nullable=True
    )

    status = Column(
        String(20),
        default="pending"
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
