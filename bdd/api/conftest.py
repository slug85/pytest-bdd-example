import pytest
from _pytest.fixtures import FixtureRequest
from api_client import APIClient


@pytest.fixture(scope="function")
def api_client(request: FixtureRequest) -> APIClient:
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
