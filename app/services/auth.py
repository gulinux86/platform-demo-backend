from datetime import UTC, datetime, timedelta

from jose import jwt

from app.config import settings


def create_access_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.now(UTC) + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode(payload, settings.api_secret_key, algorithm=settings.algorithm)


def verify_token(token: str) -> dict:
    return jwt.decode(token, settings.api_secret_key, algorithms=[settings.algorithm])
