import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from app.routers.health import router

app = FastAPI()
app.include_router(router)


@pytest.mark.asyncio
async def test_health_endpoint_success():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "environment" in data


@pytest.mark.asyncio
async def test_health_endpoint_wrong_method():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post("/api/health")
        assert response.status_code == 405
