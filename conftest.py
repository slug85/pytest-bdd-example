import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest

from api_client import APIClient
from api_requests import pin_request, auth_request
from datastore import DataStore


def pytest_addoption(parser: Parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://vpr-fo1.im.perekrestok.ru/"
    )


@pytest.fixture(scope="session")
def api_client(request: FixtureRequest) -> APIClient:
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)


@pytest.fixture(scope="function")
def datastore() -> DataStore:
    return DataStore()


@pytest.fixture(scope="function")
def auth(api_client: APIClient, datastore: DataStore):
    pin_request(user=datastore.user, api_client=api_client)
    auth_request(user=datastore.user, api_client=api_client)
