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
from sklearn.feature_extraction.text import CountVectorizer


# change path to match location of files
sample = pd.read_csv('/home/explore-student/unsupervised_data/sample_submission.csv')
genome_scores = pd.read_csv('/home/explore-student/unsupervised_data/genome_scores.csv')
genome_tags = pd.read_csv('/home/explore-student/unsupervised_data/genome_tags.csv')
train = pd.read_csv('/home/explore-student/unsupervised_data/train.csv')
links = pd.read_csv('/home/explore-student/unsupervised_data/links.csv')
imdb_data = pd.read_csv('/home/explore-student/unsupervised_data/imdb_data.csv')
movies = pd.read_csv('/home/explore-student/unsupervised_data/movies.csv')

def unique_words(s):

    """
    Takes in a string and and returns a string.

    Parameters:
    s (str): A string of words or a sentence.

    Returns:
    (str): A string of unique words.

    """
    unique_list = []
    l = s.split()
    [unique_list.append(x) for x in l if x not in unique_list]
    return ' '.join(unique_list)

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
    # List of movies in test dataset
    test_movies = list(set(test.movieId))

    # List of movies in movies dataset
    movie_movies = list(movies.movieId)

    # List of movies in train dataset
    train_movies = list(set(train.movieId))

    # List of movies in tag dataset
    tag_movies = list(set(tags.movieId))
    
    # Merging all tags of each movie into a sentence like string
    tag4all = []
    for i in tag_movies:
        tag4all.append(' '.join(tags[tags.movieId==i].tag.fillna('').apply(
            lambda x: x.lower().replace(' ',''))))
    
    # Data-frame of merged tags
    tag_df = pd.DataFrame({'movieId':tag_movies,
                           'tag_mash':tag4all},
                          columns=['movieId','tag_mash'])
        
    # Merging all meta-data for each movie in imdb dataset    
    imdb_data.title_cast = imdb_data.title_cast.fillna('').apply(
      lambda x: ' '.join(x.lower().replace(' ','').split('|')))
    
    imdb_data.director = imdb_data.director.fillna('').apply(
      lambda x:x.lower().replace(' ',''))
    
    imdb_data.plot_keywords = imdb_data.plot_keywords.fillna('').apply(
      lambda x: ' '.join(x.lower().replace(' ','').split('|')))
  
    merge_list = []
    for i in imdb_data.index:
        merge_list.append(
            imdb_data.title_cast[i]+' '+imdb_data.director[i]+' '+imdb_data.plot_keywords[i])
    
    new_imdb = pd.DataFrame({'movieId':imdb_data.movieId,
                             'meta_mash':pd.Series(merge_list)},
                            columns=['movieId','meta_mash'])    

    new_train = pd.Series(train_movies).to_frame('movieId')
    
    movies.genres = movies.genres.apply(lambda x:" ".join(x.lower().split("|")))
    
    # copy1-movies, copy2-tag_df, copy3-new_imdb
    # Meging all meta-data to train dataset
    train_gen = pd.merge(new_train, movies, on='movieId',how='left')
  
    train_gen = pd.merge(train_gen, tag_df, on='movieId',how='left').fillna('')

    train_gen = pd.merge(train_gen, new_imdb, on='movieId',how='left').fillna('')

    mash_list = []
    for i in train_gen.index:
        mash_list.append(
            train_gen.genres[i]+' '+train_gen.tag_mash[i]+' '+train_gen.meta_mash[i])

    train_gen['merge_of_all'] = pd.Series(mash_list)
    train_gen.merge_of_all = train_gen.merge_of_all.apply(lambda x: unique_words(x))

    # Subset of the data
    #movies_subset = movies[:subset_size]
    movies_subset = train_gen[:subset_size]
    return movies_subset

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
    data = data_preprocessing(1000) # increase to 27000 for streamlit app
    # Instantiating and generating the count matrix
    count_vec = CountVectorizer()
    count_matrix = count_vec.fit_transform(data['merge_of_all'])
    indices = pd.Series(data['title'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    # Getting the index of the movie that matches the title
    idx_1 = indices[indices == movie_list[0]].index[0]
    idx_2 = indices[indices == movie_list[1]].index[0]
    idx_3 = indices[indices == movie_list[2]].index[0]
    # Creating a Series with the similarity scores in descending order
    rank_1 = cosine_sim[idx_1]
    rank_2 = cosine_sim[idx_2]
    rank_3 = cosine_sim[idx_3]
    # Calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
    # Getting the indexes of the 10 most similar movies
    listings = score_series_1.append(score_series_1).append(score_series_2).append(score_series_3).sort_values(ascending = False)

    # Store movie names
    recommended_movies = []
    # Appending the names of movies
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:top_n]:
        recommended_movies.append(list(movies['title'])[i])
    return recommended_movies

print(data) # choose three titles from dataframe
print(content_model(['<list of chosen movies>']))