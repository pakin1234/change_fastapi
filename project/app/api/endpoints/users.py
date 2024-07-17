from typing import Annotated

from fastapi import FastAPI, Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from project.app.api.models.users import Token
from project.app.core.security import authenticate_user, fake_users_db, TIME_EXPIRATION, create_jwt_token
from datetime import timedelta

user_router = APIRouter()

@user_router.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    print(user)
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
    return Token(access_token=access_token, type_token="bearer")