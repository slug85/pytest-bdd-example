import json

from requests import Response

from api_client import APIClient
from api_paths import *
from datastore import User


def pin_request(user: User, api_client: APIClient) -> Response:
    data = json.dumps({
        "grant_type": "phone_code",
        "client_id": api_client.client_id,
        "client_secret": api_client.client_secret,
        "phone_number": user.phone,
        "response_type": "phone_code",
        "scope": ""
    })
    return api_client.post(path=token_request_path, data=data, user=user)


def auth_request(user: User, api_client: APIClient) -> Response:
    data = json.dumps({
        "grant_type": "phone_code",
        "client_id": api_client.client_id,
        "client_secret": api_client.client_secret,
        "phone_number": user.phone,
        "pin": "12321",
        "scope": ""
    })
    response = api_client.post(path=auth_request_path, data=data)
    user.token = response.json()['access_token']
    return response


def privileges_request(user: User, api_client: APIClient) -> Response:
    response = api_client.get(path=privileges_request_path, user=user)
    return response
