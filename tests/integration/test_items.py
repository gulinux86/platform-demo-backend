import pytest
from httpx import AsyncClient

from app.config import settings
from app.services.auth import create_access_token


def auth_headers() -> dict:
    token = create_access_token({"sub": "test-client"})
    return {"Authorization": f"Bearer {token}"}


@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    response = await client.post(
        "/items/",
        json={"title": "Test Item", "description": "A test", "status": "todo"},
        headers=auth_headers(),
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["id"] is not None


@pytest.mark.asyncio
async def test_list_items(client: AsyncClient):
    await client.post("/items/", json={"title": "Item 1"}, headers=auth_headers())
    await client.post("/items/", json={"title": "Item 2"}, headers=auth_headers())

    response = await client.get("/items/", headers=auth_headers())
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.asyncio
async def test_update_item(client: AsyncClient):
    create = await client.post("/items/", json={"title": "Original"}, headers=auth_headers())
    item_id = create.json()["id"]

    response = await client.put(
        f"/items/{item_id}",
        json={"status": "done"},
        headers=auth_headers(),
    )
    assert response.status_code == 200
    assert response.json()["status"] == "done"


@pytest.mark.asyncio
async def test_delete_item(client: AsyncClient):
    create = await client.post("/items/", json={"title": "To delete"}, headers=auth_headers())
    item_id = create.json()["id"]

    response = await client.delete(f"/items/{item_id}", headers=auth_headers())
    assert response.status_code == 204

    get = await client.get(f"/items/{item_id}", headers=auth_headers())
    assert get.status_code == 404


@pytest.mark.asyncio
async def test_unauthenticated_request(client: AsyncClient):
    response = await client.get("/items/")
    assert response.status_code == 403
