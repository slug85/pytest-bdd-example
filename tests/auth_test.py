from tests.api_client import APIClient


def test_pin(api_client: APIClient):
    response = api_client.post("mobile/api/v1/oauth/request_token")
    assert response.status_code == 200
