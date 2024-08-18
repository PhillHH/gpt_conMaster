import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_chat(client):
    response = client.post('/chats', json={
        'message': 'Testnachricht'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Testnachricht'

def test_get_chats(client):
    response = client.get('/chats')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_chat(client):
    response = client.get('/chats/1')
    assert response.status_code == 200
    assert 'message' in response.json

def test_update_chat(client):
    response = client.put('/chats/1', json={
        'message': 'Aktualisierte Nachricht'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Aktualisierte Nachricht'

def test_delete_chat(client):
    response = client.delete('/chats/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Chat deleted'
