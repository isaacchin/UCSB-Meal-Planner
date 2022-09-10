from pydantic import BaseSettings, AnyHttpUrl
from decouple import config, Csv
from typing import List

class Settings(BaseSettings):
    API_STR: str = "/api"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRATION: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "UCSB_Meal_Planner"

    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    ADMIN_USER: str = config("ADMIN_USER", cast=str)

class Config:
    case_sensitive = True

settings = Settings()