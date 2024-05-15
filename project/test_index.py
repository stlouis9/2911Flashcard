from main import app

def test_index():
    flask_app = app.test_client()  # Create test client
    response = flask_app.get('/')  # Make GET request to root URL
    assert response.status_code == 200  # Check status code
    assert b"FLASHWIZARD" in response.data