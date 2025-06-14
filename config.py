from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

ENV = os.getenv("ENV", "development")
load_dotenv(dotenv_path=".env")

class Settings(BaseSettings):
    DATABASE_URL: str 
    DEBUG: bool = False
    ENV: str = ENV

    class Config:
        case_sensitive = True

settings = Settings()
