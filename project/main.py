from flask import Flask, render_template, jsonify, request, redirect, url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
from db import db
from models import User, Flashcard
from flask_login import LoginManager,login_user,login_required,current_user,logout_user
import csv


app = Flask(__name__, static_folder='templates/assets')
app.config['SECRET_KEY'] = 'flashwizard'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashwizard.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)


# routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    # statement = db.select(Flashcard).where(Flashcard.user_id == current_user.id)
    # records = db.session.execute(statement)
    # flashcards = records.scalars()
    flashcards = Flashcard.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', name=current_user.name, flashcards=flashcards)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('profile'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    question = request.form.get('question')
    answer = request.form.get('answer')
    topic = request.form.get('topic')
    flashcard = Flashcard(question=question, answer=answer, topic=topic, user_id=current_user.id)
    db.session.add(flashcard)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/delete_flashcard', methods=['POST'])
def delete_flashcard():
    flashcard_id = request.form.get('flashcard_id')
    flashcard = Flashcard.query.get(flashcard_id)
    if flashcard:
        db.session.delete(flashcard)
        db.session.commit()
    return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run(debug=True,port=5000)
