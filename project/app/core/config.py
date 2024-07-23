from environs import Env
from pydantic import BaseModel

env = Env()

class APICurrency(BaseModel):
    api_key: str

def load_api_key():
    env = Env()
    env.read_env()

    return APICurrency(
        api_key=env.str("API_KEY")
    )


# class Settings(BaseSettings):
#     base_external_api_url: str = "https://api.apilayer.com/currency_data/"
#     base_external_api_key: str = "yg4AQYAK9B2ha6iYc7if7Oc5m0LkWiZs"

# # посмотреть нужен ли будет этот экземпляр, или можно будет сразу обращаться к классу 
# settings = Settings()

