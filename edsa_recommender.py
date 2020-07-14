"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from PIL import Image
#Plots
import seaborn as sns
import matplotlib.style as style 
sns.set(font_scale=1)
import matplotlib.pyplot as plt
#import plotly.figure_factory as ff

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

data_path = '../unsupervised_data/unsupervised_movie_data/'
#dataframe of movie titles
#def genre_titles(filename,genre):
#    filename = '../edsa-recommender-system-predict/'+str(filename)
#    chunks = pd.read_csv(filename,chunksize=10000)
#    data = pd.DataFrame()
#    for chunk in chunks:
#        chunk = chunk[chunk.genres.apply(lambda x: genre in x)]
#        data = pd.concat([data,chunk])
#    data = data.title.tolist()
#    return(data)

# Function to chunk data and calculated genre distribution

def genre_count(filename):
    '''Plots the distribution of genres in the movies dataset'''
    filename = data_path+str(filename)
    chunks = pd.read_csv(filename,chunksize=10000)
    data = pd.DataFrame()
    count = 0
    dict_genres = {}
    for chunk in chunks:
        chunk_genres = ','.join([genres.replace('|',',').lower() for genres in chunk.genres]).split(',')
        chunk_genres = [item for item in chunk_genres if item != '(no genres listed)']
        for genre in chunk_genres:
            if genre in dict_genres:
                dict_genres[genre]+=1
            else:
                dict_genres[genre]=1
    sorted_dict = sorted(dict_genres.items(), key=lambda x: x[1],reverse=True)
    genre, frequency = zip(*sorted_dict)
    plt.figure(figsize=(10,5))
    freq_plot = sns.barplot(x = frequency,y = list(genre),palette='pastel')
    freq_plot.set(title='Genre frequency',
                  xlabel='Genre_count',ylabel='Genre')
    plt.show()
    return (freq_plot)

# Data Loading

#title_list = load_movie_titles('resources/data/movies.csv')
#ratings = pd.read_csv('../edsa-recommender-system-predict/train.csv')

def background_setup(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ['Welcome','Reccomender','EDA','Solution Overview','About']

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox('Choose Option', page_options)
    if page_selection == 'Welcome':
        def background_setup(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        background_setup('home_style.css')
#         Header contents
#        st.write('# Nextflix')
        st.image('resources/imgs/home_page/nextflix_home.png')
    if page_selection =='Reccomender':
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
#        Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))
#
        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]
#
#        Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
#
#
        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == 'EDA':
        def genre_count(filename):
            '''Plots the distribution of genres in the movies dataset'''
            filename = data_path+str(filename)
            chunks = pd.read_csv(filename,chunksize=10000)
            data = pd.DataFrame()
            count = 0
            dict_genres = {}
            for chunk in chunks:
                chunk_genres = ','.join([genres.replace('|',',').lower() for genres in chunk.genres]).split(',')
                chunk_genres = [item for item in chunk_genres if item != '(no genres listed)']
                for genre in chunk_genres:
                    if genre in dict_genres:
                        dict_genres[genre]+=1
                    else:
                        dict_genres[genre]=1
            sorted_dict = sorted(dict_genres.items(), key=lambda x: x[1],reverse=True)
            genre, frequency = zip(*sorted_dict)
            plt.figure(figsize=(10,5))
            freq_plot = sns.barplot(x = frequency,y = list(genre),palette='pastel')
            freq_plot.set(title='Genre frequency',
                          xlabel='Genre_count',ylabel='Genre')
            plt.show()
            return (freq_plot)
        st.title('EDA') 
        genres_setlist = ['Action','Adventure','Animation','Children','Comedy','Crime','Documentary',
                          'Drama','Fantasy','Horror','Mystery','Romance','Sci-fi','Thriller','War','Western']
        genres = st.multiselect('select genres',genres_setlist)
        st.write(genres)
        st.write(genre_count('movies.csv').figure)

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
