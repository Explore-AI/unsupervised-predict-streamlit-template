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

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')



# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Exploratory Data Analysis", "Solution Overview"]

    st.sidebar.image("default.png", use_column_width=True)
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

        st.write("Collaborative filtering is the process of predicting the interests of a user by identifying preferences and information from many users. This is done by filtering data for information or patterns using techniques involving collaboration among multiple agents, data sources, etc. The underlying intuition behind collaborative filtering is that if user A and B have similar taste in a product, then A and B are likely to have similar taste in other products as well.")
        st.image("model-based.png")
        st.write("Memory based approaches — also often referred to as neighbourhood collaborative filtering. Essentially, ratings of user-item combinations are predicted on the basis of their neighbourhoods. This can be further split into user based collaborative filtering and item based collaborative filtering. User based essentially means that likeminded users are going to yield strong and similar recommendations. Item based collaborative filtering recommends items based on the similarity between items calculated using user ratings of those items.")
        st.write("Model based approaches — are predictive models using machine learning. Features associated to the dataset are parameterized as inputs of the model to try to solve an optimization related problem. Model based approaches include using things like decision trees, rule based approaches, latent factor models etc.")

    if page_selection == "Exploratory Data Analysis":
        title_eda = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Exploratory Data Analysis</h1>
        """

        st.image('Exploratory-Analysis-Banner-940px.jpg',use_column_width=True)
    
        sys_eda = st.selectbox("Choose an EDA section suitable for you",
        ('Ratings','Movies','Directors','Genres'))

        if sys_eda == "Ratings":

                op_ratings = st.radio("Choose an option under ratings",("Rating distribution","Percentage of users per rating"))

                if op_ratings == "Percentage of users per rating":
                    st.image('users-per-rating.png',use_column_width=True)
                if op_ratings == "Rating distribution":
                    st.image('rating-distribution.png',use_column_width=True)

        if sys_eda == "Genres":
            op_genre = st.radio("Choose an option under Genres",("Genre distribution","Word cloud of movie genres"))
            if op_genre == "Genre distribution":
                st.image('popular-genres.png')
            if op_genre == "Word cloud of movie genres":
                st.image('popular-genres2.png',use_column_width=True)  

        if sys_eda == "Directors":            
            op_director = st.radio("Choose an option under directors", ("Top 25 most rated directors","Top 25 directors with most number of movies","10 highest rated director with over 10000 ratings","10 worst rated directors with over 10000 ratings")) 
            if op_director == "Top 25 most rated directors":
                st.image('top_25_most_D1.png',use_column_width=True)
            if op_director == "Top 25 directors with most number of movies":
                st.image('Top_25_directors_D2.png',use_column_width=True)
            if op_director == "10 highest rated director with over 10000 ratings":
                st.image('10_highest_rated_D3.png',use_column_width=True)
            if op_director == "10 worst rated directors with over 10000 ratings":
                st.image('10_worst_directors_D4.png',use_column_width=True)
                        
        if sys_eda == "Movies":
                op_movies = st.radio("Choose an option under movies",("Top 25 most rated movies of all time","25  most rated movies of the 21st century","Top 10 best and worst rated movies with over 10000 ratings","Total movies released per year"))
                if op_movies == "Top 25 most rated movies of all time":
                    st.image('25_most_1.png',use_column_width=True)
                if op_movies == "25  most rated movies of the 21st century":
                    st.image('25_most_2.png',use_column_width=True)
                if op_movies == "Top 10 best and worst rated movies with over 10000 ratings":
                    st.image('10_best_3.png',use_column_width=True)
                    st.image('10_worst_4.png',use_column_width=True)
                if op_movies == "Total movies released per year":
                    st.image('Total_5.png',use_column_width=True)         

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

if __name__ == '__main__':
    main()
