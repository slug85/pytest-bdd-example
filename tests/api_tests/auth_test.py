from tests.api_tests.api_steps import *
from tests.datastore import DataStore


def test_auth(api_client: APIClient, datastore: DataStore):
    response = pin_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 201
    response = auth_request(user=datastore.user, api_client=api_client)
    assert response.status_code == 200
