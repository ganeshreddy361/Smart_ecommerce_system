from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Cart, Product
from app.schemas.schemas import CartRequest
from app.auth.auth import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/")
def get_cart(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    items = db.query(Cart).filter(Cart.user_id == current_user.id).all()

    return [
        {
            "id": item.id,
            "product_id": item.product_id,
            "product_name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity,
            "subtotal": item.product.price * item.quantity
        }
        for item in items
    ]

@router.post("/")
def add_to_cart(
    data: CartRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == data.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < data.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    existing = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == data.product_id
    ).first()

    if existing:
        existing.quantity += data.quantity
    else:
        existing = Cart(
            user_id=current_user.id,
            product_id=data.product_id,
            quantity=data.quantity
        )
        db.add(existing)

    product.popularity += 1
    db.commit()

    return {"message": "Product added to cart"}

@router.delete("/{cart_id}")
def remove_from_cart(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    item = db.query(Cart).filter(
        Cart.id == cart_id,
        Cart.user_id == current_user.id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()

    return {"message": "Product removed from cart"}
