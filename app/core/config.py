from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSGR_URL: PostgresDsn = ""
    SECRET_KEY:str = ""
    ALGORITHM:str = ""
    ACCESS_TOKEN_EXPIRES_MIN:int = 30

    class Config:
        env_file = ".env_set"

settings = Settings()