"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Importing data
# load Movie dataset
df_data = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/imdb_data.csv')
# load movies csv
df_movie = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/movies.csv')

#movies = pd.read_csv('resources/data/movies.csv', sep = ',')
#movies.dropna(inplace=True)

# Merge movie, data and train dataframes
df_title = df_movie.merge(df_data, on='movieId')

def data_preprocessing(subset_size):
    """Prepare data for use within Content filtering algorithm.
    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.
    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.
    """
    # Split genre data into individual words.
    # Split genre , title and keywords into individual words
    df_title['keyWords'] = df_title['plot_keywords'].str.replace('|', ' ')
    df_title['genre'] = df_title['genres'].str.replace('|', ' ')
    df_title['cast'] = df_title['title_cast'].str.replace('|', ' ')
    # Split movie title by title and year
    split_values_m = df_title['title'].str.split("(", n=1, expand = True)
    #Set movie name to title only - remove year
    df_title.title = split_values_m[0]
    # Create new column for year
    df_title['year'] = split_values_m[1]
    df_title['year'] = df_title['year'].str.strip(')')
    df_title['title'] = df_title['title'].str.rstrip()
    #movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    # Subset of the data
    movies_subset = df_title[:subset_size]
                           
    return movies_subset



# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
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
    # Initializing the empty list of recommended movies
    
    data = data_preprocessing(200000)
    
    # Select Features relevant for recommendations
    select_features = ['cast', 'director', 'keyWords', 'genre', 'title']
    # Replace null values with null strings in selected features
    for feature in select_features:
        df_title[feature] = df_title[feature].fillna('')
    # Combine all selected features into one list and assign to df_movie_base
    df_title_recom = df_title['director']+' '+df_title['keyWords']+' '+df_title['genre']+' '+df_title['cast']+' '+df_title['title']
    # Convert text to feature vectors
    vect_m = TfidfVectorizer()
    movie_vectors = vect_m.fit_transform(df_title_recom)
    # Similarity calculation using cosine similarity
    similarity = cosine_similarity(movie_vectors, movie_vectors)
    indices = pd.Series(df_title['title'])
    # Index value of user selected movies
    mo_1_idx = indices[indices == movie_list[0]].index[0]
    mo_2_idx = indices[indices == movie_list[1]].index[0]
    mo_3_idx = indices[indices == movie_list[2]].index[0]
    # Similarity scores with other movies for the 3 selected movies
    mo_1_score = list(enumerate(similarity[mo_1_idx]))
    mo_2_score = list(enumerate(similarity[mo_2_idx]))
    mo_3_score = list(enumerate(similarity[mo_3_idx]))
    # Sort by score - second value 
    similar_sorted_1 = sorted(mo_1_score, key = lambda x:x[1], reverse = True)
    similar_sorted_2 = sorted(mo_2_score, key = lambda x:x[1], reverse = True)
    similar_sorted_3 = sorted(mo_3_score, key = lambda x:x[1], reverse = True)
    movie_one = pd.Series(similar_sorted_1)
    movie_two = pd.Series(similar_sorted_2)
    movie_three = pd.Series(similar_sorted_3)
    # Store scores for all 3 movies in one list 
    scores_movies = movie_one.append(movie_two).append(movie_three)
    scores_movies = sorted(scores_movies, key = lambda x:x[1], reverse = True)
    # Select top 50 movies (highest scores)
    top_50 = list(scores_movies[1:50])
    # Remove score value and only keep movie ID
    top_50_list = [i[0] for i in top_50]
    recommended_movies = []
    for i in top_50_list[:12]:
        if (i != mo_1_idx).any() & (i != mo_2_idx).any() & (i != mo_3_idx).any():
            recommended_movies.append(list(df_title['title'])[i])
    
    return recommended_movies