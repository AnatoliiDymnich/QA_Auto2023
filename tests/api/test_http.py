import pytest
import requests


@pytest.mark.http
def test_first_request() :
    r = requests.get('https://api.github.com/zen')
    print(r.text)



@pytest.mark.http
def test_second_request() :
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers
    
    assert body['blog'] == 'http://chriswanstrath.com/'
    assert r.status_code == 200
    assert headers["Content-Type"] == 'application/json; charset=utf-8'


@pytest.mark.http
def test_status_code_request() :
    r = requests.get('https://api.github.com/users/anatolii_dymnich')

    assert r.status_code == 404