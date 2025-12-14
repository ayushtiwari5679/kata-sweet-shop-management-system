# 🍬 Sweet Shop Management System (TDD Kata)

A full-stack **Sweet Shop Management System** built using **FastAPI**, **React**, and **SQLite**, following **Test-Driven Development (TDD)** principles and modern software engineering best practices.

This project was developed as part of a technical kata to demonstrate backend API design, frontend SPA development, authentication, testing, and responsible AI usage.

---

## 🎯 Objective

The goal of this kata is to design, build, and test a full-stack Sweet Shop Management System that allows users to browse, search, and purchase sweets while allowing admin users to manage inventory securely.

---

## 🧱 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pytest

### Frontend
- React 18
- Vite
- Axios
- Tailwind CSS

---

## ✨ Features

### 👤 Authentication
- User registration
- User login
- JWT-based token authentication
- Role-based access control (Admin / User)

### 🍭 Sweet Management
- Add sweets (Admin only)
- View all sweets
- Search sweets by name, category, or price range
- Update sweet details (Admin only)
- Delete sweets (Admin only)

### 📦 Inventory
- Purchase sweets (stock decreases)
- Restock sweets (Admin only)
- Purchase button disabled when stock is zero

---

## 🔐 API Endpoints

### Auth
- `POST /api/auth/register`
- `POST /api/auth/login`

### Sweets (Protected)
- `POST /api/sweets`
- `GET /api/sweets`
- `GET /api/sweets/search`
- `PUT /api/sweets/{id}`
- `DELETE /api/sweets/{id}`

### Inventory
- `POST /api/sweets/{id}/purchase`
- `POST /api/sweets/{id}/restock`

---

## 🚀 Local Setup Instructions

### 📂 Project Location


---

sweet-shop/


---

### ▶ Backend Setup

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs at:

http://localhost:8000


Swagger API Docs:

http://localhost:8000/docs

▶ Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:5173

🧪 Running Tests
cd backend
pytest


The test suite covers:

Authentication

Sweet CRUD operations

Inventory purchase & restock logic

🔁 Test-Driven Development (TDD)

This project follows the Red → Green → Refactor approach:

Write failing tests

Implement minimal logic to pass tests

Refactor code for clarity and maintainability

Commit history reflects incremental, test-first development.

📸 Screenshots
Sweet Shop Dashboard

The dashboard displays available sweets, pricing, stock information, purchase buttons, and admin controls.

🤖 My AI Usage (Mandatory Disclosure)
AI Tools Used

ChatGPT (OpenAI)

How I Used AI
🔐 Authentication

Generated initial JWT authentication boilerplate

Assisted with structuring login and registration endpoints

Helped debug token validation and dependency injection issues

🎨 Frontend

Assisted in designing React component structure

Helped generate login and registration form layouts

Assisted in setting up Axios API service patterns

My Reflection on AI Usage

AI significantly improved development speed by reducing boilerplate and assisting with debugging.
All business logic, validation, tests, and architectural decisions were reviewed, refined, and implemented manually to ensure correctness, maintainability, and learning value.

🧾 AI Co-Authorship in Git Commits

For commits where AI assistance was used, the following co-author trailer was added:

Co-authored-by: Claude <AI@users.noreply.github.com>
Co-authored-by: ChatGPT <AI@users.noreply.github.com>

👨‍💻 Author

Ayush Tiwari
