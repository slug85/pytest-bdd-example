import pytest
from email.parser import Parser
from _pytest.fixtures import FixtureRequest

from tests.api_client import APIClient


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
