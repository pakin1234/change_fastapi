import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
TIME_EXPIRATION = timedelta(minutes=30)

def create_jwt_token(data: dict):
    expiration = datetime() + TIME_EXPIRATION
    data.update({"exp": expiration})
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verify_jwt_token(token_jwt: str):
    try:
      decoded_jwt_token = jwt.decode(token_jwt, SECRET_KEY, algorithms=[ALGORITHM])
      return decoded_jwt_token
    except jwt.PyJWTError:
      return None

