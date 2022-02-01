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
    usecols  =['userId', 'movieId', 'rating','timestamp'],dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

ratings_df = ratings_df[:40000]



# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
#model_knn = pickle.load(open('resources/models/model_knn.pkl', 'rb'))
movie_rating = pd.merge(movies_df , ratings_df, on = 'movieId')
cols = ['movieId', 'userId', 'title', 'rating']
movie_rating = movie_rating[cols]
movie_ratings = movie_rating.copy()

def data_preprocessing(data):
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

    
    util_matrix = movie_ratings.pivot_table(index = ['title'], 
                                       columns = ['userId'],
                                       values = 'rating') 

    # Normalize each row (a given user's ratings) of the utility matrix
    util_matrix_norm = util_matrix.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
    # Fill Nan values with 0's, transpose matrix, and drop users with no ratings
    util_matrix_norm.fillna(0, inplace=True)
    util_matrix_norm = util_matrix_norm.T
    util_matrix_norm = util_matrix_norm.loc[:, (util_matrix_norm != 0).any(axis=0)]
    # Save the utility matrix in scipy's sparse matrix format
    util_matrix_sparse = sp.sparse.csr_matrix(util_matrix_norm.values)

    # Compute the similarity matrix using the cosine similarity metric
    user_similarity = cosine_similarity(util_matrix_sparse.T)
    # Save the matrix as a dataframe to allow for easier indexing  
    user_sim_df = pd.DataFrame(user_similarity, 
                           index = util_matrix_norm.columns, 
                           columns = util_matrix_norm.columns)
    return user_sim_df, util_matrix_norm

def collab_generate_top_N_recommendations(user, k=20):

    # Cold-start problem - no ratings given by the reference user. 
    # With no further user data, we solve this by simply recommending
    # the top-N most popular books in the item catalog. 
    user_sim_df = data_preprocessing(movie_ratings)
    util_matrix_norm = data_preprocessing(movie_ratings)
    if user not in user_sim_df.columns:
        return movie_ratings.groupby('userId').mean().sort_values(by='rating',
                                        ascending=False).index.to_list()
    
    # Gather the k users which are most similar to the reference user 
    sim_users = user_sim_df.sort_values(by=user, ascending=False).index[1:k+1]
    favorite_user_items = [] # <-- List of highest rated items gathered from the k users  
    most_common_favorites = {} # <-- Dictionary of highest rated items in common for the k users
    
    for i in sim_users:
        # Maximum rating given by the current user to an item 
        max_score = util_matrix_norm.loc[:, i].max()
        # Save the names of items maximally rated by the current user   
        favorite_user_items.append(util_matrix_norm[util_matrix_norm.loc[:, i]==max_score].index.tolist())
        
    # Loop over each user's favorite items and tally which ones are 
    # most popular overall.
    for item_collection in range(len(favorite_user_items)):
        for item in favorite_user_items[item_collection]: 
            if item in most_common_favorites:
                most_common_favorites[item] += 1
            else:
                most_common_favorites[item] = 1
    # Sort the overall most popular items and return the top-N instances
    sorted_list = sorted(most_common_favorites.items(), key=operator.itemgetter(1), reverse=True)
    top_N = [x[0] for x in sorted_list]
    return top_N

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
    movie_features_df = data_preprocessing(movies_df,ratings_df)
    movie_features_df_matrix = csr_matrix(movie_features_df.values)
    df = movie_features_df

    movie_1 = movie_list[0]
    movie_2 = movie_list[1]
    movie_3 = movie_list[2]

    me_1 = movie_1
    x_1 = collab_generate_top_N_recommendations(me_1)

    movies_1 = ['kwanda']

    test = 1

    for count in x_1:

        kwanda = movie_ratings[movie_ratings['userId'] == count].sort_values(by = 'rating', ascending = False)
    
        if kwanda.iloc[0]['title'] not in movies_1 and kwanda.iloc[0]['title'] != me_1:
        
            if test != 11:
        
                movies_1.append(kwanda.iloc[0]['title'])
                test += 1
    recommended_movies_1 = movies_1[1:]
    
    me_2 = movie_2
    x_2 = collab_generate_top_N_recommendations(me_2)

    movies_2 = ['kwanda']

    test = 1

    for count in x_2:

        kwanda = movie_ratings[movie_ratings['userId'] == count].sort_values(by = 'rating', ascending = False)
    
        if kwanda.iloc[0]['title'] not in movies_2 and kwanda.iloc[0]['title'] != me_2:
        
            if test != 11:
        
                movies_2.append(kwanda.iloc[0]['title'])
                test += 1

    recommended_movies_2 = movies_2[1:]

    me_3 = movie_3
    x_3 = collab_generate_top_N_recommendations(me_3)

    movies_3 = ['kwanda']

    test = 1

    for count in x_3:

        kwanda = movie_ratings[movie_ratings['userId'] == count].sort_values(by = 'rating', ascending = False)
    
        if kwanda.iloc[0]['title'] not in movies_3 and kwanda.iloc[0]['title'] != me_3:
        
            if test != 11:
        
                movies_3.append(kwanda.iloc[0]['title'])
                test += 1

    recommended_movies_3 = movies_3[1:]

    recommended_movie = [recommended_movies_1,recommended_movies_2,recommended_movies_3]

    recommended_movies = random.sample(recommended_movie, 10)

    return recommended_movies
