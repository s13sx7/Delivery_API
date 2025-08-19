from typing import Optional
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_PWD: str
    DB_USER: str
    SECKRET_KEY: str
    ALGORITHM: str

    @property
    def DATABASE_URL(self) ->Optional[PostgresDsn]:
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}") # type: ignore
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() # type: ignore