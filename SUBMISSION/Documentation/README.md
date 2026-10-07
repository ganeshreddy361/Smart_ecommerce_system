# Smart E-Commerce Platform

## Project Overview
A full-stack smart e-commerce platform with a FastAPI-based user panel and Django-based admin panel.

## Technology Stack
- FastAPI
- Django
- MySQL
- JWT Authentication
- React / Frontend
- WebSockets
- Stripe Payment Integration
- Chart.js / Plotly

## User Panel - FastAPI
- User registration and login
- JWT authentication
- Product browsing
- Cart management
- Order management
- Payment processing
- Notifications
- WebSocket support

## Admin Panel - Django
- User management
- Product management
- Order management
- Notifications
- Analytics
- Reports
- Django migrations

## Main Entities
- User
- Product
- Cart
- Order
- Payment
- Notification

## Project Structure

smart-ecommerce-platform/
├── django_backend/
│   ├── ecommerce_admin/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── notifications/
│   ├── analytics/
│   ├── reports/
│   └── manage.py
│
└── fastapi_backend/
    ├── app/
    │   ├── routers/
    │   ├── models/
    │   ├── schemas/
    │   ├── services/
    │   ├── auth/
    │   └── websocket/
    └── requirements.txt

## Running Django

cd django_backend
python manage.py migrate
python manage.py runserver

## Running FastAPI

cd fastapi_backend
uvicorn app.main:app --reload

## API Documentation

FastAPI interactive API documentation is available at:

http://127.0.0.1:8000/docs

## Database

Django migration files are included in the project for database setup.

## Security

- JWT authentication is implemented for protected API access.
- Passwords should not be stored in plain text.
- Role-based access control is supported.
- Payment information should not store CVV data.

## Deliverables

- Django source code
- FastAPI source code
- Database migrations
- API implementation
- Documentation
- Demo materials
