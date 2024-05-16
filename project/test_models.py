from models import User, Flashcard
from conftest import create_user, create_flashcard

def test_hashed_password(create_user):
    assert create_user.email == "testuser@test.com"
    assert create_user.password != "password"
    assert create_user.name == "testuser"
    
def test_flashcard(create_flashcard):
    assert create_flashcard.question == "What is 2+2?"
    assert create_flashcard.answer == "4"
    