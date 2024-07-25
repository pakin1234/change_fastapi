from httpx import get
from project.app.core.config import load_api_key
from project.app.api.models.currency import ExchangeRequest
from fastapi import HTTPException, status

config = load_api_key()
API_KEY = config.api_key
BASE_URL = "https://api.apilayer.com/currency_data/"

def get_currency_list():
    response = get(
        url = BASE_URL + "list",
        headers = {"apikey": API_KEY}
    )
    response.raise_for_status()
    return response.json()["currencies"]

def convert_currencies(currency: ExchangeRequest):
    url = BASE_URL + f"convert?to={currency.to_currency}&from={currency.from_currency}&amount={currency.amount}"
    response = get(
        url=url,
        headers = {"apikey": API_KEY}
    )
    response.raise_for_status()
    return response.json()
