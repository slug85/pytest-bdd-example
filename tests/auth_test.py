import json

from tests.api_client import APIClient
from tests.api_paths import token_request
from tests.datastore import DataStore


def test_pin(api_client: APIClient, datastore: DataStore):
    data = json.dumps({
        "grant_type": "phone_code",
        "client_id": api_client.client_id,
        "phone_number": datastore.user.phone,
        "response_type": "phone_code",
        "client_secret": api_client.client_secret,
        "scope": ""
    })
    response = api_client.post(path=token_request, data=data)
    assert response.status_code == 201
