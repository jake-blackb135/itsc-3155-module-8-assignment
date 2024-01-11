# TODO: Feature 1
from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton

def test_get_movie_list():
    movie_list = movie_repository_singleton.get_all_movies()
    movie1 = Movie('The Incredible Hulk', 'Louis Terrier', 7)
    movie_list.append(movie1)
    movie2 = Movie('Transformers', 'Michael Bay', 4)
    movie_list.append(movie2)
    movie3 = Movie('Toy Story', 'John Lasseter', 10)
    movie_list.append(movie3)
    movie4 = Movie('The Dark Knight', 'Christopher Nolan', 9)

    assert movie_list == [movie1, movie2, movie3]
    assert movie_list[1] == movie2
    assert movie_list[2] == movie3
    assert len(movie_list) == 3
    assert len(movie_list) != 5
    assert movie_list[0].director != 'Christopher Nolan'
    assert movie_list[1].rating == 4
    assert movie_list[2] != movie4
    