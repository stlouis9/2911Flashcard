import manage
from main import app
from db import db
from unittest.mock import MagicMock

def test_manage_creates_all_tables():
    db.create_all = MagicMock() 
    with app.app_context():
        manage.create_all_tables()  
    db.create_all.assert_called_once()