import httpx
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

from project.app.api.models.currency import ExchangeRequest, ExchangeResponse
from project.app.core.security import get_current_active_user
from project.app.utils.external_api import get_currency_list
# from project.app.utils.external_api import external_api_client

currency_router = APIRouter()

@currency_router.get("/list", dependencies=[Depends(get_current_active_user)])
async def fetch_currency_list():
    data = get_currency_list()
    return data




