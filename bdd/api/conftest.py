import pytest
from _pytest.fixtures import FixtureRequest
from bdd.api.api_requests import *
from datastore import DataStore


@pytest.fixture(scope="function")
def api_client(request: FixtureRequest) -> APIClient:
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)


@pytest.fixture(scope="function")
def auth(api_client: APIClient, datastore: DataStore):
    pin_request(user=datastore.user, api_client=api_client)
    auth_request(user=datastore.user, api_client=api_client)


@pytest.fixture(scope="function")
def auth_pin(api_client: APIClient, datastore: DataStore):
    pin_request(user=datastore.user, api_client=api_client)
