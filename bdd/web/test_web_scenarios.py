from pytest_bdd import scenarios, scenario
from web_steps import *


# @scenario(feature_name="features/web.feature", scenario_name="Открытие формы")
# def test_auth():
#     pass


scenarios("features")
