"""

    Helper functions for data loading and manipulation.

    Author: Explore Data Science Academy.

"""
# Data handling dependencies
import pandas as pd
import numpy as np
import streamlit as st




def load_movie_titles(path_to_movies):
    """Load movie titles from database records.

    Parameters
    ----------
    path_to_movies : str
        Relative or absolute path to movie database stored
        in .csv format.

    Returns
    -------
    list[str]
        Movie titles.

    """
    # ratings_df = pd.read_csv('resources/data/ratings.csv')
    df = pd.read_csv(path_to_movies)
    df = df.dropna()
    # df = df[df.movieId.isin(ratings_df.movieId.values.tolist())]
    movie_list = df['title'].to_list()
    return movie_list

# movies[movies.movieId.isin(train.movieId.values.tolist())].title.values.tolist()