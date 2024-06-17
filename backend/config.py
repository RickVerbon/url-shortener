import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "URL Shortener"
    environment: str = os.getenv("URLSHORT_ENVIRONMENT", "development")
    base_url: str = os.getenv("URLSHORT_BASE_URL", "http://localhost:8000/")
    url_length: int = os.getenv("URLSHORT_URL_LENGTH", 5)
    database: str = os.getenv("URLSHORT_DATABASE", "sqlite")

    # PostgreSQL settings
    pg_host: str = os.getenv("PGHOST", "localhost")
    pg_port: int = os.getenv("PGPORT", 5432)
    pg_user: str = os.getenv("PGUSER", "urlshort")
    pg_password: str = os.getenv("PGPASSWORD", "urlshort")
    pg_dbname: str = os.getenv("PGDATABASE", "urlshort")

    class Config:
        env_file = ".env"

settings = Settings()