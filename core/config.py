from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"

    DATABASE_URL: str

    DEBUG: bool = False

    ALLOWED_ORIGINS: str = ""

    OPEN_API_KEY: str = ""

    @field_validator("ALLOWED_ORIGINS")
    @classmethod
    def allowed_origins_validator(cls, v: str) -> List[str]:
        return v.split(",") if v else []

class Config:
    env_file = ".env"
    enf_file_encoding = "utf-8"
    case_sensitive = True

settings = Settings()
