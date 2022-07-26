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
movies = pd.read_csv('./resources/data/movies.csv' ,sep = ',')
ratings_data = pd.read_csv('./resources/data/ratings.csv')

#Drop Timestamp from rating_data
ratings_data.drop(['timestamp'], axis=1, inplace=True)

#Merge dataframes rating_df and movies
ratings = ratings_data.merge(movies[['movieId', 'title']], on='movieId')

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model=pickle.load(open('./resources/models/SVD_model.pkl', 'rb'))

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
    # Data preprosessing
    reader = Reader(rating_scale=(0, 5))
    load_df = Dataset.load_from_df(ratings_data,reader)
    a_train = load_df.build_full_trainset()

    predictions = []
    for ui in a_train.all_users():
        predictions.append(model.predict(iid=item_id,uid=ui, verbose = False))
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
    id_store=[]
    # For each movie selected by a user of the app,
    # predict a corresponding user within the dataset with the highest rating
    for i in movie_list:
        movieid = movies[movies['title'] == i]['movieId'].values[0]
        predictions = prediction_item(item_id = movieid)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # Take the top 10 user id's from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.append(pred.uid)
    # Return a list of user id's
    return id_store


def get_user_movies(data, user_list):
    """
    Func returns list of movies
    :param data , user_list:
    :return: dataframe subset of train data
    """
    temp = pd.DataFrame()
    for i in user_list:
        temp_df = data[data['userId'] == i]
        temp = temp.append(temp_df)
    return temp

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


    user_ids = pred_movies(movie_list)

    temp = get_user_movies(ratings, user_ids)

    movie_ids = []

    for i in movie_list:
        #Get movieId from tittle
        movieID = movies[movies['title']==i]['movieId'].values[0]
        movie_ids.append(movieID)

    # Add new user with ratings to userlist
    new_user_row1 = {'userId': 1000000, 'movieId': movie_ids[0], 
            'rating': 5.0, 'title': movie_list[0]}
    new_user_row2 = {'userId': 1000000, 'movieId': movie_ids[1], 
            'rating': 5.0, 'title': movie_list[1]}
    new_user_row3 = {'userId': 1000000, 'movieId': movie_ids[2], 
            'rating': 5.0, 'title': movie_list[2]}
    temp = temp.append([new_user_row1, new_user_row2, new_user_row3], 
            ignore_index=True)

    # create pivot table
    user_ratings = temp.pivot_table(index='userId', columns='title', 
            values='rating').fillna(0)
    # compute correlations from pivot table
    item_similarity_df = user_ratings.corr(method='pearson')

    def get_similar_movies(movie_name, user_rating=5):
        """
        Func returns a list of similar movies
        Args:
            movie_name , user_rating
        Returns:
            list of similar movies
        """
        similar_score = item_similarity_df[movie_name] * user_rating
        similar_score = similar_score.sort_values(ascending=False)
        return similar_score

    similar_movies = pd.DataFrame()

    # get similar movies of fav movies
    for movie in movie_list:
        similar_movies = similar_movies.append(get_similar_movies(movie, 5), 
                ignore_index=True)

    recommended_movies = []
    # sum similarities together append highest values
    for i in similar_movies.sum().sort_values(ascending=False).index:
        if i in movie_list:
            pass
        else:
            recommended_movies.append(i)

    return recommended_movies[:10]
