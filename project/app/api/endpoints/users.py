from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from project.app.api.models.users import Token, UserInDB, User
from project.app.core.security import authenticate_user, config, create_jwt_token, get_password_hash
from project.app.db import fake_users_db
from datetime import timedelta
import bcrypt

user_router = APIRouter()

@user_router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password", 
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_jwt_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "type_token": "bearer"}


@user_router.post("/register")
async def register_user(
    user: User, password: Annotated[str, Body()]
    ):
    if user.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
            )
    hashed_password = get_password_hash(password=password)
    fake_users_db[user.username] = UserInDB(**user.model_dump(), hashed_password=hashed_password).model_dump()
    print(fake_users_db)
    return {"data": "added successfully"}
