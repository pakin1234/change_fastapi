from pydantic import BaseModel

class ExchangeRequest(BaseModel):
    from_currency: str
    to_currency: str

class ExchangeResponse(BaseModel):
    from_currency: str
    to_currency: str
    rate: str


