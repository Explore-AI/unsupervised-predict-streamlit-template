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
    movie_list = df['title'].to_list()
    return movie_list

#############################################
#               PAGES PATH                  #
#############################################
PAGES_PATH = 'utils/'



#############################################
#               Slides Link                 #
#############################################
SLIDES_LINK = ''


#############################################
#               CSS PATH                 #
#############################################
CSS_PATH = "./utils/css/"

########################################
#           PAGES FUNCTIONS            #    
########################################
def read_file(markdown_file, PAGES_PATH=PAGES_PATH):
    return Path(PAGES_PATH+markdown_file).read_text()

def local_css(file_name):
    with open(CSS_PATH+file_name,  encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)
