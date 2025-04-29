from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.database import get_db
from app.core.security import (
    get_current_user,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

userRoute = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

@userRoute.post("/", response_model=UserOut)
async def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    print("Attempting to create user:", user.username)  # Debug log
    try:
        result = service.create_user(user)
        print("User created successfully")
        return result
    except HTTPException:
        # Re-raise HTTPExceptions with their original status codes
        raise
    except Exception as e:
        print("Error creating user:", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@userRoute.get("/{user_id}", response_model=UserOut)
async def read_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
    current_user_id: int = Depends(get_current_user)
):
    # Verify requesting user matches user_id or has admin rights
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@userRoute.put("/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
    current_user_id: int = Depends(get_current_user)
):
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    updated_user = service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@userRoute.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
    current_user_id: int = Depends(get_current_user)
):
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
        
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return None

@userRoute.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service)
):
    try:
        if not form_data.username or not form_data.password:
            raise HTTPException(status_code=400, detail="Username and password are required")

        user = service.get_user_by_username(form_data.username)
        if not user:
            print(f"User not found: {form_data.username}")
            raise HTTPException(status_code=400, detail="Incorrect username or password")
            
        if not verify_password(form_data.password, user.hashed_password):
            print("Invalid password for user:", form_data.username)
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        # Re-raise HTTPExceptions with their original status codes
        raise
    except Exception as e:
        print("Login error:", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
