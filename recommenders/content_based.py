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
# Streamlit dependencies
import streamlit as st

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords  # Stopwords module provides a list of common words to be removed from the text.

# Utility Libraries
from currency_converter import CurrencyConverter

import string  # Provides constants and classes for string manipulation.

# Global Constants for reproducibility and consistency
RAND_STATE = 42
GENOME_RELEVANCE_THRESHOLD = 0.65 # Ignore genome tags below this threshold
USER_REVIEW_THRESHOLD = 30 # Only consider users with review counts larger than this number
MOVIE_REVIEW_THRESHOLD = 5000 # Only consider movies with more reviews than this number
CONTENT_VEC_MIN_WORD_TO_REMOVE = 10 # Remove words that occurs less that this value in dataset 

# Importing data
# movies = pd.read_csv('resources/data/movies.csv', sep = ',')
# ratings = pd.read_csv('resources/data/ratings.csv')
# movies.dropna(inplace=True)

genome_scores_df = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/genome_scores.csv')
genome_tags_df = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/genome_tags.csv')
imdb_data_df = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/imdb_data.csv')
links_df = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/links.csv')
movies_df = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/movies.csv')
tags_df = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/tags.csv')

# genome_scores_df = pd.read_csv('genome_scores.csv')
# genome_tags_df = pd.read_csv('genome_tags.csv')
# imdb_data_df = pd.read_csv('imdb_data.csv')
# links_df = pd.read_csv('links.csv')
# movies_df = pd.read_csv('movies.csv')
# tags_df = pd.read_csv('tags.csv')

# extra_imdb_name_basics_df = pd.read_table("./resources/imdb_name_basics.tsv")
# extra_imdb_title_crew_df = pd.read_table("./resources/imdb_title_crew.tsv")

print("Data Import Complete")

# # Removing unnecessary columns from imported data
# extra_imdb_name_basics_df.drop(["birthYear", "deathYear", "primaryProfession", 'knownForTitles'], axis=1, inplace=True)
# extra_imdb_title_crew_df.drop(['writers'], axis=1, inplace=True)
# extra_imdb_title_crew_df.rename(columns={"directors": "nconst"}, inplace=True)

# # Joining imported datasets
# df_extra_imdb_combo = pd.merge(extra_imdb_title_crew_df, extra_imdb_name_basics_df, on="nconst", how="left")
# df_extra_imdb_combo.drop("nconst", axis=1, inplace=True)

# # Converting IMDB ID to correct format
# df_extra_imdb_combo.rename(columns={"tconst":"imdbId"}, inplace=True)
# df_extra_imdb_combo['imdbId'] = df_extra_imdb_combo['imdbId'].str.replace('tt','').astype(int)

# # Adding the corresponding IMDB links to the dataframe we need to update:
# imdb_data_df = pd.merge(imdb_data_df, links_df[['movieId', 'imdbId']], on='movieId', how='left')

# # Merging the correct director into a new column (primaryName) in the dataframe 
# imdb_data_df = pd.merge(imdb_data_df, df_extra_imdb_combo, on='imdbId', how='left')

# # Function to update the director with correct value
# def replace_director(df):
#     for index, row in df.iterrows():
#         if pd.notnull(row['primaryName']):
#             df.at[index, 'director'] = row['primaryName']
#     return df

# # Applying the function
# imdb_data_df = replace_director(imdb_data_df)

# # Dropping redundant columns after merge
# imdb_data_df.drop('imdbId', axis=1, inplace=True)
# imdb_data_df.drop('primaryName', axis=1, inplace=True)

# print("Data Link Complete")

# Create a df for storing all available movie data
all_movie_data = imdb_data_df

# Add movie title and genres to the new dataframe
all_movie_data = pd.merge(all_movie_data, movies_df, on='movieId', how='left')

# Remove movies with unknown titles
all_movie_data = all_movie_data[all_movie_data['title'].notna()]

# Filter out genome scores below threshold to ensure only relevant tags gets mapped to movie metadata
filtered_genome_tag_data = genome_scores_df[genome_scores_df['relevance']>= GENOME_RELEVANCE_THRESHOLD]

# Merging genome scores with genome tags
filtered_genome_tag_data = pd.merge(filtered_genome_tag_data, genome_tags_df, on='tagId')

# Dropping redundant columns
filtered_genome_tag_data = filtered_genome_tag_data.drop(["tagId", "relevance"], axis=1)

# To keep tags of multiple words as a single entity, we replace spaces with underscores
filtered_genome_tag_data['tag'] = filtered_genome_tag_data['tag'].str.replace(" ", "_")

# Adding a space after each tag so that tags get merged as individual entities
filtered_genome_tag_data['tag'] = filtered_genome_tag_data['tag'] + " "

# Combining all tags for each movie
filtered_genome_tag_data = filtered_genome_tag_data.groupby(by = 'movieId').sum()

# Renaming tag column so that it does not get confused with user generated tags later on
filtered_genome_tag_data.rename(columns={"tag": "genome_tags"}, inplace=True)

# Adding our genome tags to movie metadata
all_movie_data = pd.merge(all_movie_data, filtered_genome_tag_data, on='movieId', how='left')

# Select features to join into movie metadata
modified_user_tags = tags_df[['movieId', 'tag']]

# Replace spaces with underscores so that entities remain unique
modified_user_tags['tag'] = modified_user_tags['tag'].str.replace(" ", "_")

# Adding a space after each tag so that tags get merged as individual entities
modified_user_tags['tag'] = modified_user_tags['tag'] + " "

# Combining all tags for each movie
modified_user_tags = modified_user_tags.groupby(by='movieId').sum()

# Renaming tag column to avoid confusion with genome tags
modified_user_tags.rename(columns={"tag": "user_tags"}, inplace=True)

# Converting tags to lowercase to avoid unwanted distinction
modified_user_tags['user_tags'] = modified_user_tags['user_tags'].str.lower()

print("Movie DF Complete")

# Removing any punctuation except underscores
removelist = []
for punc in string.punctuation:
    if punc != '_':
        removelist.append(punc)

for char in removelist:
    modified_user_tags['user_tags'] = modified_user_tags['user_tags'].str.replace(char, '')

# Adding user tags to movie metadata
all_movie_data = pd.merge(all_movie_data, modified_user_tags, on='movieId', how='left')

# Feature to create `release_year` and `release_decade` feature from movie title
def get_decade(df):


    # Extract date from title
    df['release_year'] = df['title'].str[-6:]

    # Remove brackets from date
    for char in ['(', ')']:
        df['release_year'] = df['release_year'].str.replace(char, '')
    
    # Extract decade of release from release year
    df['release_decade'] = df['release_year'].str[:-1] + "0's"

    # Converting release year to integer
    #df['release_year'] = df['release_year'].astype(int)

    # Run through df to see if year and decade got extracted correctly:
    for index, row in df.iterrows():
        year = row['release_year']
        if year.isnumeric():
            # Convert year to intiger
            df.at[index, 'release_year'] = int(year)
        else:
            # Year extraction failed. Remove year and decade data
            df.at[index, 'release_year'] = np.nan
            df.at[index, 'release_decade'] = np.nan
    return df

# Applying the function
all_movie_data = get_decade(all_movie_data)

# Remove unlisted genre descriptions
all_movie_data['genres'] = all_movie_data['genres'].str.replace( "(no genres listed)" ,"")

# Process text data
def clean_text_features(df):
    # Features to process
    features = ['title_cast', 'director', 'plot_keywords', 'genres']

    # Apply changes to all features
    for feature in features:
        # Replace spaces with underscores to ensure multiple-worded concepts gets treated as single entity
        df[feature] = df[feature].str.replace(' ', '_')

        # Replace pipe symbol (|) with space to separate different entities
        df[feature] = df[feature].str.replace('|', ' ')

        # Convert string to lowercase to avoid unwanted distinctions
        df[feature] = df[feature].str.lower()

    return df

# Applying the function
all_movie_data = clean_text_features(all_movie_data)

# Create currency converter
c = CurrencyConverter()
available_currencies = list(c.currencies)

# Function to clean movie budget
def clean_and_convert_budget(budgetstring):

    # Test if value is missing
    if budgetstring != budgetstring:
        return np.nan
    
    # Delete commas from input string
    budgetstring = budgetstring.replace(",", "")

    # If in USD, convert to correct int format
    if budgetstring[0] == '$':
        new_budget = budgetstring.replace('$', '')
        return int(new_budget)
    
    # If able to convert to USD, convert to USD
    elif budgetstring[:3] in available_currencies:
        currency = budgetstring[:3]
        value = budgetstring[3:]
        new_value = c.convert(int(value), currency, "USD")
        return int(new_value)

    # If unable to convert to USD, delete entry since we can't use it
    else:
        return np.nan


# Applying the function
all_movie_data['budget'] = all_movie_data["budget"].apply(clean_and_convert_budget)

print("Data Clean Complete")

# def data_preprocessing(subset_size):
#     """Prepare data for use within Content filtering algorithm.

#     Parameters
#     ----------
#     subset_size : int
#         Number of movies to use within the algorithm.

#     Returns
#     -------
#     Pandas Dataframe
#         Subset of movies selected for content-based filtering.

#     """
#     # Split genre data into individual words.
#     movies['keyWords'] = movies['genres'].str.replace('|', ' ')
#     # Subset of the data
#     movies_subset = movies[:subset_size]
#     return movies_subset
    

# Function to combine movie features 
def combine_content_features(row):
    return row['title_cast'] + ' ' + row['director'] + ' ' + row['plot_keywords']+ ' ' + row['genres'] + ' ' + row['genome_tags'] + ' ' + row['user_tags'] + ' ' + row['release_decade']


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
    # Creating a copy of the data for use in the content based filter
    content_filter_data = all_movie_data

    # Making sure we convert all text data to string datatype
    content_filter_data['title_cast'] = content_filter_data['title_cast'].astype(str)
    content_filter_data['director'] = content_filter_data['director'].astype(str)
    content_filter_data['plot_keywords'] = content_filter_data['plot_keywords'].astype(str)
    content_filter_data['genres'] = content_filter_data['genres'].astype(str)
    content_filter_data['genome_tags'] = content_filter_data['genome_tags'].astype(str)
    content_filter_data['user_tags'] = content_filter_data['user_tags'].astype(str)
    content_filter_data['release_decade'] = content_filter_data['release_decade'].astype(str)


    # Applying the function
    content_filter_data['combined_features'] = content_filter_data.apply(combine_content_features, axis=1)

    # Subset of the data
    movies_subset = content_filter_data[:subset_size]
    return movies_subset

# # !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# # You are, however, encouraged to change its content.  
# def content_model(movie_list,top_n=10):
#     """Performs Content filtering based upon a list of movies supplied
#        by the app user.

#     Parameters
#     ----------
#     movie_list : list (str)
#         Favorite movies chosen by the app user.
#     top_n : type
#         Number of top recommendations to return to the user.

#     Returns
#     -------
#     list (str)
#         Titles of the top-n movie recommendations to the user.

#     """
#     # Initializing the empty list of recommended movies
#     recommended_movies = []
#     data = data_preprocessing(27000)
#     # Instantiating and generating the count matrix
#     count_vec = CountVectorizer()
#     count_matrix = count_vec.fit_transform(data['keyWords'])
#     indices = pd.Series(data['title'])
#     cosine_sim = cosine_similarity(count_matrix, count_matrix)
#     # Getting the index of the movie that matches the title
#     idx_1 = indices[indices == movie_list[0]].index[0]
#     idx_2 = indices[indices == movie_list[1]].index[0]
#     idx_3 = indices[indices == movie_list[2]].index[0]
#     # Creating a Series with the similarity scores in descending order
#     rank_1 = cosine_sim[idx_1]
#     rank_2 = cosine_sim[idx_2]
#     rank_3 = cosine_sim[idx_3]
#     # Calculating the scores
#     score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
#     score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
#     score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
#     # Getting the indexes of the 10 most similar movies
#     listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)

#     # Store movie names
#     recommended_movies = []
#     # Appending the names of movies
#     top_50_indexes = list(listings.iloc[1:50].index)
#     # Removing chosen movies
#     top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
#     for i in top_indexes[:top_n]:
#         recommended_movies.append(list(movies['title'])[i])
#     return recommended_movies

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
    recommended_movies = []
    data = data_preprocessing(3000)
    
    print('Preprocessing Complete')
    
    # Filter out only necessary features
    content_filter_data = data[['movieId', 'title', 'combined_features']]

    # Filter out movies with no combined features

    # Create list of titles
    content_filter_titles = data['title']

    # Create list of indexes to map titles to data
#     content_filter_indices = pd.Series(data.index, index=data['title'])
    content_filter_indices = pd.Series(data['title'])
    
    print('Vectorize Start')

    # Instantiating and generating the count matrix
    count_vec = CountVectorizer(min_df=CONTENT_VEC_MIN_WORD_TO_REMOVE, stop_words=stopwords.words('english')) # Do not consider features occurring less than 10 times in corpus 
    count_matrix = count_vec.fit_transform(content_filter_data['combined_features'])

    print('Vectorize End')
    
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    print('Cosine Sim End')
    
    # Getting the index of the movie that matches the title
    idx_1 = content_filter_indices[content_filter_indices == movie_list[0]].index.values
    idx_2 = content_filter_indices[content_filter_indices == movie_list[1]].index.values
    idx_3 = content_filter_indices[content_filter_indices == movie_list[2]].index.values
    
    # Creating a Series with the similarity scores in descending order
    rank_1 = np.reshape(cosine_sim[idx_1], (-1, 1)).flatten()
    rank_2 = np.reshape(cosine_sim[idx_2], (-1, 1)).flatten()
    rank_3 = np.reshape(cosine_sim[idx_3], (-1, 1)).flatten()
    
    # Calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
    
    print(score_series_1)
    # Getting the indexes of the 10 most similar movies
#     listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
    listings = pd.concat([score_series_1, score_series_2, score_series_3])
    # Store movie names
    recommended_movies = []
    # Appending the names of movies
    top_50_indexes = list(listings.iloc[1:50].index)
    
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:top_n]:
        recommended_movies.append(list(movies_df['title'])[i])
    return recommended_movies

