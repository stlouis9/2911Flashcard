from main import app
from conftest import test_client, login

def test_index(test_client):
    response = test_client.get('/')  # Make GET request to root URL
    assert response.status_code == 200  # Check status code
    assert b"FLASHWIZARD" in response.data
    
    
def test_login(test_client):  # Create test client
    response = test_client.get('/login', data={'email': 'testuser@test', 'password': 'password'})  # Make GET request to login URL
    assert response.status_code == 200  # Check status code
    assert b"Login" in response.data  # Check if the login page is rendered    


def test_logout(test_client, login):
    
    assert login.status_code == 200
    
    # Make GET request to logout URL
    logout_response = test_client.get('/logout')
    
    assert logout_response.status_code == 200
    # Check if the user is redirected to the logout page after logging out
    assert b"logged out" in logout_response.data

def test_signup(test_client):
    response = test_client.post('/signup', data={'email': 'testuser@test', 'password': 'password', 'name': 'testuser'}, follow_redirects = True)  # Make GET request to signup URL
    assert response.status_code == 200  # Check status code
    assert b"Sign Up" in response.data  # Check if the signup page is rendered
   
def test_profile(test_client, login):
    assert login.status_code == 200
    response = test_client.get('/profile', follow_redirects = True)  # Make GET request to profile URL
    assert response.status_code == 200  # Check status code # Check if the profile page is rendered
    assert b"Welcome" in response.data  # Check if the flashcards section is rendered

def test_add_flashcards(test_client, login):
    assert login.status_code == 200
    response = test_client.post('/add_flashcard', data={'question': 'Hello', 'answer': 'World', 'topic': 'test'}, follow_redirects = True)
    assert response.status_code == 200  # Check status code
    assert b"Hello" in response.data  # Check if the flashcards page is rendered