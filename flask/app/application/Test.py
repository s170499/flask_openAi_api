import pytest
import json
from .app import create_app, db
from models import QandA

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_ask_question(client):
    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'question' in data
    assert 'answer' in data
    assert data['question'] == 'What is the capital of France?'
    assert data['answer'] is not None