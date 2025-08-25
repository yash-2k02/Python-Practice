# FastAPI + MySQL CRUD Project

This is a **FastAPI application** that demonstrates REST APIs for Customers, Products, and Orders using **raw SQL queries** with MySQL.  

---

## Project Structure

### 🔹 Key Files
- **main.py** → FastAPI app entry point, includes routers.  
- **db.py** → Database connection setup using `mysql.connector`.  
- **models/** → Pydantic models (request/response validation).  
  - `customer.py`, `product.py`, `order.py`  
- **routes/** → API route handlers for CRUD operations.  
- **requirements.txt** → Python dependencies.  

---

## Features
- FastAPI app with modular routes.  
- MySQL database connection using `mysql.connector`.  
- CRUD operations for:
  - **Customers**
  - **Products**
  - **Orders**
- Uses **Pydantic models** for request validation (`CustomerCreate`, `CustomerUpdate`, etc).  

---