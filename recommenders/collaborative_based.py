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
movies_df.movieId = movies_df.movieId.astype(int)
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

#Manupulate ratings_df and movies_df
#ratings_all = pd.merge(movies_df, ratings_df, on='movieId', how='outer')

#Load and decompress model
def decompress_pickle(file):
    data = bz2.BZ2File(file,'rb')
    data = cPickle.load(data)
    return(data)
model = decompress_pickle('../pickled_files/full_compressed.pbz2')

# Building the Model

#model=pickle.load(open('../pickled_files/training_df_1.pkl', 'rb'))
#model = pickle.load(open('resources/models/SVD.pkl','rb'))

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
    reader = Reader(rating_scale=(0.5, 5))
    load_df = Dataset.load_from_df(ratings_df,reader)
    a_train = load_df.build_full_trainset()


    predictions = []
    for ui in a_train.all_users():
        predictions.append(model.predict(iid=item_id,uid=ui, verbose = False))
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
    movieids = pd.DataFrame()
    # In each movie predict a user with the highest rating
    for i in movie_list:
        movieid = movies_df[movies_df.title==str(i)].movieId
        movieids = pd.concat([movieids,movieid],axis=0)
    for movie in movieids.loc[:,0].tolist():
        predictions = prediction_item(item_id = movie)
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

#    indices = pd.Series(movies_df['title'])
    all_users = pd.DataFrame()
    user_ids = pred_movies(movie_list)
    for user in set(user_ids):
        all_users = pd.concat([all_users,ratings_df[ratings_df['userId']==user]])
    a = {}
    temp_df = pd.DataFrame()
    for movieid in set(all_users.movieId.tolist()):
        if movieid in movies_df.movieId:
            count = len(all_users[all_users['movieId']==movieid])
            average = all_users[all_users['movieId']==movieid].rating.mean()
#            temp_1 = pd.DataFrame({'movieId':movies_df[movies_df['movieId']==movieid].title.tolist()
#                                   ,'popularity':[count*average]})
            temp_1 = pd.DataFrame.from_records([{ 'movieId':movies_df[movies_df['movieId']==movieid].title.tolist(),
                                                 'popularity':count*average}])
            temp_df = pd.concat([temp_df,temp_1])
        temp_df = temp_df.sort_values(by='popularity',ascending=False)
#            a[movieid] = count*average
#    sorted_a = sorted(a.items(), key=lambda x: x[1],reverse=True)[:10]
#    movieLists = []
#    for i in sorted_a:
#        movieLists.append(indices[i[0]])
    return(temp_df)
#    df_init_users = ratings_df[ratings_df['userId']==movie_ids[0]]
#    for i in movie_ids :
#        df_init_users=df_init_users.append(ratings_df[ratings_df['userId']==i])
#    return(all_users)
    # Getting the cosine similarity matrix
#    cosine_sim = cosine_similarity(np.array(df_init_users), np.array(df_init_users))
#    idx_1 = indices[indices == movie_list[0]].index[0]
#    idx_2 = indices[indices == movie_list[1]].index[0]
#    idx_3 = indices[indices == movie_list[2]].index[0]
#    # creating a Series with the similarity scores in descending order
#    rank_1 = cosine_sim[idx_1]
#    rank_2 = cosine_sim[idx_2]
#    rank_3 = cosine_sim[idx_3]
#    # calculating the scores
#    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
#    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
#    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
#     # appending the names of movies
#    listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
#    recommended_movies = []
#    # choose top 50
#    top_50_indexes = list(listings.iloc[1:50].index)
#    # Removing chosen movies
#    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
#    for i in top_indexes[:top_n + 1]:
#        recommended_movies.append(list(movies_df['title'])[i])
#    return df_init_users