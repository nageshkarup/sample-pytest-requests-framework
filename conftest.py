import pytest

from main.base.api_client import APIClient


@pytest.fixture(scope="function", autouse=True)
def api_client(request):
    client = APIClient()
    request.cls.client = client
    yield client

