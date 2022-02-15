from pytest_bdd import scenario
from steps import *


@scenario(feature_name="web.feature", scenario_name="Открытие формы")
def test_auth(datastore: DataStore, config_browser):
    pass


@scenario(feature_name="web.feature", scenario_name="Открытие каталога")
def test_catalog(datastore: DataStore, config_browser):
    pass
