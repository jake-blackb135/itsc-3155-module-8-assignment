# TODO: Feature 3
from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton

def test_get_movie_by_title():
    movie = movie_repository_singleton.create_movie("Up","Pete Docter",10)
    mov = movie_repository_singleton.get_movie_by_title("Up")
    assert movie == mov

    mov = movie_repository_singleton.get_movie_by_title("")
    assert mov == None

    mov = movie_repository_singleton.get_movie_by_title("Down")
    assert mov == None

    

def test_get_movie_by_title2():
    movie = movie_repository_singleton.create_movie("Up","Pete Docter",10)
    movie2 = movie_repository_singleton.create_movie("The Fellowship of the Ring","Peter Jackson",10)

    mov = movie_repository_singleton.get_movie_by_title("The Fellowship of the Ring")
    assert movie2 == mov

    