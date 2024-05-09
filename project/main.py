from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import User, Flashcard, Topic

db = SQLAlchemy()
app = Flask(__name__, static_folder='templates/assets')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    question = request.form.get('question')
    answer = request.form.get('answer')
    topic = request.form.get('topic')
    flashcard = Flashcard(question=question, answer=answer, topic=topic)
    db.session.add(flashcard)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/add_topic', methods=['POST'])
def add_topic():
    topic = request.form.get('topic')
    email = request.form.get('email')
    topic = Topic(topic=topic, email=email)
    db.session.add(topic)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True,port=5000)
