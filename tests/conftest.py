import pytest

from tests.api_client import APIClient


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://vpr-fo1.im.perekrestok.ru/"
    )


@pytest.fixture(scope="session")
def api_client(request) -> APIClient:
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
