# 📚 Book Review Service

A minimal full-stack backend service built with **FastAPI** and **Strawberry GraphQL**. It supports both REST and GraphQL APIs for managing books and their reviews, with Redis caching and PostgreSQL (or SQLite) for persistence.

---

## 🔧 Tech Stack

- **Python 3.10+**
- **FastAPI** for REST API
- **Strawberry GraphQL** for GraphQL support
- **SQLAlchemy (Async)** as ORM
- **SQLite / PostgreSQL** as database
- **Redis** for caching
- **Alembic** for migrations
- **Pytest** for automated testing

---

## 🗂️ Project Structure

```
book-review-service/
│
├── main.py                      # Entry point
├── requirements.txt
├── alembic.ini
├── README.md
│
├── models/                      # SQLAlchemy models
│   ├── book.py
│   ├── review.py
│   └── base.py
│
├── routes/                      # REST endpoints
│   └── book_routes.py
│
├── schemas/                     # Pydantic and GraphQL types
│   ├── book.py
│   └── review.py
│
├── services/
│   ├── database.py             # DB engine + session
│   ├── cache.py                # Redis logic
│   └── graphql.py              # GraphQL schema + resolvers
│
├── tests/
│   └── test_books.py
│
└── migrations/                 # Alembic auto-generated files
    └── versions/
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/book-review-service.git
cd book-review-service
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file (or rename `.env.example`) with:

```env
DATABASE_URL=sqlite+aiosqlite:///./book_reviews.db
REDIS_URL=redis://localhost:6379
```

✅ Use `psycopg` instead of `aiosqlite` for PostgreSQL:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
```

---

## 🧱 Run Migrations

```bash
alembic init migrations
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

---

## 🟢 Run the Server

```bash
uvicorn main:app --reload
```

- REST API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- GraphQL: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

---

## 🔌 REST Endpoints

| Method | Endpoint                  | Description               |
|--------|---------------------------|---------------------------|
| GET    | `/books`                  | Get all books             |
| POST   | `/books`                  | Add a new book            |
| GET    | `/books/{id}/reviews`     | Get reviews for a book    |
| POST   | `/books/{id}/reviews`     | Add review to a book      |

---

## 🧠 GraphQL Operations

### ✅ Queries - List All Books

```graphql
query {
  books {
    id
    title
    author
  }
}
```

### ✅ Queries - List Reviews for a Book
```graphql
query {
  reviews(bookId: 1) {
    id
    reviewerName
    rating
    comment
  }
}
```

### ✅ Mutation - Add a book
```graphql
mutation {
  addBook(title: "The Alchemist", author: "Paulo Coelho") {
    id
    title
    author
  }
}
```

### ✅ Mutation - Add a Review to a Book
```graphql
mutation {
  addReview(
    bookId: 1,
    reviewerName: "John Doe",
    rating: 5,
    comment: "Absolutely amazing!"
  ) {
    id
    reviewerName
    rating
    comment
  }
}

```



---

## 🧪 Run Tests

```bash
pytest tests/ -v
```

- Includes **unit tests** and a **cache miss integration test**
- Uses `TestClient` and `MockRedis`

---

## 🚨 Error Handling

- Graceful fallback if Redis is unavailable
- Try-except blocks for DB transactions
- Clear FastAPI exception handlers for HTTP errors

---

## 📦 Redis Caching

- `GET /books` reads from Redis first
- Falls back to DB and updates Redis on cache miss

---

## 🧩 Future Extensions (Design Interview Prep)

- Add **GraphQL subscriptions** using Redis pub/sub for live review updates
- Add **JWT Authentication** for user-based review posting
- Add **rate limiting** and **pagination**
- Use **Docker** for containerization
- CI/CD pipeline via GitHub Actions

---

## 📎 License

Use it freely!