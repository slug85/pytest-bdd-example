from tests.api_client import APIClient


def test_fun(api_client: APIClient):
    print(api_client.base_address)
