from tests.api_client import APIClient


def test_pin(api_client: APIClient):
    response = api_client.post(path="mobile/api/v1/oauth/request_token", data="""{
            "grant_type": "phone_code",
            "client_id": 8,
            "phone_number": "79002347594",
            "response_type": "phone_code",
            "client_secret": "ZlxUY81YlQOdWcof9G6EkHiz0316Z1Xhr0WNHDKY",
            "scope": ""
        }""")
    assert response.status_code == 201
