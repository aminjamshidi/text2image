from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )

    TOGETHER_API_KEY: str
    TTI_MODEL_NAME: str = "black-forest-labs/FLUX.1-schnell-Free"


settings = Settings()
