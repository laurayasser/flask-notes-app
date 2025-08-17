# 📝 Flask Notes Web App (Docker + MySQL + Docker Compose)

A simple **Note-Taking Web Application** built with:
- **Flask (Python)** for the backend
- **MySQL** for persistent storage
- **Docker & Docker Compose** for containerized orchestration on AWS EC2

---

## 🚀 Features
- Add notes through a simple web UI
- View all saved notes (latest first)
- REST API:
  - `POST /notes` → create a note
  - `GET /notes` → list notes in JSON
- Health check endpoint (`/healthz`)
- MySQL persistence using Docker volumes

---

## 🏗️ Architecture
