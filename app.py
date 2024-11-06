from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)


# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lecture2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize db and flask migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(50), nullable=False)
    subject_code = db.Column(db.String(10), nullable=True)

# configure routes and view


@app.route('/')
def index():
    name = "Ifraheem"
    return render_template('index.html', name=name)


@app.route('/save_data', methods=['POST'])
def save_user():
    username = request.form['username']
    email = request.form['email']

    new_user = User(username=username, email=email)

    db.session.add(new_user)
    db.session.commit()

    print("i got a form. ")
    return 'data has been saved.'


if __name__ == '__main__':
    app.run(debug=True)
