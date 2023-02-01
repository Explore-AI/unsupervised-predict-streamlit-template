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
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)
movies_df.dropna(inplace=True)

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model=pickle.load(open('resources/models/SVD.pkl', 'rb'))

def collab_model(movie_list, top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
    by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : int
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    # Map movie titles to movie ids
    movie_ids = []
    for movie in movie_list:
        movie_id = movies_df.loc[movies_df['title'] == movie, 'movieId'].iloc[0]
        movie_ids.append(movie_id)

    # Filter ratings_df to only include ratings for the selected movies
    df_init_users = ratings_df[ratings_df['movieId'].isin(movie_ids)].pivot(index='userId', columns='movieId', values='rating').fillna(0)

    # Calculate cosine similarity between users based on the selected movies
    cosine_sim = cosine_similarity(df_init_users, df_init_users)

    # Get the indices of the selected movies in the movies_df DataFrame
    movie_idx = [movies_df[movies_df['movieId'] == movie_id].index[0] for movie_id in movie_ids]

    # Create a list of tuples containing the index and similarity score for each movie
    similarity_scores = []
    for i, sim in enumerate(cosine_sim[movie_idx[0]]):
        similarity_scores.append((i, sim))

    # Sort the list of tuples based on similarity score in descending order
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the movies to recommend (excluding the selected movies)
    recommend_indices = [i for i, sim in similarity_scores if i not in movie_idx][:top_n]

    # Map movie indices to movie titles
    recommended_movies = [movies_df.iloc[i]['title'] for i in recommend_indices]

    return recommended_movies
