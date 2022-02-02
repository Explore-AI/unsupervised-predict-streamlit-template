"""

    Collaborative-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `collab_model` !!

    You must however change its contents (i.e. add your own collaborative
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import pandas as pd
import os
import numpy as np
import pickle
import copy
import random
from surprise import Reader, Dataset
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data


movies_df = pd.read_csv('resources/data/movies.csv', usecols=['movieId','title'], dtype={'movieId':'int32','title':'str'})

movies_df = movies_df[:27000]

ratings_df = pd.read_csv('resources/data/ratings.csv',
    usecols  =['userId', 'movieId', 'rating'],dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

ratings_df = ratings_df[:30000]



# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model_knn = pickle.load(open('resources/models/model_kn_1.pkl', 'rb'))


def data_preprocessing(movies_df,ratings_df):
    """Map a given favourite movie to users within the
       MovieLens dataset with the same preference.

    Parameters
    ----------
    movies : dataframe
        movie data.
    ratings : dataframe
        ratings data
    Returns
    -------
    dataframe
        matrix of high rated movies.

    """
    # Data preprocessing
    movies_merged_df = movies_df[14900:15200].merge(ratings_df, on = 'movieId')
    movies_average_rating=movies_merged_df.groupby('title')['rating'].mean().sort_values(ascending=False).reset_index().rename(columns={'rating':'Average Rating'})
    movies_rating_count=movies_merged_df.groupby('title')['rating'].count().sort_values(ascending=True).reset_index().rename(columns={'rating':'Rating Count'}) #ascending=False
    rating_with_RatingCount = movies_merged_df.merge(movies_rating_count, left_on = 'title', right_on = 'title', how = 'left')
    popularity_threshold = 0
    popular_movies= rating_with_RatingCount[rating_with_RatingCount['Rating Count']>=popularity_threshold]
    
    return popular_movies


# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def collab_model(movie_list,top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
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
    popular_movies = data_preprocessing(movies_df,ratings_df)
    movie_features_df = popular_movies.pivot_table(index='title',columns='userId',values='rating').fillna(0)
    movie_features_df_matrix = csr_matrix(movie_features_df.values)
    df = movie_features_df


    movies_1 = []

    for i in range(0,len(movie_list)):

        t = movie_list[i]
        base = df.index.get_loc(t)

        query_index = base
        distances, indices = model_knn.kneighbors(movie_features_df.
                     iloc[query_index,:].values.reshape(1, -1),n_neighbors = 6)
  
        for i in range(0, len(distances.flatten())):

            if i != 0:
                movies_1.append(movie_features_df.index[indices.flatten()[i]])
    
            recommended_movies = movies_1

    #recommended_movies = random.sample(recommended_movie, 10)

    
    return recommended_movies
