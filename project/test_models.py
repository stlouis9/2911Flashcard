from models import User, Flashcard
from conftest import create_user, create_flashcard
from main import app
from db import db

def test_hashed_password(create_user):
    assert create_user.email == "testuser@test.com"
    assert create_user.password != "password"
    assert create_user.name == "testuser"
    
def test_flashcard(create_flashcard):
    assert create_flashcard.question == "What is 2+2?"
    assert create_flashcard.answer == "4"

def test_user_flashcards(create_user):
    assert create_user.flashcards == []  

def test_flashcard_model(create_flashcard):
    assert create_flashcard.question == "What is 2+2?"
    assert create_flashcard.answer == "4"
    assert create_flashcard.topic == "Math"
    assert create_flashcard.user_id == 1  

def test_user_flashcards_relationship(create_user, create_flashcard):
    with app.app_context():
        create_user.flashcards.append(create_flashcard)
        db.session.commit()

        assert len(create_user.flashcards) == 1
        assert create_user.flashcards[0].question == "What is 2+2?"

def test_flashcard_user_relationship(create_user, create_flashcard):
    with app.app_context():
        create_flashcard.user = create_user
        db.session.commit()
        assert create_flashcard.user.email == "testuser@test.com"