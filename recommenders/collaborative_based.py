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
from sklearn.metrics.pairwise import cosine_similarity

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
        # take the top 10 user id's from each movie with highest rankings
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
    all_users = pd.DataFrame()
    user_ids = pred_movies(movie_list)
    for user in set(user_ids):
        all_users = pd.concat([all_users,ratings_df[ratings_df['userId']==user]])
    piv_df = pd.pivot_table(all_users,index='userId',columns='movieId',values='rating')
    piv_df_2 = piv_df.fillna(0)
    cosine_sim = pd.DataFrame(cosine_similarity(piv_df_2,piv_df_2),index=piv_df_2.index,columns=piv_df_2.index)
    for i in piv_df.index:
    similarities = np.array(cosine_sim[i])
    for movie in piv_df.columns:
        if np.isnan(piv_df.loc[i,movie]):
            numerator = sum(piv_df_2.loc[:,movie].values*similarities)
            denominator = sum(similarities[np.array([i for i,v in enumerate(piv_df_2.loc[:,movie]) if v > 0])])
            if numerator > 0:
                piv_df.loc[i][movie] = numerator/denominator
            else:
                piv_df.loc[i][movie] = 0
    averages = pd.DataFrame()
    for movie in piv_df.columns:
        if movie in movies_df.movieId:
            average = piv_df.loc[:,movie].mean()
            temp_df = pd.DataFrame({'movieId':[movie],'average':[average]})
            averages = pd.concat([averages,temp_df])
    averages = averages.sort_values(by='average',ascending=False)
    #    a = {}
#    temp_df = pd.DataFrame()
#    for movieid in set(all_users.movieId.tolist()):
#        if movieid in movies_df.movieId:
#            count = len(all_users[all_users['movieId']==movieid])
#            average = all_users[all_users['movieId']==movieid].rating.mean()
#            temp_1 = pd.DataFrame.from_records([{ 'title':movies_df[movies_df['movieId']==movieid].title.tolist(),
#                                                 'popularity':count*average}])
#            temp_df = pd.concat([temp_df,temp_1])
#        temp_df = temp_df[temp_df['popularity'] < 30]
#        temp_df = temp_df.sort_values(by='popularity',ascending=False)
#        top10 = [i[0] for i in temp_df.head(10).title]

    return(averages)