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
    st.sidebar.title("Movie Recommendation System")
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","Recommender System", "Team","Process","Conclusion"]

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
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
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
                    st.error("Oops! Looks like this algorithm doesn't work.\
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
                    st.error("Oops! Looks like this algorithm doesn't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    

    if page_selection == "Welcome":
        st.title("Welcome to your Movie Recommender App")

        st.image('Images/movie_night1.jpg',width = 640)

        st.write("The aim for this application is to give users the ability to discover new movies based on their 3 favourite movies.")

        about = st.sidebar.checkbox("About")
        if about:
            
            
            st.subheader("**Problem Statement**")
            st.markdown("Recommender systems became a useful feature due to the necessity to navigate in the sea of content.\
                        There is a lot of stuff available online,\
                        and many users have a hard time not only finding something they want but even figuring out what it is that they want in the first place.\
                        So,the recommender system is a delicate way of bringing users and relevant content together.\
                        In essence,anything can be recommended or suggested - shoes, clothes, places, films, applications,\
                         browser plugins, memes, music, blog posts, communities, even people or their specific skills, and so on.\
                         All the recommendation system does is narrowing the selection of specific content to the one that is the most relevant to the particular user.")
            
            st.subheader("**Overview**")
            st.markdown("Using the content-based algorithm, the app takes in the user's three favourite movies\
                        then gives the user a list of recommended movies that user can watch and discovered")
    if page_selection == "Team":
        st.title("Meet the team")
    
                
        st.subheader("**Unsupervised AE4**")
        
        st.image("Images/group_member.png", use_column_width=True)
        st.markdown("* Jean-Luc Van Zyl- Team Coordinator")
        st.markdown("* Pearl Matsane")
        st.markdown("* Lydia Lehutjo")
        st.markdown("* Tyrone Khanyile")
        st.markdown("* Katleho Mphuthi")

        st.subheader("**Superviser**")
        st.write("Ali Elimam")
    if page_selection == "Process":
        st.sidebar.subheader("Exploratory Data Analysis")
        
        source = st.sidebar.checkbox("Data Source")
        if source:
            st.subheader("Where did we get the data from?")
            st.image('Images/download.jpg', use_column_width =False)
            st.markdown("The data was obtained from the MovieLens \
            which has the several millions 5-star ratings obtained from users using the online recommendation system.\
            The IMBD (imbd_df) was legally scraped from IMDB.")

        look = st.sidebar.checkbox("Data")
        if look:
            st.subheader("What did the data consists?")
            st.markdown("* Movies -Movie titles are entered manually or imported from https://www.themoviedb.org/, and include the year of release in parentheses")
            st.markdown("* Genome_scores - is a score mapping the strength between movies and tag-related properties.")
            st.markdown("* Genome_tags - User assigned for the movies within the dataset.")
            st.markdown("* Imdb - Additional movie metadata scraped from IMDB using the links.csv file.")
            st.markdown("* Links - File providing a mapping between a MovieLens ID and associated IMDB and TMDB IDs.")
            st.markdown("* Train - The training split of the dataset. Contains user and movie IDs with associated rating data.")


        user = st.sidebar.checkbox("User analysis")
        if user:
            st.subheader("Insights from users")
            st.image('Images/user_analysis.png', width = 720)
            st.markdown("These graphs show the density plots of the average rating of users and the number of movies per user.\
                        What is observed that most of the users rated the movies an avg of 3.5 and most users watched less than 500 movies")
        movies = st.sidebar.checkbox("Movie analysis")
        if movies:
            st.subheader("Insights from Movies")
            st.image('Images/wordcloud.png', use_column_width=False)
            st.markdown("These are most common genres in the dataset!")

        st.sidebar.subheader("Modelling")
        model = st.sidebar.checkbox("Content-based")
        if model:
            st.subheader("Content based Model")
            st.markdown("**Algorithm:**")
            st.markdown("The algorithm that was used was the unsupervised kNN learning best method.\
                        It acts as a uniform interface to three different nearest neighbors algorithms:\
                        BallTree, KDTree, and a brute-force algorithm based on routines in sklearn.metrics.pairwise.\
                        More infomation can be received here:https://scikit-learn.org/stable/modules/neighbors.html#:~:text=1.-,Unsupervised%20Nearest%20Neighbors,based%20on%20routines%20in%20sklearn.")
    
    if page_selection == "Conclusion":
        st.subheader("**Overall conclusion**")
        st.markdown("In this where data is generated at a faster rated than we can use.\
                        With a majority of modern services and products now being offered predominately online,\
                        it can be hard to get to know your customers.\
                        Unlike running a local store where you get to know each person that comes in,\
                        online businesses can struggle to know exactly what their users are expecting.")

        st.subheader("**How can your business use this?**")
        st.markdown("To advances in machine learning, and deep learning specifically,\
                        it is now possible to get to know millions of customers completely online simply through their data.\
                        By using a data model to filter through your users' favorite products and interests,\
                        it is easier than ever to make recommendations to them for what they would enjoy to use or buy.")
            
        st.markdown("Content-based solutions are used by a range of different businesses.\
                        They're probably the most commonly used method and one we have all encountered at some point.\
                        Sites such as Amazon and the Google Play Store are just some of the many examples out there.")


        st.title("Enjoy your movies! ")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.    

if __name__ == '__main__':
    main()
