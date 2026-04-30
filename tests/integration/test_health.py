import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_readiness(client: AsyncClient):
    response = await client.get("/readiness")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"
