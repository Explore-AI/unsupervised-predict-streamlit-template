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
import streamlit as st
import joblib,os
from PIL import Image

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
    page_options = ["Recommender System","About", "Solution Overview"]

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
    if page_selection == "About":
        #Title
        st.title('About')
        st.write('--------------------------------------')
        #introduction
        st.markdown('INTRODUCTION')
        st.info(""""Recommender Systems is a subclass of information filtering system that
                    seeks to predict the "rating" or "preference" a user would give
                    to an item. Recommender systems are used by companies
                    like Youtube, Netflix and Amazon for e-commerce and
                    online advertisement. They are very critical brcause
                    that is how many companies are able to generate money.
                    We have two types of reccomender systems, contet based
                    and collaborative fltering.
                    Collaborative methods for recommender systems are methods
                    that are based solely on the past interactions recorded between
                    users and items in order to produce new recommendations.
                    Unlike collaborative methods that only rely on the user-item
                    interactions, content based approaches use additional information
                    about users and/or items.""")
        st.markdown('EXPLORATORY DATA ANALYSIS')
        from PIL import Image
        i = Image.open("resources/imgs/total_data.PNG")
        st.image(i)
        st.text("     ")
        st.markdown('All about users and ratings')
        rating = Image.open("resources/imgs/rating_dis.PNG")
        st.image(rating)
        st.info("""Integer values have taller bars than the floating values since most
                   of the users assign rating as integer value""")
        st.text("     ")
        from PIL import Image
        day_rating = Image.open("resources/imgs/day_rating.PNG")
        st.image(day_rating, caption='Average number of ratings per day')
        st.info("""We calcated the average rating for each day of the week
                   and we can see that we receive the most ratings on a Sunday and on a Saturday""")
        st.text("     ")
        from PIL import Image
        st.markdown('All about genres and tags')
        bar_genre =Image.open("resources/imgs/bar_genre.PNG")
        st.image(bar_genre, caption='Most common genres')
        st.info("""In the above histogram we can see that the Drama genre seems to be having the
                 most movies tags with a little over 25000 released movies followed by the Comedy
                 genre that has over over 15000 movies. This could possible mean that most ratings
                 are coming from these two genres as well.""")
        if st.button("Wordcloud for Tags"):
            from PIL import Image
            tag = Image.open('resources/imgs/tag_word.PNG')
            st.image(tag, caption='Most common tags', width=650)
        st.text("      ")
        st.markdown("All About movies")
        from PIL import Image
        movie_per = Image.open("resources/imgs/movie_per.PNG")
        st.image(movie_per, caption="Number of movies released per year", width=550)
        st.info("""Number of movies released per year increasing almost exponentially until 2010,
                 then flattening and dropping signifincantly in 2011.""")


    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
