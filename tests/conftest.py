import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://vpr-fo1.im.perekrestok.ru/"
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")
