import requests 
import pytest

@pytest.fixture()
def obj_id():
    payload = {
        "name": "Apachi",
        "data":{
            "year": 2022,
            "price":1222,
            "CPU model": "Intel Core j4",
            "Hard disk size": "5 TB"
        }

    }
    response = requests.post(url = 'https://api.restful-api.dev/objects', json=payload).json()
    yield response ['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response["id"]}')


def test_create_object():
    payload = {
        "name": "Apachi",
        "data": {
            "year": 2022,
            "price":1222,
            "CPU model": "Intel Core j4",
            "Hard disk size": "5 TB"
        }

    }
    response = requests.post(url= 'https://api.restful-api.dev/objects', json=payload).json()
    assert response['name'] == payload['name']

def test_get_object(obj_id):
    print(obj_id)
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}'). json()
    assert response['id'] == obj_id



def test_update_object(obj_id):
    payload = {
            "name": "Apachi",
            "data":{
                "year": 2002,
                "price":1222,
                "CPU model": "j4",
                "Hard disk size": "1 TB"
            }
    }

    response = requests.put(url = f'https://api.restful-api.dev/objects/{obj_id}', json= payload). json()
    assert response['name'] == payload['name']

def test_delete_object(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404


