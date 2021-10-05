import json

from requests import Response

from tests.api_client import APIClient
from tests.api_paths import token_request
from tests.datastore import User, DataStore


def pin_request(user: User, api_client: APIClient) -> Response:
    data = json.dumps({
        "grant_type": "phone_code",
        "client_id": api_client.client_id,
        "phone_number": user.phone,
        "response_type": "phone_code",
        "client_secret": api_client.client_secret,
        "scope": ""
    })
    return api_client.post(path=token_request, data=data)
