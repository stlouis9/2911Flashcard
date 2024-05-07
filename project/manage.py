from main import app
from db import db
from models import User
db.create_all(app=app)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()