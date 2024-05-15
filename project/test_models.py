from models import User, Flashcard
def test_hashed_password():
    user = User(email="raajvir@gmail.com", password="password", name="Raajvir")
    assert user.email == "raajvir@gmail.com"
    assert user.password != "password"
    assert user.name == "Raajvir"