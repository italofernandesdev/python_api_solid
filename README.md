# User API (SOLID, FastAPI, MySQL)

A production-ready RESTful API for user management, built with:
- FastAPI (Python 3.10+)
- MySQL 8.0+
- SQLAlchemy ORM
- JWT authentication
- SOLID design principles

## Features
- Secure JWT token authentication
- CRUD operations for user management
- MySQL database integration
- Pydantic data validation
- Clean architecture following SOLID principles
- Environment configuration (.env)
- Automated database migrations

## Prerequisites
- Python 3.10+
- MySQL 8.0+
- pip 22.0+

## Installation
1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment:
   - Copy `.env.template` to `.env`
   - Update database credentials in `.env`

## Running the Application
```bash
uvicorn app.main:app --reload
```

## API Documentation
After starting the server, access interactive API docs at:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## API Reference
### Authentication
- `POST /auth/token` - Get JWT token

### Users
- `POST /users/` - Create new user
- `GET /users/{user_id}` - Get user details
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user
- `GET /users/` - Get all users

## Development
```bash
# Run tests
pytest

# Run with production settings
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Deployment
For production deployment, consider using:
- Gunicorn with Uvicorn workers
- Docker containerization
- MySQL cloud database

## Contributing
Pull requests are welcome. Please open an issue first to discuss changes.
