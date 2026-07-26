from pydantic_settings import BaseSettings, SettingsConfigDict 
from pydantic import SecretStr


class Settings(BaseSettings):
    database_url : str
    openai_api_key : SecretStr
    groq_api_key : SecretStr
    logfire_token : SecretStr
    hf_token : SecretStr
    runpod_api_key : SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )


settings = Settings()