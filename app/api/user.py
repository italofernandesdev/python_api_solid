from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

@router.post("/", response_model=UserOut)
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    print("Attempting to create user:", user.username)  # Debug log
    try:
        result = service.create_user(user)
        print("User created successfully")
        return result
    except Exception as e:
        print("Error creating user:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    updated_user = service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return None
