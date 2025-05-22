# ecommerce-backend/README.md

# 🧠 E-Commerce Backend (FastAPI)

This is the backend API for a mobile phone e-commerce web app built with FastAPI. It supports user registration, login, and full CRUD operations for products.

---

## 📁 Folder Structure

```
ecommerce-backend/
├── run.py
├── requirements.txt
├── app/
│   ├── main.py
│   ├── models/
│   │   └── mock_db.py
│   ├── routes/
│   │   ├── product_routes.py
│   │   └── user_routes.py
│   ├── schemas/
│       ├── product_schema.py
│       └── user_schema.py
```

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/ecommerce-backend.git
   cd ecommerce-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # for Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   python run.py
   ```

5. Visit docs at:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ Features

- User Signup & Login (with simulated token)
- Role support: `customer` and `admin`
- CRUD for products
- In-memory database (mocked)
- Modular code structure

---

## 🔧 Requirements

- Python 3.9+
- FastAPI
- Uvicorn

Install via:
```bash
pip install fastapi uvicorn
```

---

## 📌 Next Goals

- JWT-based authentication
- Admin-only product creation
- Cart and order endpoints
- Persistent database (PostgreSQL/MongoDB)

---

## 🙌 Author

Built by Swatantra Sharma as part of a backend development assignment.
