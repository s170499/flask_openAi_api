import pytest
import requests

@pytest.fixture
def app_url():
    return 'http://localhost:8000/ask'

def test_ask_question(app_url):
    question = 'What is the capital of France?'

    response = requests.post(app_url, json={'question': question})
    assert response.status_code == 200

    data = response.json()
    assert 'question' in data
    assert 'answer' in data
    assert data['question'] == question
    assert data['answer']

if __name__ == '__main__':
    pytest.main()