import sys
import os
import openai
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    # Erstellen Sie einen neuen Chat
    post_response = client.post('/chats', json={'message': 'Testnachricht', 'user_id': 1})
    
    # Überprüfen Sie, ob der Chat erfolgreich erstellt wurde
    assert post_response.status_code == 201  # 201 Created
    created_chat_id = post_response.json['id']  # Die ID des erstellten Chats sollte zurückgegeben werden
    
    # Versuchen Sie nun, den erstellten Chat abzurufen
    response = client.get(f'/chats/{created_chat_id}')
    assert response.status_code == 200  # Stellen Sie sicher, dass der Abruf erfolgreich ist
    assert response.json['message'] == 'Testnachricht'  # Überprüfen Sie, ob die Nachricht korrekt ist


def test_update_chat(client):
    # Erstellen Sie einen neuen Chat
    post_response = client.post('/chats', json={'message': 'Testnachricht', 'user_id': 1})
    
    # Überprüfen Sie, ob der Chat erfolgreich erstellt wurde
    assert post_response.status_code == 201  # 201 Created
    created_chat_id = post_response.json['id']  # Die ID des erstellten Chats sollte zurückgegeben werden
    
    # Aktualisieren Sie den erstellten Chat
    response = client.put(f'/chats/{created_chat_id}', json={
        'message': 'Aktualisierte Nachricht'
    })
    
    # Überprüfen Sie, ob die Aktualisierung erfolgreich war
    assert response.status_code == 200
    assert response.json['message'] == 'Aktualisierte Nachricht'  # Überprüfen Sie, ob die Nachricht aktualisiert wurde


def test_delete_chat(client):
    # Erstellen Sie einen neuen Chat
    post_response = client.post('/chats', json={'message': 'Testnachricht', 'user_id': 1})
    
    # Überprüfen Sie, ob der Chat erfolgreich erstellt wurde
    assert post_response.status_code == 201  # 201 Created
    created_chat_id = post_response.json['id']  # Die ID des erstellten Chats sollte zurückgegeben werden
    
    # Löschen Sie den erstellten Chat
    response = client.delete(f'/chats/{created_chat_id}')
    
    # Überprüfen Sie, ob das Löschen erfolgreich war
    assert response.status_code == 200

def test_create_branch(client):
    response = client.post('/branches/create', json={
        'chat_id': 1,
        'message': 'Start a new branch'
    })
    assert response.status_code == 201
    assert 'branch_id' in response.json

def test_get_branch(client):
    response = client.get('/branches/1')
    assert response.status_code == 200
    assert 'branch_id' in response.json

