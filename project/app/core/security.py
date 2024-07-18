from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends, HTTPException, status

import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import project.app.api.models.users as amu
from project.app.db import fake_users_db

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
TIME_EXPIRATION = timedelta(minutes=30)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# Перенести в файл db.py?
# ---------------------------
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }
# # ---------------------------

def create_jwt_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)
    if expires_delta:
       expire += expires_delta
    else:
       expire += timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt_token(encoded_jwt: str):
    try:
      decoded_jwt = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[ALGORITHM])
      return decoded_jwt
    except jwt.PyJWTError:
      return None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
   return pwd_context.hash(password)

def get_user(db, username: str):
   if username in db:
      user_dict = db[username]
      return amu.UserInDB(**user_dict)
   
def authenticate_user(fake_db, username: str, password: str):
   user = get_user(fake_db, username)
   if not user:
      return False
   if not verify_password(password, user.hashed_password):
      return False
   return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
   credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED, 
      detail="No validate credentials", 
      headers={"WWW-Authenticate": "Bearer"},)
   try:
     payload = verify_jwt_token(token)
     username: str = payload.get("sub")
     if username is None:
        raise credentials_exception
     token_data = amu.TokenData(username=username)
   except:
     raise credentials_exception
   user = get_user(fake_users_db, username=token_data.username)
   if user is None:
      raise credentials_exception
   return user


