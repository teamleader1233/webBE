import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_URL: str = Field(..., env='DATABASE_URL')
    # DOMAIN: str = Field(..., env='DOMAIN')
    
    SECURITY_ALGORITHM = "HS256"
    SECRET_KEY = "123456"

    TOKEN_EXPIRE_MINUTES = 45


settings = Settings()