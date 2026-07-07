""" This module handles all requests and queries tied to flask routes."""

import os
from flask import Flask, render_template, request, redirect, url_for, abort
import movie_service
from data_manager import DataManager
from models import db, Movie

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"sqlite:///{os.path.join(basedir, 'data/moviestack.db')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app.

data_manager = DataManager() # Create an object of your DataManager class

@app.route('/')
def index():
    """ Display the main page with all existing users. """
    users = data_manager.get_users()

    return render_template('index.html', users=users)

@app.route('/users', methods=['POST'])
def create_user():
    """ Create a new user and add it to the database."""
    username = request.form.get("username", "").strip()

    if not username:
        return redirect(url_for("index"))

    data_manager.create_user(username)

    return redirect(url_for("index"))

@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_user_movies(user_id):
    """Displays a list of movies owned by a user."""
    user = data_manager.get_user(user_id)
    movies = data_manager.get_movies(user_id)

    if user is None:
        abort(404)

    return render_template(
        "movies.html",
        user=user,
        movies=movies
    )

@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """Add a new movie to a user’s list of favorite movies."""
    title = request.form.get("title", "").strip()
    year = request.form.get("year", "").strip()

    if not title:
        return redirect(url_for("get_user_movies", user_id=user_id))

    movie_data = movie_service.get_movie_from_omdb(
        title,
        year if year else None
    )

    if movie_data is None:
        movie = Movie(
            name=title,
            user_id=user_id
        )
    else:
        movie = Movie(
            name=movie_data["name"],
            year=movie_data["year"],
            director=movie_data["director"],
            imdb_id=movie_data["imdb_id"],
            poster_url=movie_data["poster_url"],
            user_id=user_id
        )

    data_manager.add_movie(movie)

    return redirect(url_for("get_user_movies", user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update',
           methods=['POST'])
def update_movie(user_id,movie_id):
    """Modify the title of a specific movie in a user’s list, without
    depending on OMDb for corrections."""
    new_title = request.form.get("title", "").strip()

    if not new_title:
        return redirect(url_for("get_user_movies", user_id=user_id))

    data_manager.update_movie(movie_id, new_title)

    return redirect(url_for("get_user_movies", user_id=user_id))

@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete',
           methods=['POST'])
def delete_movie(user_id,movie_id):
    """Remove a specific movie from a user’s favorite movie list."""
    data_manager.delete_movie(movie_id)

    return redirect(url_for("get_user_movies", user_id=user_id))


if __name__ == "__main__":
    # One-time creation of database
    # with app.app_context():
    #     db.create_all()

    app.run()
