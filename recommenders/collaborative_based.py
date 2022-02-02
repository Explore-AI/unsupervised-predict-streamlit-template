"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
import random
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer


# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',')
ratings = pd.read_csv('resources/data/ratings.csv')
movies.dropna(inplace=True)


def data_preprocessing(data):
    """ Preprocess data for use within for content-based filtering algorithm.
    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.
    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.
    """
    movies = data.copy()
    # Separate genre using a ',' instead of '|'.
    movies['bag_of_words'] = movies['genres'].str.replace('|', ' ')

    movies['genres'] = movies['genres'].apply(str).apply(lambda x: x.split('|'))
    return movies

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def collab_model(movie_list,top_n=10):
    """
    Performs Content filtering using a list of movies supplied
       by the app user.
    Parameters
    ----------
    movie_list : list (str)
        Favorite movies selected by the app user.
    top_n : type
        number of top recommendations to return to the user.
    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.
    """
    #global movies
    # removing the favorite movie list
    nmovies = data_preprocessing(movies)
    genre_list = []
    for i in movie_list:
        genre_list.append(list(nmovies[nmovies['title']==i]['genres'])[0])
    


    #instantiate the multilabelbinarizer for sparsity
    mlb =  MultiLabelBinarizer()
    mlb.fit_transform(genre_list)
    genre_list = mlb.classes_
    nmovies = nmovies[~nmovies['title'].isin(movie_list)] # remove selected movies
    mgen = nmovies

    #looping over genres for similarity
    for gen in genre_list:

        mgen = mgen[mgen['bag_of_words'].str.contains(gen)]

        if len(mgen)<=top_n:

            break
            
        mgen2 = mgen
        
        
    asscr = ratings[ratings['movieId'].isin(mgen2['movieId'].values)][['movieId', 'rating']]

    top_movies = (asscr.groupby(['movieId']).mean().reset_index()).sort_values('rating', ascending =False)[:top_n + 5]
    top_list = list((nmovies[nmovies['movieId'].isin(top_movies['movieId'].values)]['title']).values)

    return random.sample(top_list, top_n)