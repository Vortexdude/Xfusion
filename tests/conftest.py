import pytest

from app.app import create_app

@pytest.fixture
def client():
    app = create_app(env='dev')
    with app.test_client() as client:
        yield client


def _create_user(fname, lname, email, password):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    responce = client.post(
        '/users', 
        data={'fname' : fname, 'lname' : lname, 'email': email, 'password': password},
        headers=headers
    )    
    data = responce.data.decode()
    assert 'id' in data

def _login_user(email, password):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'timeout': '3000'
    }
    responce = client.post(
        '/login', 
        data={'email': email, 'password': password},
        headers=headers
    )
    data = responce.data.decode()
    assert 'token' in data
