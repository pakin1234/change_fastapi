from pydantic import BaseModel

class ExchangeRequest(BaseModel):
    to_currency: str
    from_currency: str
    amount: float

class ExchangeResponse(BaseModel):
    rate: str

class ListOfAcceptedCurrencies(BaseModel):
    currencies: list


