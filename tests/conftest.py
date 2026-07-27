import pytest
from fastapi.testclient import TestClient

from src.api import app, service


@pytest.fixture(autouse=True)
def reset_service() -> None:
    service.reset()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
