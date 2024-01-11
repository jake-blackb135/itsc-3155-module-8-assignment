# TODO: Feature 2
from src.models.movie import Movie

# test_case
def test_movie_model():
    movie = Movie('The Incredible Hulk', 'Louis Terrier', 7)

    assert type(movie) == Movie
    assert movie.title == 'The Incredible Hulk'
    assert movie.director == 'Louis Terrier'
    assert movie.rating == 7

# test_case_2
def test_movie_model_2():
    movie = Movie('The Dark Knight', 'Christopher Nolan', 9)

    assert type(movie) == Movie
    assert movie.title == 'The Dark Knight'
    assert movie.director == 'Christopher Nolan'
    assert movie.rating != '9'

# test_case_3
def test_movie_model_3():
    movie = Movie('Saving Private Ryan', 'Steven Spielberg', 8)

    assert type(movie) == Movie
    assert movie.title != 'saving private ryan'
    assert movie.director != 'George Lucas'
    assert movie.rating == 8

# test_case_4
def test_movie_model_4():
    movie = Movie('Transformers', 'Michael Bay', 4)

    assert type(movie) == Movie
    assert movie.title == 'Transformers'
    assert movie.director != 'Michael B@y'
    assert movie.rating != ''

# test_case_5
def test_movie_model_5():
    movie = Movie('Toy Story', 'John Lasseter', 10)

    assert type(movie) == Movie
    assert movie.title != ''
    assert movie.director != ''
    assert movie.rating != 2