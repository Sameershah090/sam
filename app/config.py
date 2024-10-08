from pydantic import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    PORT: int = 8080

    class Config:
        env_file = ".env"

settings = Settings()
