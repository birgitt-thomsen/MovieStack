""" This module handles all requests and queries tied to flask routes."""
import os
from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app.

data_manager = DataManager() # Create an object of your DataManager class

@app.route('/')
def index():
    """ Get a list of all registered users and pass them to index.html."""
    users = data_manager.get_users()

    return render_template('index.html', users=users)

@app.route('/users', methods=['POST'])
def create_user():
    """Get username from data form and pass it on to the create_user
    function in data_manager."""
    username = request.form.get("username", "").strip()

    if not username:
        return redirect(url_for("index"))

    data_manager.create_user(username)

    return redirect(url_for("index"))

@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_user_movies(user_id):
    """Clicking on a user name, the app retrieves that user’s list of favorite
    movies and displays it."""
    movies = data_manager.get_movies(user_id)
    return render_template(
        "movies.html",
        movies=movies
    )

@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """Add a new movie to a user’s list of favorite movies."""
    pass

@app.route('/users/<int:user_id>/movies/<int:movie_id>/update',
           methods=['POST'])
def update_movie(user_id,movie_id):
    """Modify the title of a specific movie in a user’s list, without
    depending on OMDb for corrections."""
    pass

@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete',
           methods=['POST'])
def delete_movie(user_id,movie_id):
    """Remove a specific movie from a user’s favorite movie list."""
    pass


if __name__ == "__main__":
    # One-time creation of database
    # with app.app_context():
    #     db.create_all()

    app.run()
