from app.db.base import Base
from app.db.session import engine
from app.models.user import User  # Ensure models are imported

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully! Tables:", Base.metadata.tables.keys())

if __name__ == "__main__":
    init_db()
