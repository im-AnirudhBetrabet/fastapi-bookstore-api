# 📚 FastAPI Bookstore API

A production-style **Bookstore REST API** built using **FastAPI**, designed to demonstrate
clean API design, validation, and progressive backend architecture.

The project is built **incrementally in stages**:
1. JSON-based storage
2. Pydantic validation & schemas
3. Database-backed persistence (SQL / NoSQL)

This mirrors how real backend systems evolve in production.

---

## 🚀 Features

- RESTful API design
- Clean route separation
- Request & response validation
- Meaningful error handling
- Incremental architecture evolution
- Easily extensible to authentication, pagination, and AI services

---

## 🧱 Architecture Evolution

### Stage 1 — JSON-Based API
- In-memory / JSON file storage
- Core CRUD operations
- HTTP methods & status codes
- FastAPI routing fundamentals

### Stage 2 — Validation with Pydantic
- Request & response models
- Schema validation
- Automatic OpenAPI documentation
- Clear data contracts

### Stage 3 — Database Integration
- Repository pattern
- Dependency injection
- Swappable persistence layer
- SQL (SQLite/PostgreSQL) or NoSQL (MongoDB)

The **API interface remains stable** across all stages.

---

## 📦 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **SQLAlchemy / MongoDB** (Stage 3)
- **pytest** (optional)

---

## 📂 Project Structure
```
fastapi-bookstore-api/
├── app/
│ ├── api/ # Route definitions
│ ├── models/ # Pydantic models
│ ├── services/ # Business logic
│ ├── repository/ # Data access layer
│ ├── db/ # DB configuration
│ └── main.py
├── data/
│ └── books.json # Stage 1 storage
├── tests/
├── README.md
└── requirements.txt
```

---

## 🔗 API Endpoints

### Books
- `GET /books` – List all books
- `GET /books/{id}` – Get book by ID
- `POST /books` – Add a new book
- `PUT /books/{id}` – Update a book
- `DELETE /books/{id}` – Remove a book

---

## ▶️ Running the Project

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fastapi-bookstore-api.git
cd fastapi-bookstore-api
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn app.main:app --reload
```

### 4. Open API Docs
- Swagger UI: http://localhost:8000/docs

- ReDoc: http://localhost:8000/redoc