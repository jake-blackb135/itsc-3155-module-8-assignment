# TODO: Feature 2
from flask.testing import FlaskClient


def test_create_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data

    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response_data
    assert b'<p class="mb-3">Create a movie rating below</p>' in response_data
    assert b'<input type="text" class="form-control w-50" name="t" id="t" placeholder="Enter the title of the movie..." autocomplete="off">' in response_data
    assert b'<select class="dropdown" name="r" id="r">' in response_data

    assert b'<h2 class="mb-5">Create Movie Rating</h1>' not in response_data
    assert b'<p class="mb-5">Create a movie rating below</p>' not in response_data
    assert b'<input type="text" class="form-control w-50" name="t" id="t" placeholder="..." autocomplete="off">' not in response_data
    assert b'<select class="dropdown" name="R" id="r">' not in response_data