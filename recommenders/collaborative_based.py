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
import streamlit as st
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

# Suppress cell warnings for a cleaner notebook
import warnings
warnings.filterwarnings('ignore')

# Importing data
movies_df = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/movies.csv', sep = ',')
ratings_df = pd.read_csv('resources/data/ratings.csv')
ratings_df.drop(['timestamp'], axis=1,inplace=True)

    #Below function creates a pivot table

def movie_data(movie):
    # New pivot where each column would represent each unique userId and each row represents each unique movieId
    movie_pivot = movie.pivot(index = 'movieId', columns = 'userId', values = 'rating')
    # Convert NAN to zero value
    movie_pivot.fillna(0, inplace = True)

    return movie_pivot

    # Below function finds nearest neighbors and returns recommended movie list using cosine similarity between movies
@st.cache(show_spinner=False, suppress_st_warning=True)
def collab_model(movie_list,top_n=10):
    # Use function to merge dataframse and select submit based on highest coutn of movie ratings 
    movie = movies_df.merge(ratings_df, how = 'left', on='movieId')
    # Below limits the data to 6000 rows based on highest count for movie rating
    #movies_count= movie_full.groupby('title')['rating'].count().sort_values(ascending=False).reset_index().rename(columns={'rating':'Rating Count'}) 
    # Merge count with title/ movieid/ rating 
    #movies_with_count = movie_full.merge(movies_count, on= 'title')
    #Use dataset with a minimum count of ratings per movie of 6000
    #view_threshold = 6000
    #movie = movies_with_count[movies_with_count['Rating Count']>= view_threshold] 
      
    # Convert df to a pivot table and replace NAN value with zero
    movie_pivot = movie_data(movie)  
    #number_recommend = 10
    # Reduce sparsity to assist with computation time on large dataset
    csr_item = csr_matrix(movie_pivot.values)  
    movie_pivot.reset_index(inplace=True)
    # Initiate KNN model using NearestNeighbors and Cosine similarity
    knn_item = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors = 20, n_jobs = -1)
    knn_item.fit(csr_item)
    # Remove year from movie title
    movie_list2 = [x[:-7] for x in movie_list]
    # Empty list to store recommended movieID's
    full_list = []
    # Check if selected movie is in the moevie dataframe
    movie_list_1 = movies_df[movies_df['title'].str.contains(movie_list2[0])]  #check if movie selected is in movie dataframe
    movie_list_2 = movies_df[movies_df['title'].str.contains(movie_list2[1])]
    movie_list_3 = movies_df[movies_df['title'].str.contains(movie_list2[2])]
    
    if len(movie_list_1):
        movie_index_1 = movie_list_1.iloc[0]['movieId']  # finds movie index of selected movie
        movie_index_1 = movie_pivot[movie_pivot['movieId'] == movie_index_1].index[0] # finds movie index in pivot table
        distances , indices = knn_item.kneighbors(csr_item[movie_index_1],n_neighbors=top_n+1)  #find 10 most similar movies with KNN model (index of movie and distance)
        # index of recommended movies with distance in sorted list - most similar first
        recommend_movie_indices_1 = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1] # excluding the selected movie
        
        # Calculate the same for movie 2 and 3 as per movie 1 from movie list: 
        
    if len(movie_list_2):
        movie_index_2 = movie_list_2.iloc[0]['movieId']  
        movie_index_2 = movie_pivot[movie_pivot['movieId'] == movie_index_2].index[0]
        distances , indices = knn_item.kneighbors(csr_item[movie_index_2],n_neighbors=top_n+1)  
        recommend_movie_indices_2 = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1] 

    if len(movie_list_3):
        movie_index_3 = movie_list_3.iloc[0]['movieId']  
        movie_index_3 = movie_pivot[movie_pivot['movieId'] == movie_index_3].index[0]
        distances , indices = knn_item.kneighbors(csr_item[movie_index_3],n_neighbors=top_n+1)  
        recommend_movie_indices_3 = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1] 
                
    # Combine above three lists and sort from closest to lowest distance
    full_list = recommend_movie_indices_1 + recommend_movie_indices_2 + recommend_movie_indices_3
    full_list = sorted(full_list, key = lambda x:x[1], reverse = True)
    
    recommend_list = []        # list for recommended movies
    for item in full_list:     # loop through recommended movies to find title of movies
        movie_index = movie_pivot.iloc[item[0]]['movieId']
        idx = movies_df[movies_df['movieId'] == movie_index].index
        recommend_list.append({'Title':movies_df['title'].iloc[idx].values[0],'Distance':item[1]}) # extract title of movie
    df_recommend = pd.DataFrame(recommend_list,index=range(1,31)) # convert to dataframe
    recommended_movies = df_recommend['Title'][:10].tolist()
    
    return recommended_movies