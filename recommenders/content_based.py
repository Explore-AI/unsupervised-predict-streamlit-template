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
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies = pd.read_csv('./resources/data/movies.csv', sep = ',')
ratings = pd.read_csv('./resources/data/ratings.csv')
movies.dropna(inplace=True)

def data_preprocessing(df):
    """Prepare data for use within Content filtering algorithm.
    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.
    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.
    """
    movies = df.copy()
    # Split genre data into individual words.
    movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    movies['genres'] = movies['genres'].apply(str).apply(lambda x: x.split('|'))
    return movies

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.

    """
    #global movies
    # removing the favorite movie list
    nmovies = data_preprocessing(movies)
    genre_list = []
    for i in movie_list:
        genre_list.append(list(nmovies[nmovies['title']==i]['genres'])[0])



    from sklearn.preprocessing import MultiLabelBinarizer
    mlb2 =  MultiLabelBinarizer()
    mlb2.fit_transform(genre_list)
    genre_list = mlb2.classes_
    nmovies = nmovies[~nmovies['title'].isin(movie_list)]
    mgen = nmovies
    for gen in genre_list:
        mgen = mgen[mgen['keyWords'].str.contains(gen)]
        if len(mgen)<=top_n:
            break

        mgen2 = mgen


    asscr = ratings[ratings['movieId'].isin(mgen2['movieId'].values)][['movieId', 'rating']]
    top_movies = (asscr.groupby(['movieId']).mean().reset_index()).sort_values('rating', ascending =False)[:top_n]
    return list((nmovies[nmovies['movieId'].isin(top_movies['movieId'].values)]['title']).values)
