import pytest
from jose import jwt

from app.config import settings
from app.services.auth import create_access_token, verify_token


def test_create_and_verify_token():
    token = create_access_token({"sub": "test-user"})
    payload = verify_token(token)
    assert payload["sub"] == "test-user"


def test_token_contains_expiry():
    token = create_access_token({"sub": "test-user"})
    payload = jwt.decode(token, settings.api_secret_key, algorithms=[settings.algorithm])
    assert "exp" in payload


def test_invalid_token_raises():
    from jose import JWTError
    with pytest.raises(JWTError):
        verify_token("invalid.token.here")
