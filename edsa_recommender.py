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
    page_options = ["Recommender System","About this App", "Exploratory Data Analysis","Meet the Team","Contact Us"]

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
        
    if page_selection == "About this App":
        st.image('resources/imgs/movieposter.jpg',use_column_width=True)
        st.title("About this App")
        st.markdown(open('about this app.md').read())
        st.image(['resources/imgs/images.jpg'], width=350)
        
    if page_selection == "Meet the Team": 
        st.title("Meet the Team")
        st.markdown(open('untitled3.md').read())
        st.image(['resources/imgs/index.jpg'], width=300)
        
    if page_selection == "Contact Us":
        st.image(['index4.png'], width=300)
        st.title("Contact Us")
        st.markdown(open('contactus.md').read())
        st.image(['index5.jpg'], width=300)
        
    if page_selection == "Exploratory Data Analysis":
        st.image("eda2.jpg",width=300)
        st.title("Exploratory Data Analysis")
        st.markdown("This section will present a brief insight into the data used to build the recommender system for this app. ")
        st.image('Screenshot (31).png',use_column_width=True)
        st.info("Figure 1 Above we can see the most common film genres in the data set. It clear that Drama, Comedy and Thriller are most common, whereas Film-Noir and Imax are the least common.")
        
        st.image('Screenshot (33).png',use_column_width=True)
        st.info("Figure 2 presents the 15 most highly rated movies in the data set. The top 3 rated movies include The Shawshank Redemption, Forrest Gump and Pulp Fiction, all of which were released in 1994.")
        
        st.image('Screenshot (35).png',use_column_width=True)
        st.info("Figure 3 presents a word cloud of the distribution of words appearing in movie titles. The most prominent words are Girl, Love and Boy.")
        
        st.image('Screenshot (37).png',use_column_width=True)
        st.info("Figure 4 presents the number of movies per director. As can be seen Luc Besson, Woody Allen and Stephen King directed the most movies in the data set.")
        
        st.image('Screenshot (39).png',use_column_width=True)
        st.info("Figure 5 presents the most common movie tags in the data set. As can be seen 'based-on'(a true story), 'Comedy', and 'Book' are commonly occuring tags, suggesting that comedies and movies based on true stories or books are popular.")
        
        st.image('Screenshot (41).png',use_column_width=True)
        st.info("Figure 5 present the number of times a genre tag appears in the data set. Most commonly occuring tags include sci-fi, atmospheric and action.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
