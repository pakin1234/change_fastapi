from fastapi import FastAPI
from project.app.api.endpoints.users import user_router


app = FastAPI()
app.include_router(user_router, prefix="/auth")


@app.get("/")
async def main_page():
    return {"data": "Hello world"}