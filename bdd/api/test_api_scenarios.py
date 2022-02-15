from pytest_bdd import scenario
from api_steps import *


@scenario(feature_name="features/privileges.feature", scenario_name="Получение привиоегий")
def test_priviledges(auth):
    pass


@scenario(feature_name="features/auth.feature", scenario_name="Получение токена")
def test_auth():
    pass


@scenario(feature_name="features/screen.feature", scenario_name="Получение Главный экран без авторизации")
def test_screen(auth_pin):
    pass

# scenarios("./features")