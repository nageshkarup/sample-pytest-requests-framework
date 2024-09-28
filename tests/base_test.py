import pytest

from main.base.api_client import APIClient


@pytest.mark.usefixtures("api_client")
class BaseTest:
    client: APIClient
