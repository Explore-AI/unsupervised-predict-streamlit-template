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
raw_movies = pd.read_csv("resources/data/movies.csv")
raw_ratings = pd.read_csv("resources/data/ratings.csv")


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "About The App", "EDA", "Team Information"]

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
    #if page_selection == "Solution Overview":
        #st.title("Solution Overview")
        #st.write("Describe your winning approach on this page")
        
    if page_selection == "About The App":
        st.title("Solution Overview")
        st.info("Predict Overview: EDSA Movie Recommendation 2022")
		# You can read a markdown file from supporting resources folder
        st.write("""In today’s technology driven world, recommender systems are socially and economically critical to ensure that individuals can make optimised choices surrounding the content they engage with on a daily basis. One application where this is especially true is movie recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.

The goal is to construct a recommendation algorithm based on content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences.

Providing an accurate and robust solution to this challenge has immense economic potential, with users of the system being personalised recommendations - generating platform affinity for the streaming services which best facilitates their audience's viewing.""")
    

        st.image("resources/imgs/Image_header.png",use_column_width=True)
    
        st.subheader("Raw data")
        if st.checkbox('Show movies data'): # data is hidden if box is unchecked
            st.write(raw_movies[['movieId', 'title', 'genres']]) # will write the df to the page

        if st.checkbox('Show ratings data'): # data is hidden if box is unchecked
            st.write(raw_ratings[['userId', 'movieId', 'rating', 'timestamp']])


    if page_selection == "EDA":
        st.title("Explore Data Analysis")

        st.info(""" Exploratory Data Analysis(EDA) allows us to gain a better understanding of our data without having to make any
 assumptions. EDA is a necessary component before moving on to the modeling phase since it provides context and 
 recommendations on how to proceed when creating the proper model. It will also aid in the proper interpretation
 of the results. You will not be able to properly comprehend your data unless you use EDA.""")

        st.write("Here are the highlights of our dataset")
        st.image("resources/imgs/eda screenshot.png",use_column_width=True)
        st.image("resources/imgs/ratings.png",use_column_width=True)

    if page_selection == "Team Information":
        title_about = """
        <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
        <h1 style="color:black;text-align:center;">  21st Century Tech Solutions </h1>
        <h3 style="color:black;text-align:center;"> We provide tailormade solutions for our clients. We pride ourselves in our ability to provide solution which are specifical designed for your needs. </h3>
        """

        mission = """
        <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
        <h1 style="color:black;text-align:center;">  Our Objective  </h1>
        <h3 style="color:black;text-align:center;"> Provide insight from data to provide data driven solutions . &#128515</h3>
        """

        contributors = """
        <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
        <h1 style="color:black;text-align:center;">  Members </h1>
        <h3 style="color:black;text-align:center;">Mandlenkosi Ngidi</h3>
        <h3 style="color:black;text-align:center;">Sboniso Shandu</h3>
        <h3 style="color:black;text-align:center;">Anathi Ncayiyana</h3>
        <h3 style="color:black;text-align:center;">Tsidiso Maselela</h3>
        <h3 style="color:black;text-align:center;">Peter Selolo</h3>

        """

        st.image("resources/imgs/TECHSAV.png",use_column_width=True)
        st.markdown(title_about, unsafe_allow_html=True)
        st.markdown(mission, unsafe_allow_html=True)
        st.markdown(contributors, unsafe_allow_html=True)

        st.info("Github repo url: https://github.com/Sboniso-Shandu/unsupervised-predict-streamlit-template")
        st.info("Kaggle submission url: https://www.kaggle.com/competitions/edsa-movie-recommendation-2022/submissions")
        st.info("AWS EC2 instance url:  ")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
