from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Platform Demo API"
    debug: bool = False

    database_url: str = "sqlite+aiosqlite:///./dev.db"

    api_secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    gcs_bucket_name: str = ""
    project_id: str = ""


settings = Settings()
