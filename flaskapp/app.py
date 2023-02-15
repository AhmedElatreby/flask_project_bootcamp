import flask
from flask import jsonify, request
import sqlalchemy
from flaskapp import database, models
from flaskapp.database import dbSession
from flaskapp.models import Movie

app = flask.Flask(__name__)
database.initdb()


@app.route('/add_movie', methods=['POST'])
def add_movie():
    if request.method == 'POST':
        return 'Done', 201
    else:
        return 'Error', 400


@app.route('/movies')
def movies():
    movie_list = Movie.query.all()
    movies = []
    for movie in movie_list:
        movies.append({'id': movie.id, 'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})


@app.route('/movies/a')
def movies_beginning_with_a():
    movie_list = Movie.query.filter(Movie.title.like('A%')).all()
    movies = []
    for movie in movie_list:
        movies.append({'id': movie.id, 'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})


@app.route('/movies/order_by_rating')
def movies_order_by_rating():
    movie_list = Movie.query.order_by(Movie.rating.desc()).all()
    movies = []
    for movie in movie_list:
        movies.append({'id': movie.id, 'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})


@app.route('/movies/<int:rating>')
def get_movies_by_rating(rating):
    movie_list = Movie.query.filter(Movie.rating == rating).all()
    if not movie_list:
        return jsonify({'message': 'There are no {} Star movies in the database'.format(rating)})
    else:
        movies = []
        for movie in movie_list:
            movies.append({'id': movie.id, 'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})
