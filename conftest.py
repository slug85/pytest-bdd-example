import pytest
from _pytest.config.argparsing import Parser
from datastore import DataStore


def pytest_addoption(parser: Parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://vpr-fo1.im.perekrestok.ru"
    )


@pytest.fixture(scope="function")
def datastore() -> DataStore:
    return DataStore()


@pytest.fixture
def pytestbdd_strict_gherkin():
    return False
