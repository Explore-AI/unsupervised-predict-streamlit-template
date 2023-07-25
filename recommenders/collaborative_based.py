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
import bz2
import os
import copy
import surprise
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
ifile = bz2.BZ2File("resources/models/svd_plus_compress", "rb")
model=pickle.load(ifile)
ifile.close()

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

    # Store the id of users
    id_store=[]
    
    #Store movie_ids
    mov_ids = []
    
    #iterate over the movie list
    for movie in movie_list:
        
        #append the id from the movies_df to the list
        mov_ids.append(int(movies_df['movieId'][movies_df['title']==movie]))
    # For each movie selected by a user of the app,
    # predict a corresponding user within the dataset with the highest rating
    for i in mov_ids:
        predictions = prediction_item(item_id = i)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # Take the top 10 user id's from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.append(pred.uid)
    
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

    #store the movie ids
    mov_ids = []
    
    #iterate over the movie list
    for movie in movie_list:
        #append the movie id from the movies_df to the list
        mov_ids.append(int(movies_df['movieId'][movies_df['title']==movie]))
    
    #store predicted similar users
    user_ids = pred_movies(movie_list)
    
    #generate a df with the ratings of similar users
    df_init_users = ratings_df[ratings_df['userId'].isin(user_ids)]
    #merge the df to obtain the movie titles
    df_init_users = pd.merge(df_init_users, movies_df, on="movieId", how="inner")
    #drop the genres column
    df_init_users.drop('genres', inplace = True, axis = 1)
    
    #create dictionary to create a new user with the ratings
    user_row1 = {'userId':500000, 'movieId': mov_ids[0], 'title': movie_list[0], 'rating': 5.0}
    user_row2 = {'userId':500000, 'movieId': mov_ids[1], 'title': movie_list[1], 'rating': 5.0}
    user_row3 = {'userId':500000, 'movieId': mov_ids[2], 'title': movie_list[2], 'rating': 5.0}
    #append the new ratings as observations
    df_init_users = df_init_users.append([user_row1,
                                          user_row2, 
                                          user_row3],
                                        ignore_index =True)
    
    
    #pivot the similar users to have unique rows
    user_pivot = pd.pivot_table(df_init_users,
                                values = 'rating',
                                columns = 'title',
                                index = 'userId')
    
    #fill the nulls with 0
    user_pivot = user_pivot.fillna(0)
    #obtain the correlation matrix
    corr_movie_df = user_pivot.corr(method = 'pearson')
    
    #create a new dataframe
    movie_sim_df = pd.DataFrame()
    #iterate over the movie list
    for movie in movie_list:
        #calculate the similarity score
        high_score = corr_movie_df[movie] * 5
        #sort the value with the highest score at the top
        high_score = high_score.sort_values(ascending = False)
        #append the sorted scores to the dataframe
        movie_sim_df = movie_sim_df.append(high_score, 
                                          ignore_index = True)
    
    #store the movie titles recommended
    all_movies_recommended = []
    
    #calculate the cumulative score for each movie in the df
    for mov in movie_sim_df.sum().sort_values(ascending = False).index:
        if mov in movie_list:
            pass
        else:
            #append the movie title on the list
            all_movies_recommended.append(mov)
    #get the top n movies
    recommended_movies = all_movies_recommended[:top_n]
    #return the recommended movies
    return recommended_movies
