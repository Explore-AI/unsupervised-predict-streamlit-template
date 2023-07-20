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
from scipy.sparse import csr_matrix

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

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

    print('We just entered the collab funtion')
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

    # indices = pd.Series(movies_df['title'])
    # movie_ids = pred_movies(movie_list)
    # df_init_users = ratings_df[ratings_df['userId']==movie_ids[0]]
    # for i in movie_ids :
    #     df_init_users=df_init_users.append(ratings_df[ratings_df['userId']==i])
    # # Getting the cosine similarity matrix
    # cosine_sim = cosine_similarity(np.array(df_init_users), np.array(df_init_users))
    # idx_1 = indices[indices == movie_list[0]].index[0]
    # idx_2 = indices[indices == movie_list[1]].index[0]
    # idx_3 = indices[indices == movie_list[2]].index[0]
    # # Creating a Series with the similarity scores in descending order
    # rank_1 = cosine_sim[idx_1]
    # rank_2 = cosine_sim[idx_2]
    # rank_3 = cosine_sim[idx_3]
    # # Calculating the scores
    # score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    # score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    # score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
    #  # Appending the names of movies
    # listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
    # recommended_movies = []
    # # Choose top 50
    # top_50_indexes = list(listings.iloc[1:50].index)
    # # Removing chosen movies
    # top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    # for i in top_indexes[:top_n]:
    #     recommended_movies.append(list(movies_df['title'])[i])
    # return recommended_movies

    # Assuming movies_df and ratings_df are the DataFrames containing movie and rating information
    # Get movieIds from movie_list
    # movie_ids = pred_movies(movie_list)

    # # Create a utility matrix with users as rows and movies as columns
    # utility_matrix = ratings_df.pivot(index='userId', columns='movieId', values='rating')

    # # Filter rows corresponding to movie_ids
    # selected_users = utility_matrix.loc[movie_ids]

    # # Convert utility matrix to a sparse matrix
    # selected_users_sparse = csr_matrix(selected_users.fillna(0))

    # # Compute cosine similarity matrix using sparse matrices
    # cosine_sim_sparse = cosine_similarity(selected_users_sparse)

    # # Get indices of movies in movie_list
    # movie_indices = movies_df[movies_df['movieId'].isin(movie_ids)].index

    # # Calculate the scores based on cosine similarity with movie_list movies
    # scores = cosine_sim_sparse[:, movie_indices].sum(axis=1)

    # # Sort movies based on scores in descending order
    # top_indexes = np.argsort(scores)[::-1]

    # # Get recommended movies excluding the ones in movie_list
    # recommended_movies = list(movies_df['title'][top_indexes])
    # recommended_movies = [movie for movie in recommended_movies if movie not in movie_list]

    # return recommended_movies[:top_n]

        # Assuming movies_df and ratings_df are the DataFrames containing movie and rating information

    # Get movieIds from movie_list
    movie_ids = pred_movies(movie_list)
    print('movie_ids PASSED')

    # Create a utility matrix with users as rows and movies as columns
    utility_matrix = ratings_df.pivot(index='userId', columns='movieId', values='rating')
    print('Util matrix done')

    # Filter rows corresponding to movie_ids
    selected_users = utility_matrix.loc[movie_ids]
    print('Util matrix filtering done')

    # Convert utility matrix to a sparse matrix
    selected_users_sparse = csr_matrix(selected_users.fillna(0))
    print('Converting util to sparse matrix done')

    print("Shape of selected_users_sparse:", selected_users_sparse.shape)
    

    # Compute cosine similarity matrix using sparse matrices
    cosine_sim_sparse = cosine_similarity(selected_users_sparse)

    print("Shape of cosine_sim_sparse:", cosine_sim_sparse.shape)

    # Get indices of movies in movie_list
    movie_indices = movies_df[movies_df['movieId'].isin(movie_ids)].index

    print("Movie indices:", movie_indices)

    # Calculate the scores based on cosine similarity with movie_list movies
    scores = cosine_sim_sparse[:, movie_indices].sum(axis=1)

    # Sort movies based on scores in descending order
    top_indexes = np.argsort(scores)[::-1]

    # Get recommended movies excluding the ones in movie_list
    recommended_movies = list(movies_df['title'][top_indexes])
    recommended_movies = [movie for movie in recommended_movies if movie not in movie_list]

    return recommended_movies[:top_n]
