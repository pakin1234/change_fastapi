from fastapi import FastAPI
from project.app.api.endpoints.users import user_router
from project.app.api.endpoints.currency import currency_router


app = FastAPI()
app.include_router(user_router, prefix="/auth")
app.include_router(currency_router, prefix="/currency")



@app.get("/")
async def main_page():
    return {"data": "Hello world"}