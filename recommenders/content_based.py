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
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',',delimiter=',')
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
    #Initiate an empty list for the genres
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
    data = data_preprocessing(27000)
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(data['keyWords'])
    cosine_sim = linear_kernel(count_matrix, count_matrix)
    indices = pd.Series(data.index, index=data['title']).drop_duplicates()
    # Initializing the empty list of recommended movies
    idx0 = indices[movie_list[0]]
    idx1 = indices[movie_list[1]]
    idx2 = indices[movie_list[2]]
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores0 = list(enumerate(cosine_sim[idx0]))
    sim_scores1 = list(enumerate(cosine_sim[idx1]))
    sim_scores2 = list(enumerate(cosine_sim[idx2]))

    # Sort the movies based on the similarity scores
    sim_scores0 = sorted(sim_scores0, key=lambda x: x[1], reverse=True)
    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
    sim_scores2 = sorted(sim_scores2, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores0 + sim_scores1 + sim_scores2

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:top_n+1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return data['title'].iloc[movie_indices].tolist()
