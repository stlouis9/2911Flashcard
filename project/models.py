from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import mapped_column, relationship
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    email = db.Column(db.String(100), db.ForeignKey('user.email'))
    user = db.relationship('User', back_populates='topics')

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    answer = db.Column(db.String(1000))
    topic = db.Column(db.String(100))
    email = db.Column(db.String(100), db.ForeignKey('user.email'))
    user = db.relationship('User', back_populates='flashcards')