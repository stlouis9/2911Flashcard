from main import app
from db import db
from models import User

def create_all_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_all_tables()
