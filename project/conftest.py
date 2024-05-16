import pytest
from main import app
from models import User, Flashcard


@pytest.fixture
def test_client():
    flask_app = app.test_client()
    yield flask_app
    
@pytest.fixture
def login(test_client):
    response = test_client.post('/login', data={'email': 'testuser@test', 'password': 'password'}, follow_redirects = True)
    yield response
    
@pytest.fixture
def create_user():
    user = User(email="testuser@test.com", password="password", name="testuser")
    return user

@pytest.fixture
def create_flashcard():
    flashcard = Flashcard(question="What is 2+2?", answer="4", topic="Math", user_id=1)
    return flashcard