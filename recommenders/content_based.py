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
from sklearn.feature_extraction.text import TfidfVectorizer

# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',')
ratings = pd.read_csv('resources/data/ratings.csv')
movies.dropna(inplace=True)

def data_preprocessing(subset_size):
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
    # Split genre data into individual words.
    movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    # Subset of the data
    movies_subset = movies[:subset_size]
    return movies_subset

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
   # Convert the movie genres into a single string for each movie
    movies['genres'] = movies['genres'].str.replace('|', ' ')

    # Combine genres to create movie descriptions
    movies['description'] = movies['genres']

    # Convert the movie descriptions into a Tfidf matrix
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies['description'])

    # Get the indices of the selected favorite movies
    idx_movies = movies[movies['title'].isin(movie_list)].index.tolist()

    # Calculate similarity scores between the selected favorite movies and all other movies
    similarity_scores = cosine_similarity(tfidf_matrix[idx_movies], tfidf_matrix)

    # Get the average similarity scores for each movie across the selected favorite movies
    avg_similarity_scores = similarity_scores.mean(axis=0)

    # Get the indices of the top_n recommended movies based on the average similarity scores
    top_n_indices = avg_similarity_scores.argsort()[::-1][:top_n]

    # Get the titles of the top_n recommended movies
    recommended_movies = movies.iloc[top_n_indices]['title'].tolist()

    return recommended_movies