# TODO: Feature 3
from flask.testing import FlaskClient

def test_search_movies(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
    assert b'<p class="mb-3">Search for a movie rating below</p>' in response_data
    assert b'<button type="submit"  class="btn btn-primary">Submit</button>' in response_data
