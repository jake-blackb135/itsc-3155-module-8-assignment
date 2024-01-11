from asyncio.windows_events import NULL
import re
from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

#renders the home page
@app.get('/')
def index():
    return render_template('index.html')


#method to get the list of all Movies in the database
@app.get('/movies')
def list_all_movies():
    movie_list = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie_list=movie_list)


# Renders the new movie page
@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


#method to add new movie to the database
@app.post('/movies')
def create_movie():
    #Collects user input
    movieInfo = None
    t = request.form.get('t')
    d = request.form.get('d')
    r = request.form.get('r')
    
    #Creates new movie using user Data and adds it to the database
    if t != None and t != '' and d != None and d != '' and r != None and r != '':
        movieInfo = movie_repository_singleton.create_movie(t, d, int(r))
    else:
        return render_template('create_movies_form.html', create_rating_active=True)
    
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    #Searches the database for any movie matching the title the user searches
    title = request.args.get('title')
    if title != None and title != '':
        movies = movie_repository_singleton.get_movies_by_title(title)
        

        #If a movie is found renders the page again with the movie the user searched for
        if movies != None:
            return render_template('search_movies.html', movies=movies)
            
        return render_template('search_movies.html', search_active=True, title='')
      
    else:
        return render_template('search_movies.html', search_active=True, title='')
