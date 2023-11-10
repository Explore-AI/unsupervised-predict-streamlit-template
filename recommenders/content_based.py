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
from sklearn.metrics.pairwise import linear_kernel
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
    # Initializing the empty list of recommended movies
    recommended_movies = []
    data = data_preprocessing(30000)
    # Instantiating and generating the count matrix
    tf_vec = TfidfVectorizer(strip_accents='unicode')
    tfidf_matrix = tf_vec.fit_transform(data['keyWords'])
    cos_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(data.index, index=data['title']).drop_duplicates()

    def get_rec_list(movie_list, cos_sim=cos_sim):
        idx = []
        for title in movie_list:
            idx.append(indices[title])

        # get the pairwise similarity scores
        sim_scores1 = list(enumerate(cos_sim[idx[0]]))
        sim_scores2 = list(enumerate(cos_sim[idx[1]]))
        sim_scores3 = list(enumerate(cos_sim[idx[2]]))

        # sort movies
        sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
        sim_scores2 = sorted(sim_scores2, key=lambda x: x[1], reverse=True)
        sim_scores3 = sorted(sim_scores3, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores1[:10] + sim_scores2[:10] + sim_scores3[:10]
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # scores of the most similar movies
        sim_scores = sim_scores[1:20]

        # movies indices
        movie_indices = [i[0] for i in sim_scores]
        movie_indices = [i for i in movie_indices if i not in idx]

        # top 10 most similar movies
        return data['title'].iloc[movie_indices]

    # Store movie names
    recommended_movies = get_rec_list(movie_list)

    return recommended_movies[:10]