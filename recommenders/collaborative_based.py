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
import pandas
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import pathlib
import fastai
from fastai.collab import *
from fastai.tabular.all import *


# for windows deployment
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath


#For linux deployment
plt = platform.system()
if plt == 'Linux': 
    pathlib.WindowsPath = pathlib.PosixPath
else:
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath

# Importing data
# movies_df = pd.read_csv('resources/data/movies.csv',sep = ',')
# ratings_df = pd.read_csv('resources/data/ratings.csv')
# ratings_df.drop(['timestamp'], axis=1,inplace=True)

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
# model=pickle.load(open('resources/models/SVD.pkl', 'rb'))
learn = load_learner("resources/models/learn.pkl")
dls = torch.load("resources/data/dls.pkl")

movie_factors = learn.model.i_weight.weight
movies_title = dls.classes['title']
# movie_bias = learn.model.i_bias.weight.squeeze()

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

    # indices = pd.Series(movies_df['title'])

    recommendations = []
    for movie in movie_list:
        idx = movies_title.o2i[movie]
        distances = nn.CosineSimilarity(dim=1)(movie_factors, movie_factors[idx][None])
        idx = distances.argsort(descending=True)[:4]
        recommendations.extend(list(movies_title[idx]))
        
    return recommendations[:top_n]
