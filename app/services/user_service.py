from typing import Optional
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_user(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.repository.get_user_by_username(username)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.repository.get_user_by_email(email)

    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.repository.get_users(skip, limit)

    def create_user(self, user: UserCreate) -> User:
        # Additional business logic can be added here
        return self.repository.create_user(user)

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        user = self.repository.get_user(user_id)
        if not user:
            return None
        return self.repository.update_user(user, user_update)

    def delete_user(self, user_id: int) -> bool:
        user = self.repository.get_user(user_id)
        if not user:
            return False
        self.repository.delete_user(user)
        return True
