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
    page_options = ["About The App", "Recommender System","Solution Overview","Exploratory Data Analysis", "App Developers Contacts"]

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
        st.write("We used two recommendation approaches for this App i.e. Content Based Filtering which recommend movies based on movie similarity and and collaborative Based Filtering which recommend movies based on users  user similarity")
        st.title("Content Based Filtering")
        st.image('resources/imgs/EDSA_logo.png',use_column_width=True)#put the correct one
        st.write("This filtration strategy is based on the data provided about the items. The algorithm recommends products that are similar to the ones that a user has liked in the past.\
        This similarity (generally cosine similarity) is computed from the data we have about the items as well as the user’s past preferences. \
        For example, if a user likes movies such as 'The Hobbits' then we can recommend him movies with the genre Adventure or maybe even movies directed by Peter Jackson.")
        st.title("Collaborative Based Filtering")
        st.image('resources/imgs/EDSA_logo.png',use_column_width=True)#put the correct one
        st.write("This filtration strategy is based on the combination of the user’s behavior and comparing and contrasting that with other users’ behavior in the database. It makes recommendations based on movies that those users rated.")
    
    if page_selection == "About The App":
        #st.image(("resources/imgs/team6.PNG", format='PNG')
        st.image('resources/imgs/team_ae.png',use_column_width=True)
        st.title("About The App") 
        st.markdown(""" Team AE6 has deployed Machine Learning Algorithm that are able to recommend good movies according to movie-lovers state and are able to answer the frustrating recurring question “What movies should I watch today?”.
        The algorithm deployed is able to recommend good movies based on Content-Based recommender and recommends movies based on relationship between various movies. 
        Puzzled by what you should you offer your Movie-lovers to watch from your Movie Site?
        Then this is the platform to explore and offer better alternative to your Movie-lover subscribers""")
    
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "Exploratory Data Analysis":
        st.title("Data Analysis Plots")
        if st.checkbox("Ratings insights"):
            st.subheader("These plots give insights about the ratings given for the movies")
           # st.image('resources/imgs/distribution_of_ratings.png',use_column_width=True)
            st.write("This is a count of movies that have been given a certain rating with 5 being")
            st.image('resources/imgs/ratingcount_per_user.png',use_column_width=True)
            st.image('resources/imgs/rated1.png',use_column_width=True)
            st.write("These are the 20 most rated movies. In the top 10 we only have movies from the 90s, with 1994 taking the top 3 spots.")
            st.image('resources/imgs/rating_per_release_year.png',use_column_width=True)
            
        if st.checkbox("Movie Insights"):
            st.subheader("A number of factors influence movie choices and below we take a look at \
                    some of those factors such as popular themes, actors, directors and era")
            st.write("The average movie runtime is 116.1 minutes which equates to ~1.9 hours.")
            st.image('resources/imgs/team_ae.png',use_column_width=True)
            st.write("Drama holds the most number of movies in the database followed by comedy and action.")
            st.image('resources/imgs/team_ae.png',use_column_width=True)
            st.write("The graph below shows the distribution on movies in the dataset. At first glance, \
                it is clear that the 2010s have the highest number of movies released in one decade.")
            st.image('resources/imgs/team_ae.png',use_column_width=True)
            st.write("These are the most popular themes. The keywords are a reflection of the top 3 genres \
                    in the database (drama, comedy and action). If you watch movies in these genres it is \
                    likely that the movie will have these keywords and that is why these movies have high age \
                    restictions. The keywords also show what themes people enjoy watching.")
            st.image('resources/imgs/team_ae.png',use_column_width=True)
            st.image('resources/imgs/team_ae.png',use_column_width=True)
            st.write("The graph above shows the number of times movies with specific actors in the dataset \
                    have been rated. Tom Hanks takes the lead with more than 195000 movie ratings to his name.\
                    In second place is Samuel L.Jackson followed by Morgan Freeman in third place. It makes sense \
                    that the top 3 actors with the most ratings associated with their names also star in the top \
                    3 most rated movies (refer to 'most rated movies' section). It is important\
                    to note that most of the movies in this database are American based and therefore \
                    the most popular actors are American.")
            st.image('resources/imgs/team_ae.png',use_column_width=True)    
        
       
        
    if page_selection == "App Developers Contacts":
        st.title('Project Members and their contact details')
        st.write('Mohale J: johnjeymohale@gmail.com')
        st.write('Muleka K: khuliso.muleka@gmail.com')
        st.write('Phahla M: maririasere@gmail.com')
        st.write('Sewnath K: kirensewnath@gmail.com')
        st.write('Sodo B:bhalisasodo@gmail.com')
        st.write('Manabalala S:sellomanabalala@gmail.com') 

if __name__ == '__main__':
    main()
