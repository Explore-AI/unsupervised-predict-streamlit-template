import requests
import pandas as pd



def fetch_poster(movie_id):
        data_URL = 'http://www.omdbapi.com/?apikey=ff072698'
        params = {
            'i': movie_id
        }
        data = requests.get(data_URL,params=params).json()
        full_path = (data['Poster'])
        return full_path

def fetch_runtime(movie_id):
        data_URL = 'http://www.omdbapi.com/?apikey=ff072698'
        params = {
            'i': movie_id
        }
        data = requests.get(data_URL,params=params).json()
        full_path = (data['Runtime'])
        return full_path
    
def fetch_imdbrating(movie_id):
    data_URL = 'http://www.omdbapi.com/?apikey=ff072698'
    params = {
        'i': movie_id
    }
    data = requests.get(data_URL,params=params).json()
    full_path = (data['imdbRating'])
    return full_path

def fetch_plot(movie_id):
        data_URL = 'http://www.omdbapi.com/?apikey=ff072698'
        params = {
            'i': movie_id
        }
        data = requests.get(data_URL,params=params).json()
        full_path = (data['Plot'])
        return full_path

def fetch_genre(movie_id):
    data_URL = 'http://www.omdbapi.com/?apikey=ff072698'
    params = {
        'i': movie_id
    }
    data = requests.get(data_URL,params=params).json()
    full_path = (data['Genre'])
    return full_path