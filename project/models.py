from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import mapped_column, relationship
from werkzeug.security import generate_password_hash
from db import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    flashcards = relationship('Flashcard')
    
    def __init__(self, email, password, name):
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.name = name
    

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    answer = db.Column(db.String(1000))
    topic = db.Column(db.String(100))
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='flashcards')
    
    def __init__(self, question, answer, topic, user_id):
        self.question = question
        self.answer = answer
        self.topic = topic
        self.user_id = user_id