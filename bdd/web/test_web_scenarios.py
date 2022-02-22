from pytest_bdd import scenarios
from web_steps import *


# @scenario(feature_name="features/web.feature", scenario_name="Открытие формы")
# def test_auth(datastore: DataStore):
#     pass


scenarios("./features")
