# User API (SOLID, FastAPI, MySQL)

A RESTful API for managing users, built with FastAPI, MySQL, and SQLAlchemy. Implements authentication via JWT token and follows SOLID principles.

## Features
- Token-based authentication (JWT)
- Endpoints to create, edit, and delete users
- MySQL database
- SOLID design principles

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your MySQL database in `app/core/config.py`.
3. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints
- `POST /users/` - Create user
- `PUT /users/{user_id}` - Edit user
- `DELETE /users/{user_id}` - Delete user

## Auth
All endpoints require a valid JWT token in the `Authorization: Bearer <token>` header.
