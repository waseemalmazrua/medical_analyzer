from pydantic import Field, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: PostgresDsn = Field(alias="DATABASE_URL")
    openai_api_key: SecretStr
    groq_api_key: SecretStr
    logfire_token: str
    hf_token: SecretStr
    runpod_api_key: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False
    )


settings = Settings()
