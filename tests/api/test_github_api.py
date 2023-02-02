import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exist():
    api = GitHub()
    user = api.get_user_defunkt()
    assert user['login'] == "defunkt"
