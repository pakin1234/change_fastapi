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

