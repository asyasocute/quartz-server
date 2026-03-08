# Quartz Server

Backend API for managing notes with user authentication and AI integration (Gemini, Ollama).

i started developing this as my school project but now it just shows that i can create backend in python

## Features

### Authentication

- User registration and login with JWT tokens
- Password hashing with bcrypt
- Secure token-based API access
- Superuser privileges support

### Notes Management

- Create, read, update, and delete notes
- Notes are associated with user accounts
- Full CRUD operations via REST API
- Efficient async database queries

### User Management

- User registration and profile management
- User-specific note organization
- Account management endpoints

### AI Integration

- **Google Gemini** - Generative AI capabilities
- **Ollama** - Local language model support
- AI-powered text processing and analysis
- Dedicated `/api/ai` endpoints for AI operations

## Start local development

- install uv
- install docker
- start docker
- clone this repo
- docker run --rm -d --name postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -p 5430:5432 postgres
- docker exec -it postgres psql -U myuser -c 'CREATE DATABASE mydb;'
- alembic upgrade head
- cp .env.example .env
- fastapi dev --host 0.0.0.0 ./src/main.py

or start with

docker-compose up
