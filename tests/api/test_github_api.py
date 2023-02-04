import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("AnatoliiDymnich")
    assert user['login'] == "AnatoliiDymnich"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("Anatolii_Dymnich")
    assert r['message'] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("QA_Auto2023")
    assert r['total_count'] == 3
    assert 'QA-Auto2023' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('QA_Auto2023_not_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert ['total_count'] != 0