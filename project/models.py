from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import mapped_column, relationship
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))