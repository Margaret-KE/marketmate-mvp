import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'username': 'user1'}, {'id': 2, 'username': 'user2'}]

def test_get_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json == {'id': 1, 'username': 'user1', 'email': 'user1@example.com'}

def test_create_user(client):
    data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'password123'}
    response = client.post('/users', json=data)
    assert response.status_code == 201
    assert response.json == {'message': 'User created successfully'}

