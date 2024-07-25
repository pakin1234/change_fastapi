import httpx
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

from project.app.api.models.currency import ExchangeRequest, ExchangeResponse
from project.app.core.security import get_current_active_user
from project.app.utils.external_api import get_currency_list, convert_currencies

currency_router = APIRouter()

@currency_router.get("/list", dependencies=[Depends(get_current_active_user)])
async def fetch_currency_list():
    data = get_currency_list()
    return data
 
@currency_router.get("/convert", dependencies=[Depends(get_current_active_user)])
async def currency_convert(exchange: Annotated[ExchangeRequest, Depends()]):
    data = convert_currencies(currency=exchange)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to convert money"
        )
    return data



