from fastapi import APIRouter, HTTPException, status

from app.config import settings
from app.schemas.auth import TokenRequest, TokenResponse
from app.services.auth import create_access_token

router = APIRouter()


@router.post("/token", response_model=TokenResponse)
async def login(request: TokenRequest):
    if request.api_key != settings.api_secret_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    token = create_access_token({"sub": "api-client"})
    return TokenResponse(access_token=token)
