# bento_services/ner_config.py

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class NERSettings(BaseSettings):
    hf_token: SecretStr
    logfire_token: SecretStr 

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


ner_settings = NERSettings()