import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models.models import User, Product
from app.auth.auth import hash_password

db = SessionLocal()

admin = db.query(User).filter(User.email == "admin@smartecommerce.com").first()

if not admin:
    admin = User(
        name="System Administrator",
        email="admin@smartecommerce.com",
        password=hash_password("Admin@12345"),
        role="admin"
    )
    db.add(admin)

customer = db.query(User).filter(User.email == "customer@smartecommerce.com").first()

if not customer:
    customer = User(
        name="Demo Customer",
        email="customer@smartecommerce.com",
        password=hash_password("Customer@12345"),
        role="customer"
    )
    db.add(customer)

products = [
    {
        "name": "Premium Wireless Headphones",
        "description": "Noise cancelling wireless headphones",
        "price": 5999,
        "stock": 25,
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
    },
    {
        "name": "Smart Watch Pro",
        "description": "Fitness and health tracking smartwatch",
        "price": 7999,
        "stock": 18,
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        "name": "Premium Backpack",
        "description": "Water resistant laptop backpack",
        "price": 2499,
        "stock": 30,
        "category": "Fashion",
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62"
    },
    {
        "name": "Running Shoes",
        "description": "Lightweight performance running shoes",
        "price": 4499,
        "stock": 20,
        "category": "Fashion",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    },
    {
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard for productivity and gaming",
        "price": 6999,
        "stock": 12,
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3"
    }
]

for data in products:
    exists = db.query(Product).filter(Product.name == data["name"]).first()

    if not exists:
        db.add(Product(**data))

db.commit()
db.close()

print("Demo data created successfully")
print("Admin: admin@smartecommerce.com / Admin@12345")
print("Customer: customer@smartecommerce.com / Customer@12345")
