from httpx import get
from project.app.core.config import load_api_key

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

# import httpx
# from project.app.core.config import settings

# class ExternalApiClient:
#     def __init__(self, url: str, key: str):
#         self.url = url
#         self.key = key

#     async def get_exchange_rate(self, from_currency: str, to_currency: str):
#         async with httpx.AsyncClient as client:
#             response = await client.get(
#                 # поменять путь как показано в документации API
#                 f"{self.url}/currency_change",
#                 params={"from_currency": from_currency, "to_currency": to_currency},
#                 headers={"Authorization": f"Bearer {self.key}"}
#             )
#             response.raise_for_status()
#             return response.json()
        
# external_api_client = ExternalApiClient(
#     url=settings.base_external_api_url,
#     key=settings.base_external_api_key
# )