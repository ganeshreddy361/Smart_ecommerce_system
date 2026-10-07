from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import User, Product, Cart, Order, OrderItem, Payment, Notification
from app.routers import auth, products, cart, orders, notifications, admin
from app.websocket.notifications import router as websocket_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart E-Commerce Platform API",
    description="Production-style Smart E-Commerce REST API with authentication, products, cart, orders, payments, notifications and analytics.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(notifications.router)
app.include_router(admin.router)
app.include_router(websocket_router)

@app.get("/")
def root():
    return {
        "project": "Smart E-Commerce Platform",
        "status": "running",
        "backend": "FastAPI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected"
    }
