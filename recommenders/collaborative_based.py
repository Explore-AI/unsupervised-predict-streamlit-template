
# Script dependencies
import pandas as pd
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import random

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

#Data Preprocessing
pred_movies = pd.merge(ratings_df,movies_df, on= 'movieId', how = 'left')
pred_movies= pred_movies.drop(['genres','rating','userId'], axis = 1)
pred_movies= pred_movies.drop_duplicates()
pred_movies = pred_movies.dropna()
movietitle = pred_movies.copy()

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model_load_path = "resources/models/SVD.pkl"
with open(model_load_path,'rb') as file:
    model_tuned = pickle.load(file)

def prediction_item(item_id):
    """Map a given favourite movie to users within the
       MovieLens dataset with the same preference.
    Parameters
    ----------
    item_id : int
        A MovieLens Movie ID.
    Returns
    -------
    list
        User IDs of users with similar high ratings for the given movie.
    """
    #Data preprosessing
    reader = Reader(rating_scale=(0, 5))
    load_df = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
    a_train = load_df.build_full_trainset()

    predictions = []
    for ui in a_train.all_users():
        predictions.append(model_tuned.predict(iid=item_id, uid=ui, verbose=False))
    return predictions

def pred_movies(movie_list):
    """Maps the given favourite movies selected within the app to corresponding
    users within the MovieLens dataset.
    Parameters
    ----------
    movie_list : list
        Three favourite movies selected by the app user.
    Returns
    -------
    list
        User-ID's of users with similar high ratings for each movie.
    """
    # Store the id of users
    id_store = []
    # For each movie selected by a user of the app,
    # predict a corresponding user within the dataset with the highest rating
    for i in movie_list:
        # movie_id = movietitle[movietitle['title'] == i]['movieId'].values[0]
        predictions = prediction_item(item_id=i)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # Take the top 10 user id's from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.append(pred.uid)
    # Return a list of user id's
    return id_store

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

    movie_ids = pred_movies(movie_list)
    df_init_users = ratings_df[ratings_df['userId'] == movie_ids[0]]
    for i in movie_ids[1:]:
        df_init_users = df_init_users.append(ratings_df[ratings_df['userId'] == i])

    # Getting the user-item matrix
    df_init_users = pd.merge(df_init_users, movietitle, on='movieId', how='left')
    df_init_users = df_init_users.dropna()
    users_matrix = df_init_users.groupby(['title', 'userId'])['rating'].max().unstack()
    for i in movie_list:
        if i not in users_matrix.index.values.tolist():
            df_nan = pd.DataFrame([[(np.NaN)] * len(users_matrix.columns)], index=[i], columns=users_matrix.columns)
            users_matrix = users_matrix.append(df_nan)

    # Getting the cosine similarity matrix
    cosine_sim = cosine_similarity(users_matrix.fillna(0))
    indices = pd.Series(users_matrix.index)
    idx_1 = indices[indices == movie_list[0]].index[0]
    idx_2 = indices[indices == movie_list[1]].index[0]
    idx_3 = indices[indices == movie_list[2]].index[0]

    # Creating a Series with the similarity scores in descending order
    rank_1 = cosine_sim[idx_1]
    rank_2 = cosine_sim[idx_2]
    rank_3 = cosine_sim[idx_3]

    # Calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending=False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending=False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending=False)

    # Appending the names of movies
    listings = score_series_1.append(score_series_2).append(score_series_3).sort_values(ascending=False)
    recommended_movies = []

    # Choose top 50
    top_50_indx = list(listings.iloc[1:50].index)

    # Removing chosen movies
    top_indx = np.setdiff1d(top_50_indx, [idx_1, idx_2, idx_3])
    random.shuffle(top_indx)
    for j in top_indx[:top_n]:
        recommended_movies.append(indices[j])

    return recommended_movies
