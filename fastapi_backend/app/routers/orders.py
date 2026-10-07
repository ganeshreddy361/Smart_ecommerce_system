from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Cart, Product, Order, OrderItem, Payment, Notification
from app.auth.auth import get_current_user, require_admin

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/checkout")
def checkout(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = 0

    for item in cart_items:
        if item.product.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {item.product.name}"
            )

        total += item.product.price * item.quantity

    order = Order(
        user_id=current_user.id,
        total=total,
        payment_status="paid",
        order_status="confirmed"
    )

    db.add(order)
    db.flush()

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )

        item.product.stock -= item.quantity
        db.add(order_item)

    payment = Payment(
        order_id=order.id,
        amount=total,
        payment_method="stripe",
        transaction_id=f"STRIPE-DEMO-{order.id}",
        status="succeeded"
    )

    notification = Notification(
        user_id=current_user.id,
        type="order_confirmation",
        message=f"Order #{order.id} confirmed successfully"
    )

    db.add(payment)
    db.add(notification)

    db.query(Cart).filter(Cart.user_id == current_user.id).delete()

    db.commit()
    db.refresh(order)

    return {
        "message": "Checkout successful",
        "order_id": order.id,
        "total": total,
        "payment_status": "paid",
        "order_status": "confirmed"
    }

@router.get("/",)
def my_orders(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return db.query(Order).filter(
        Order.user_id == current_user.id
    ).order_by(Order.timestamp.desc()).all()

@router.get("/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order

@router.put("/{order_id}/status")
def update_order_status(
    order_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    allowed = ["placed", "confirmed", "processing", "shipped", "delivered", "cancelled"]

    if status not in allowed:
        raise HTTPException(status_code=400, detail="Invalid order status")

    order.order_status = status

    notification = Notification(
        user_id=order.user_id,
        type="shipping_update",
        message=f"Order #{order.id} status updated to {status}"
    )

    db.add(notification)
    db.commit()

    return {
        "message": "Order status updated",
        "order_id": order.id,
        "status": status
    }
