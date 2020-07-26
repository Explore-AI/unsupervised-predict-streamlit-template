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
    ---------------------------------------------------------------------
    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.
"""

# Data dependencies
import pandas as pd
import numpy as np
import pickle
import bz2
import _pickle as cPickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',',delimiter=',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

#Manupulate ratings_df and movies_df
ratings_df = pd.merge(movies_df['movieId'], ratings_df, on='movieId', how='outer')
ratings_df['rating'] = ratings_df['rating'].fillna(ratings_df['rating'].mean())
ratings_df['userId'] = ratings_df['userId'].fillna(ratings_df['userId'].mode()[0])
ratings_df['userId'] = ratings_df['userId'].astype(int)
ratings_df['rating'] = np.round(ratings_df['rating'] , 1)
ratings_df = ratings_df[['userId','movieId','rating']]

#Load and decompress model
def decompress_pickle(file):
    data = bz2.BZ2File(file,'rb')
    data = cPickle.load(data)
    return(data)
model = decompress_pickle('../pickled_files/full_compressed.pbz2')

# Building the Model
#model=pickle.load(open('../pickled_files/training_df_1.pkl', 'rb'))

def prediction_item(item_id):
    """Short summary.
    Parameters
    ----------
    item_id : type
        Description of parameter `item_id`.
    Returns
    -------
    type
        Description of returned object.
    """
    # data preprosessing
    reader = Reader(rating_scale=(0, 5))
    load_df = Dataset.load_from_df(ratings_df,reader)
    a_train = load_df.build_full_trainset()


    predictions = []
    for ui in a_train.all_users():
        predictions.append(model.predict(iid=movies_df.title.tolist().index(i),uid=ui, verbose = False))
    return predictions

def pred_movies(movie_list):
    """Short summary.
    Parameters
    ----------
    movie_list : type
        Description of parameter `movie_list`.
    Returns
    -------
    type
        Description of returned object.
    """
    # store the id of users
    id_store=[]
    # In each movie predict a user with the highest rating
    for i in movie_list:
        predictions = prediction_item(item_id = i)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # take the top 5 user id's from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.append(pred.uid)
    # return a list of  user id's
    return id_store

def collab_model(movie_list,top_n):
    """Short summary.
    Parameters
    ----------
    movie_list : type
        Description of parameter `movie_list`.
    top_n : type
        Description of parameter `top_n`.
    Returns
    -------
    type
        Description of returned object.
    """

    indices = pd.Series(movies_df['title'])
    movie_ids = pred_movies(movie_list)
    df_init_users = ratings_df[ratings_df['userId']==movie_ids[0]]
    for i in movie_ids :
        df_init_users=df_init_users.append(ratings_df[ratings_df['userId']==i])
    # Getting the cosine similarity matrix
    cosine_sim = cosine_similarity(np.array(df_init_users), np.array(df_init_users))
    print(movie_list)
    idx_1 = indices[indices == movie_list[0]].index[0]
    idx_2 = indices[indices == movie_list[1]].index[0]
    idx_3 = indices[indices == movie_list[2]].index[0]
    # creating a Series with the similarity scores in descending order
    rank_1 = cosine_sim[idx_1]
    rank_2 = cosine_sim[idx_2]
    rank_3 = cosine_sim[idx_3]
    # calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
     # appending the names of movies
    listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
    recommended_movies = []
    # choose top 50
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:top_n + 1]:
        recommended_movies.append(list(movies_df['title'])[i])
    return recommended_movies