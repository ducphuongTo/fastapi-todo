"""Setting config"""
import os
from dotenv import load_dotenv
load_dotenv()


def get_connection_string():
    """get connection string"""
    db_engine = os.environ.get("DB_ENGINE")
    db_host = os.environ.get("DB_HOST")
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")
    db_port = os.environ.get("DB_PORT")
    return f"{db_engine}://{username}:{password}@{db_host}:{db_port}/{db_name}"

class Settings:
    """Database Setting"""
    SQLALCHEMY_DB_URL: str = get_connection_string()
    ADMIN_DEFAULT_PASSWORD: str = os.environ.get("ADMIN_DEFAULT_PASSWORD")
    """JWT Setting"""
    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 10
    """CORS Setting"""
    CORS_HEADERS: list[str] = os.environ.get("CORS_HEADERS")
    CORS_ORIGINS: list[str] = os.environ.get("CORS_ORIGINS")

settings = Settings()
