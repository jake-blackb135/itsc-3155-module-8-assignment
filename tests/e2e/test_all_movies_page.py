# TODO: Feature 1
from flask.testing import FlaskClient

def test_all_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<table class="table table-bordered">' in response_data
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response_data
    assert b'<h1 class="mb-5">All Movies</h1>' in response_data
    assert b'<select class="dropdown" name="r" id="r">' not in response_data