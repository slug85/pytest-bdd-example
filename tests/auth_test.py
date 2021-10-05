import json

from tests.api_client import APIClient
from tests.datastore import DataStore


def test_pin(api_client: APIClient, datastore: DataStore):
    data = json.dumps({
        "grant_type": "phone_code",
        "client_id": "8",
        "phone_number": datastore.user.phone,
        "response_type": "phone_code",
        "client_secret": "ZlxUY81YlQOdWcof9G6EkHiz0316Z1Xhr0WNHDKY",
        "scope": ""
    })
    response = api_client.post(path="mobile/api/v1/oauth/request_token", data=data)
    assert response.status_code == 201
