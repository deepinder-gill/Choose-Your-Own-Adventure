from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    
    DATABASE_URL: str

    DEBUG: bool = False

    ALLOWED_ORIGINS: str = ""

    OPEN_API_KEY: str = ""