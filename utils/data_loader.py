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
    df = pd.read_csv(path_to_movies)
    df = df.dropna()
    movie_list = list(df['title'])
    return movie_list

def load_dataframe(path_to_csv, index):
    """Load train data from database records.

    Parameters
    ----------
    path_to_train : str
        Relative or absolute path to interactions database stored
        in .csv format.

    Returns
    -------
    df : DataFrame
        User Interactions dataframe.

    """
    return pd.read_csv(path_to_csv,index_col=index)