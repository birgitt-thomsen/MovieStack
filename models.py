from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Movie(db.Model):
    __table_args__ = (
        db.UniqueConstraint("user_id", "imdb_id"),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.Integer)
    imdb_id = db.Column(db.String(10), nullable=False)
    poster_url = db.Column(db.String(500))

    # Link Movie to User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
