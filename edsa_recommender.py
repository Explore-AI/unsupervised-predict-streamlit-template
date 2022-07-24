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
import streamlit.components.v1 as components


# Data handling dependencies
import pandas as pd
import numpy as np

import requests
from PIL import Image
import codecs

# Custom Libraries
from utils.data_loader import load_movie_titles
from utils.load import local_css
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

#visualizations
import base64
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
import seaborn as sns
from wordcloud import WordCloud
import sweetviz as sv
_lock = RendererAgg.lock

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
links = pd.read_csv('resources/data/movies_link.csv')
movies_df = pd.read_csv('./resources/data/movies.csv')
imdb_data= pd.read_csv('./resources/data/imdb_data.csv')
tags = pd.read_csv('./resources/data/tags.csv')


# App declaration
def main():
    #load company logo
    st.sidebar.image("resources/imgs/logoo.gif")


    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "About Elite", "Movie Insights on EDA","SweetViz"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
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
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.subheader("Elite Consultancy")
        st.write("In this project, we succeeded in building an unsupervised machine learning model that is able to recommend movies based on content-based or collaborative filtering and is capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences. Our top performing model has a root mean squared error (RMSE) of 0.78, based on a testing set submitted to the EDSA Kaggle competition.")
        st.write("The singular value decomposition (SVD) algorithm is a baseline approach to recommender systems, as it has a broad range of applications including dimensionality reduction, solving linear inverse problems, and data fitting. The SVD algorithm generally performs better on large datasets compared to some other models as it decomposes a matrix into constituent arrays of feature vectors corresponding to each row and each column.")
        st.write("Have you ever imagined how Amazon Prime, Netflix, and Google predict your taste in movies so easily? It is no rocket science, that after completing one movie/series you loved, and rated it on these platforms, a few more adds up to the suggested or ‘You May Like this ‘ section in seconds! It is Machine Learning. A recommendation system predicts and filters user preferences after learning about the user’s past choices. As simple as that!")


        st.markdown("<h2 style='text-align: center; color: white;'>Content Based Filtering</h2>", unsafe_allow_html=True)
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.image('resources/imgs/content based filtering.png',use_column_width=True)
        with col2:
            st.write('')
            st.markdown("<p style='text-align: center; color: white;'>Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.:</p>", unsafe_allow_html=True)
        
        st.markdown("<h2 style='text-align: center; color: white;'>Collaborative Filtering</h2>", unsafe_allow_html=True)
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.image('resources/imgs/collaborative filtering 2.png')
        with col2:
            st.markdown("<p style='text-align: center; color: white;'>Collaborative filtering uses algorithms to filter data from user reviews to make personalized recommendations for users with similar preferences. This is the hallmark for Recommender Systems, Giving greater insights into what users/customers are interested</p>", unsafe_allow_html=True)
    
    if page_selection == "About Elite":
        #st.markdown("<h1 style='text-align: center; color: white;'>The Elites</h1>", unsafe_allow_html=True)
        st.image('resources/imgs/logo.jpg', width=700)
        st.image('resources/imgs/emma.jpeg',use_column_width=True)
        st.markdown("<p style='text-align: center; color: white;'>Fielami Emmanuel David</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: white;'>Chief Executive Officer</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: white;'>emmzytamara2@gmail.com</p>", unsafe_allow_html=True)
        st.image('resources/imgs/team.jpg',use_column_width=True)
        st.image('resources/imgs/team2.jpg',use_column_width=True)
        
        st.markdown("<h2 style='text-align: center; color: white;'>Contact Info</h2>", unsafe_allow_html=True)
        col = st.columns(1)
        st.image('resources/imgs/team3.jpg',use_column_width=True)
        
        st.markdown("<p style='text-align: center; color: white;'>We recommend that taking the recommendation engine to production and integrate with the movie streaming service to help boost viewers satisfaction and revenue for our client.</p>", unsafe_allow_html=True)
    if page_selection == "Movie Insights on EDA":
        st.title("Movies Insights")
        st.image('resources/imgs/logo.jpg', width=250)
        st.info("we allow you to visualize movies and user analytics, so that you can understand the user's behaviors")
        plotviz = ["select for EDA", "-- movie rating distribution",
                "-- Genre popularity trend",
                "-- Top Actors in most Movies",
                "-- Top directors with Most Movies", 
                "-- Most popular keywords"]
        plot_selection = st.sidebar.selectbox("Select visualisation", plotviz)
        if plot_selection == "-- movie rating distribution":
             st.image("resources/imgs/rating distribution.png",use_column_width=True)
             st.write("Most movies where scored with a rating of 4 stars with 26.6%. Indicating that most users have not had to be subjected films like BALLISTIC: ECKS VS. SEVER which is the lowest rated film of all time on Rotten Tomatoes")
        if plot_selection == "-- Genre popularity trend":
            st.image("resources/imgs/popularity trend.png",use_column_width=True)
        if plot_selection == "-- Top Actors in most Movies":
            st.image("resources/imgs/actors.png",use_column_width=True)
        if plot_selection == "-- Top directors with Most Movies":
            st.image("resources/imgs/movie directors.png",use_column_width=True)
        if plot_selection == "-- Most popular keywords":
            st.image("resources/imgs/keywords.png",use_column_width=True)
    if page_selection == "SweetViz":
        def st_display_sweetviz(report_html,width=1000,height=500):
	        report_file = codecs.open(report_html,'r')
	        page = report_file.read()
	        components.html(page,width=width,height=height,scrolling=True)
        st.image('resources/imgs/sweetviz.png',use_column_width=True)
        st.markdown('Automated EDA with Sweetviz .SweetViz Library is an open-source Python library that generates beautiful, high-density visualizations to kickstart EDA with 2 code lines.')
        ds = st.radio("Choose the data source", ("movies data", "ratings data","imdb data"))
        if ds == "movies data":
            data_file = 'resources/data/movies.csv'
        elif ds == "ratings data":
            data_file = 'resources/data/ratings.csv'
        else:
            data_file = 'resources/data/imdb_data.csv'
        if data_file is not None:
            df1 = pd.read_csv(data_file)
            st.dataframe(df1.head())
            if st.button("Generate Sweetviz Report"):
                report = sv.analyze(df1)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")

        pass
        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
