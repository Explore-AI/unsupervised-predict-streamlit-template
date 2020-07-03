# Importing packages and Data
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

os.path.exists('../resources/data/movies.csv')

# Importing data

movies = pd.read_csv('resources/data/movies.csv', sep = ',',delimiter=',') # Remove this to be modular
ratings = pd.read_csv('resources/data/ratings.csv') # Remove this to be modular
movies.dropna(inplace=True)

def datapreprocessing(subset_size):
    # spliting the genres
    movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    # Subset of the data
    movies_subset = movies[:subset_size]
    return movies_subset

def content_model(list_title):
    # initializing the empty list of recommended movies
    recommended_movies = []
    data = datapreprocessing(10000)
    # instantiating and generating the count matrix
    count_vec = CountVectorizer()
    count_matrix = count_vec.fit_transform(data['keyWords'])
    indices = pd.Series(data['title'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    # gettin the index of the movie that matches the title
    idx_1 = indices[indices == list_title[0]].index[0]
    idx_2 = indices[indices == list_title[1]].index[0]
    idx_3 = indices[indices == list_title[2]].index[0]
    # creating a Series with the similarity scores in descending order
    rank_1 = cosine_sim[idx_1]
    rank_2 = cosine_sim[idx_2]
    rank_3 = cosine_sim[idx_3]
    # calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
    # getting the indexes of the 10 most similar movies
    listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)

    #listings.drop_duplicates(inplace=True)

    # a list to store names
    recommended_movies = []
    #movie_list
    # appending the names of movies
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:21]:
        recommended_movies.append(list(movies['title'])[i])
    return recommended_movies
