from pytest_bdd import given, then, parsers
from bdd.api.api_requests import *
from datastore import DataStore


@given("Я получаю список привилегий")
def get_priviledges(api_client: APIClient, datastore: DataStore):
    response = privileges_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 200


@given("Я получаю PIN")
def get_pin(api_client: APIClient, datastore: DataStore):
    response = pin_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 201


@then("Я получаю access_token")
def get_token(api_client: APIClient, datastore: DataStore):
    response = auth_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 200


@given(parsers.cfparse("Я отправляю GET запрос {path}"))
def get(datastore: DataStore, api_client: APIClient, path):
    response = api_client.get(path=path, user=datastore.user)
    assert response.status_code == 200
