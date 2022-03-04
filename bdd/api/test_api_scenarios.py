from pytest_bdd import scenario, scenarios
from api_steps import *

# @scenario(feature_name="features/privileges.feature", scenario_name="Получение привиоегий")
# def test_priviledges(auth):
#    pass


scenarios("features")
