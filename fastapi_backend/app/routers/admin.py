from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models.models import User, Product, Order
from app.auth.auth import require_admin

router = APIRouter(prefix="/admin", tags=["Admin Analytics"])

@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    total_users = db.query(User).count()
    total_products = db.query(Product).count()
    total_orders = db.query(Order).count()
    total_sales = db.query(func.sum(Order.total)).filter(
        Order.payment_status == "paid"
    ).scalar() or 0

    low_stock = db.query(Product).filter(Product.stock <= 5).all()

    top_products = db.query(
        Product.name,
        Product.popularity
    ).order_by(Product.popularity.desc()).limit(5).all()

    return {
        "total_users": total_users,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_sales": float(total_sales),
        "low_stock_products": [
            {
                "id": p.id,
                "name": p.name,
                "stock": p.stock
            }
            for p in low_stock
        ],
        "top_products": [
            {
                "name": p.name,
                "popularity": p.popularity
            }
            for p in top_products
        ]
    }

@router.get("/users")
def users(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return db.query(User).all()
