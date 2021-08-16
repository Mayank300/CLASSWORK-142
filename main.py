from flask import Flask, request, jsonify
import csv

all_movies = []

with open('movie.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

app = Flask(__name__)

@app.route('/get-movies')

def get_movies():
    return jsonify({
        'name': all_movies[0],
        'status': '😻',
    })

liked_movies = []
disliked_movies = []
unwatched_movies = []

@app.route('/liked-movies', methods=['POST'])

def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status': 'success',
    }),200

@app.route('/disliked-movies', methods=['POST'])
 
def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        'status': 'success',
    }),200


@app.route('/unwatched-movies', methods=['POST'])
 
def unwatched_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unwatched_movies.append(movie)
    return jsonify({
        'status': 'success',
    }),200

