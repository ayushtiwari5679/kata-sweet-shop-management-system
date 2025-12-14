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
