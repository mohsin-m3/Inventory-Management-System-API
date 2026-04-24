# Inventory Management System API

A production-style backend project built using **Flask, MySQL, JWT Authentication, Docker, and REST APIs**.  
This project provides inventory operations like product management, stock control, customer orders, and secure login.

---

# Features

✅ User Registration & Login  
✅ JWT Authentication  
✅ Role-Based Access (Admin / User)  
✅ Product CRUD Operations  
✅ Order Management  
✅ MySQL Database Integration  
✅ Dockerized Setup  
✅ REST API Architecture  
✅ AWS Ready Deployment  

---

# Tech Stack

- Python 3.11
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- MySQL
- Docker
- Docker Compose
- Postman
- AWS EC2

---

# Project Structure

```text
inventory-management-api/
│── app.py
│── config.py
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── README.md
│── src/
│   ├── __init__.py
│   ├── models.py
│   ├── routes_auth.py
│   ├── routes_products.py
│   └── routes_orders.py
└── screenshots/
    ├── login.png
    ├── products.png
    └── orders.png
Installation & Setup
1 Clone Repository
git clone https://github.com/yourusername/inventory-management-api.git
cd inventory-management-api
2 Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
3 Install Dependencies
pip install -r requirements.txt
4 Configure Environment Variables

Create .env

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=mysql+pymysql://root:password@localhost/inventorydb
5 Run MySQL Database

Create database:

CREATE DATABASE inventorydb;
6 Run Application
python app.py

Server starts:

http://127.0.0.1:5000
Run Using Docker
docker-compose up --build
API Endpoints
Authentication
Register
POST /api/auth/register

Code:

{
  "username": "admin",
  "password": "admin123"
}
Login
POST /api/auth/login

Body:

{
  "username": "admin",
  "password": "admin123"
}
Products
Get Products
GET /api/products
Add Product
POST /api/products
Authorization: Bearer Token

CMD:

{
  "name": "Laptop",
  "stock": 10,
  "price": 55000
}
Orders
Create Order
POST /api/orders
Authorization: Bearer Token

Code:

{
  "product_id": 1,
  "quantity": 2
}


Deployment on AWS EC2
Launch EC2 Ubuntu instance
Install Docker
Clone repository
Run:
docker-compose up -d
Open port 5000
Future Improvements
Swagger API Docs
Email Notifications
Admin Dashboard UI
Payment Integration
Kubernetes Deployment
Author

Mohsin Majid Mulla

LinkedIn:https://www.linkedin.com/in/mohsinmulla17/
