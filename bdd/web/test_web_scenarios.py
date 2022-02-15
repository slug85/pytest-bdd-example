from pytest_bdd import scenario
from web_steps import *


@scenario(feature_name="features/web.feature", scenario_name="Открытие формы")
def test_auth(datastore: DataStore):
    pass


@scenario(feature_name="features/web.feature", scenario_name="Открытие каталога")
def test_catalog(datastore: DataStore):
    pass
