from main import app
from conftest import test_client, login

def test_index(test_client):
    response = test_client.get('/')  
    assert response.status_code == 200  
    assert b"FLASHWIZARD" in response.data
    
    
def test_login(test_client): 
    response = test_client.get('/login', data={'email': 'testuser@test', 'password': 'password'})  
    assert response.status_code == 200  
    assert b"Login" in response.data   


def test_logout(test_client, login):
    
    assert login.status_code == 200
    logout_response = test_client.get('/logout', follow_redirects = True)
    assert logout_response.status_code == 200
    
    # length = len(logout_response.data)
 
    # # create a new string of last N characters
    # Str2 = logout_response.data[length - 500:]
    
    # # print Last N characters
    # print(Str2)
    
    # assert b"logged out" in logout_response.data

def test_signup(test_client):
    response = test_client.post('/signup', data={'email': 'testuser@test', 'password': 'password', 'name': 'testuser'}, follow_redirects = True)  # Make GET request to signup URL
    assert response.status_code == 200 
    assert b"Signup" in response.data  
   
def test_profile(test_client, login):
    assert login.status_code == 200
    response = test_client.get('/profile', follow_redirects = True) 
    assert response.status_code == 200 
    assert b"Flashcard" in response.data 

def test_add_flashcards(test_client, login):
    assert login.status_code == 200
    response = test_client.post('/add_flashcard', data={'question': 'Hello', 'answer': 'World', 'topic': 'test'}, follow_redirects = True)
    assert response.status_code == 200  
    assert b"Hello" in response.data

def test_signup_existing_email(test_client):
    response = test_client.post('/signup', data={'email': 'testuser@test', 'password': 'password', 'name': 'testuser'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Sign" in response.data

def test_login_incorrect_credentials(test_client):
    response = test_client.post('/login', data={'email': 'testuser@test', 'password': 'wrongpassword'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

def test_filter_flashcards(test_client, login):
    assert login.status_code == 200
    response = test_client.post('/filter_flashcards', data={'topic': 'test'}, follow_redirects=True)
    assert response.status_code == 200

def test_update_flashcard(test_client, login):
    assert login.status_code == 200
    response = test_client.post('/update_flashcard', data={'flashcard_id': '1', 'question': 'Updated Question', 'answer': 'Updated Answer', 'topic': 'Updated Topic'}, follow_redirects=True)
    assert response.status_code == 200










 