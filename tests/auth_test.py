from tests.api_client import APIClient
from tests.api_steps import pin_request
from tests.datastore import DataStore


def test_pin(api_client: APIClient, datastore: DataStore):
    response = pin_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 201
