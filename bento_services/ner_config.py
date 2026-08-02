# bento_services/ner_config.py

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class NERSettings(BaseSettings):
    hf_token: SecretStr
    logfire_token: SecretStr
    runpod_api_key : SecretStr 

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
        env_file_encoding="utf-8",
    )


ner_settings = NERSettings()