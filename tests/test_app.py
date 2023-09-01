from tests.conftest import client

def test_create_user_in_database(client):
    fname = "Nitin"
    lname = "Namdev"
    email = "nnamdev@google.com"
    password = "test"

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
