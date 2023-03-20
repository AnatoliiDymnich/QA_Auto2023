import pytest
import requests


create_pet = {
"id": 0,
"category": {
  "id": 0,
  "name": "bird"
},
"name": "Falcony",
"photoUrls": [
  "string"
],
"tags": [
  {
    "id": 0,
    "name": "Falca"
  }
],
"status": "flying"
}

r = requests.post('https://petstore.swagger.io/v2/pet', json=create_pet)
resp = r.json()
pet_id = resp['id']


@pytest.mark.api
def test_created_pet():
    assert r.status_code == 200


@pytest.mark.api
def test_params_pet():
    r2 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}')
    body = r2.json()
    assert body['name'] == 'Falcony'
    assert body['tags'][0]['name'] == 'Falca'
    assert body['status'] == 'flying'


@pytest.mark.api
def test_pet_for_delete():
    r3 = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}')
    assert r3.status_code == 200
