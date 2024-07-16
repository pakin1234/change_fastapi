from pydantic import BaseModel

class Token(BaseModel):
   access_token: str
   type_token: str

class TokenData(BaseModel):
   username: str | None = None

class User(BaseModel):
   username: str
   email: str
   full_name: str | None = None
   disabled: bool | None = None

class UserInDB(User):
   hashed_password: str


