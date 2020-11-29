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
import scipy as sp
import pickle
import copy
from surprise import Reader, Dataset, SVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
#movies_df = pd.read_csv('/home/explore-student/unsupervised_data/unsupervised_movie_data/movies.csv',sep = ',',delimiter=',')
#ratings_df = pd.read_csv('/home/explore-student/unsupervised_data/unsupervised_movie_data/train.csv')
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',',delimiter=',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1, inplace=True)

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model=pickle.load(open('resources/models/SVD.pkl', 'rb'))

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
    load_df = Dataset.load_from_df(ratings_df,reader)
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
        predictions = prediction_item(item_id = i)
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
    names = movies_df.copy()
    names.set_index('movieId',inplace=True)
    indices = pd.Series(names['title'])
    users_ids = pred_movies(movie_list)
    # Get movie IDs and ratings for top users
    df_init_users = ratings_df[ratings_df['userId']==users_ids[0]]
    for i in users_ids[1:]:
        df_init_users = df_init_users.append(ratings_df[ratings_df['userId']==i])
    # Include predictions for chosen movies
    for j in movie_list:
        a = pd.DataFrame(prediction_item(j))
        for i in set(df_init_users['userId']):
            mid = indices[indices == j].index[0]
            est = a['est'][a['uid']==i].values[0]
            df_init_users = df_init_users.append(pd.Series([int(i),int(mid),est], index=['userId','movieId','rating']), ignore_index=True)
    # Remove duplicate entries
    df_init_users.drop_duplicates(inplace=True)
    #Create pivot table
    util_matrix = df_init_users.pivot_table(index=['userId'], columns=['movieId'], values='rating')
    # Fill Nan values with 0's and save the utility matrix in scipy's sparse matrix format
    util_matrix.fillna(0, inplace=True)
    util_matrix_sparse = sp.sparse.csr_matrix(util_matrix.values)
    # Compute the similarity matrix using the cosine similarity metric
    user_similarity = cosine_similarity(util_matrix_sparse.T)
    # Save the matrix as a dataframe to allow for easier indexing
    user_sim_df = pd.DataFrame(user_similarity, index = util_matrix.columns, columns = util_matrix.columns)
    user_similarity = cosine_similarity(np.array(df_init_users), np.array(df_init_users))
    user_sim_df = pd.DataFrame(user_similarity, index = df_init_users['movieId'].values.astype(int), columns = df_init_users['movieId'].values.astype(int))
    # Remove duplicate rows from matrix
    user_sim_df = user_sim_df.loc[~user_sim_df.index.duplicated(keep='first')]
    # Transpose matrix
    user_sim_df = user_sim_df.T
    # Find IDs of chosen load_movie_titles
    idx_1 = indices[indices == movie_list[0]].index[0]
    idx_2 = indices[indices == movie_list[1]].index[0]
    idx_3 = indices[indices == movie_list[2]].index[0]
    # Creating a Series with the similarity scores in descending order
    rank_1 = user_sim_df[idx_1]
    rank_2 = user_sim_df[idx_2]
    rank_3 = user_sim_df[idx_3]
    # Calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
    # Appending the names of movies
    listings = score_series_1.append(score_series_2).append(score_series_3).sort_values(ascending = False)
    # Choose top 50
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    # Get titles of recommended movies
    recommended_movies = []
    for i in top_indexes[:top_n]:
        recommended_movies.append(list(movies_df[movies_df['movieId']==i]['title']))
    # Return list of movies
    recommended_movies = [val for sublist in recommended_movies for val in sublist]
    return recommended_movies
