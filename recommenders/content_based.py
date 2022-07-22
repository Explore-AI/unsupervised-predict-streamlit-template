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
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from mlxtend.preprocessing import TransactionEncoder

# Suppress cell warnings for a cleaner notebook
import warnings
warnings.filterwarnings('ignore')

# Importing data
movies_df = pd.read_csv('resources/data/movies.csv',sep = ',')

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
    movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    # Subset of the data
    movies_subset = movies[:subset_size]
    return movies_subset
@st.cache(show_spinner=False, suppress_st_warning=True)
# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    genre = data_preprocessing(movies_df)
    indices = pd.Series(movies_df['title'])    # List of all index for movies
    # Names of the three selected movies
    movie_1 = genre[movie_list[0]]
    movie_2 = genre[movie_list[1]]
    movie_3 = genre[movie_list[2]]
    # Calculate similar movies for selected movie one
    similar_movie_1 = genre.corrwith(movie_1)   
    similar_movie_1 = similar_movie_1.sort_values(ascending = False) # Sort by correlation score
    similar_movie_1 = similar_movie_1.iloc[1:]  # Drop movie selected by user
    # Remove correlation value and only keep movie title
    movie_one = pd.DataFrame(similar_movie_1)
    movie_one.reset_index(inplace = True)
    movie_one = movie_one.drop(movie_one.columns[1], axis =1)
    movie_one_list = movie_one['movie_title'].tolist() # Convert to a list
    movie_one_list = movie_one_list[0:3] # Keep top four
    
    # Same process will be followed for movie two and three
    similar_movie_2 = genre.corrwith(movie_2)   
    similar_movie_2 = similar_movie_2.sort_values(ascending = False) 
    similar_movie_2 = similar_movie_2.iloc[1:]  
    movie_two = pd.DataFrame(similar_movie_2)
    movie_two.reset_index(inplace = True)
    movie_two = movie_two.drop(movie_two.columns[1], axis =1)
    movie_two_list = movie_two['movie_title'].tolist() # Convert to a list
    movie_two_list = movie_two_list[0:4] # Keep top five     
        
    similar_movie_3 = genre.corrwith(movie_3)   
    similar_movie_3 = similar_movie_3.sort_values(ascending = False) 
    similar_movie_3 = similar_movie_3.iloc[1:]  
    movie_three = pd.DataFrame(similar_movie_3)
    movie_three.reset_index(inplace = True)
    movie_three_list = movie_three['movie_title'].tolist() # Convert to a list
    movie_three_list = movie_three_list[0:3] # Keep top four 
    
    recommended_movies = movie_one_list + movie_two_list + movie_three_list
    
    return recommended_movies
