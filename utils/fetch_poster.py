"""

    links dataset.

    Author: Team_ES2.

    Note:
    ---------------------------------------------------------------------
    This function uses the requests library to make a GET request to the 
    Movie Database (TMDb) API, using a provided movie ID and API key. 
    The response from the API is in JSON format, and the function extracts
    the 'poster_path' field. The path is then concatenated with a base URL 
    to form the full poster URL. In case of any exception like invalid 
    movie_id or API key, it returns a default image URL
    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""
import os
import pandas as pd
from IPython.display import Image, HTML
import json


df_links = pd.read_csv('resources/data/links.csv')

def fetch_poster(movie_id):
    """generate poster link based on id"""
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data_link = requests.get(url)
        data_link = data_link.json()
        poster_path = data_link['poster_path']
        base_poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
        return base_poster_url
    except :
        return "https://i5.walmartimages.com/asr/4add4de6-7b92-4846-8316-b7a0cbec4dc7_1.8e2f7305081b9284e56d112fe146dc90.png"
    
    
def get_links(string):
    length = len(str(string))
    return "https://www.imdb.com/title/tt"+"0"*(7 - length)+str(string)+"/"


# the following codes takes time to run, the results has been saved as Links_2.csv
#links["images"] = links["tmdbId"].apply(fetch_poster)
#df_links["link"] = df_links["imdbId"].apply(get_links)













