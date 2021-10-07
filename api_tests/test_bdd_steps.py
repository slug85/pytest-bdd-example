import threading
import time

from pytest_bdd import scenario, given, then
from api_tests.api_requests import *
from datastore import DataStore


@scenario(feature_name="privileges.feature", scenario_name="Получение", features_base_dir="features")
def test_priviledges(auth):
    pass


@scenario(feature_name="auth.feature", scenario_name="Получение токена", features_base_dir="features")
def test_auth():
    pass


@given("Я получаю список привилегий")
def get_priviledges(api_client: APIClient, datastore: DataStore):
    response = privileges_request(datastore.user, api_client)
    count(15)
    assert response.status_code == 200


@given("Я получаю PIN")
def get_pin(api_client: APIClient, datastore: DataStore):
    response = pin_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 201


@then("Я получаю access_token")
def get_token(api_client: APIClient, datastore: DataStore):
    response = auth_request(user=datastore.user, api_client=api_client)
    count(15)
    assert response.status_code == 200


def count(max_count: int):
    for x in range(0, max_count, 1):
        print(threading.get_ident())
        time.sleep(1)
