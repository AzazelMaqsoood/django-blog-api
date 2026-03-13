# Django Blog API

REST API для блога с авторизацией, поиском и асинхронными задачами.

## 🚀 Features
- JWT Authentication
- Search & Filtering
- Nested Serializers
- Celery Background Tasks
- Dockerized

## 🛠 Installation
1. Clone repo
2. `docker-compose up --build`
3. Visit `http://localhost:8000/api/`

## 📝 API Endpoints
- `POST /api/token/` - Get JWT token
- `GET/POST /api/posts/` - List/Create posts
- `GET/POST /api/comments/` - List/Create comments
