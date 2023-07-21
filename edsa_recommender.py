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
import os
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
    page_options = ["Welcome","Recommender System","Analysis","Solution Overview"]

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
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("The best you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    html_template = """
        <div style="background-color:black;padding:10px;border-radius:10px;margin:10px;">
        <h1 style="color:Blue;text-align:center;">EDSA Movie Recommendation Challenge</h1>
        </div>
        """

    if page_selection == "Welcome":
        st.title("Welcome to the Data Detectives Movie Recommender Engine")
        
        # Display the image
        st.image('resources/imgs/Home.jpg', use_column_width=True)
        
        # Display formatted text using Markdown
        st.markdown("""
        # Movie Recommendation Challenge
        
        Welcome to our Movie Recommender Engine! We hope you'll find some great movie recommendations here.
        
        ### How it works:
        
        1. Select your three favorite movies from the drop-down lists.
        2. Choose either Content Based Filtering or Collaborative Based Filtering.
        3. Click the "Recommend" button to get personalized movie recommendations.
        
        ### About us:
        
        We are the Unsupervised ML team at EDSA, working on this amazing Movie Recommender Engine.
        
        - Mosibudi Sehata
        - Thebe Dikobo
        - Ayanda Witboi
        - Ayanda Ndlovu
        - Katsila Malepe
        - Maseru Mashiloane
        - Vasco Eti
        
        Happy movie watching!
        """)

        # Display the second image
        st.image('resources/imgs/Image2.jpg', use_column_width=True)
        
        # Display the third image
        st.image('resources/imgs/Image3.jpg', use_column_width=True)
        
        # Display the fourth image
        st.image('resources/imgs/Image4.jpg', use_column_width=True)

    if page_selection == "Analysis":
        st.title('Exploratory Data Analysis')

        if st.checkbox("ratings"):
            st.subheader("Movie ratings")
            img_path = os.path.join("resources", "imgs", "rating.jpg")
            st.image(img_path, use_column_width=True)
        
        if st.checkbox("genres"):
            st.subheader("Top Genres")
            img_path = os.path.join("resources", "imgs", "top_genres.jpg")
            st.image(img_path, use_column_width=True)

        if st.checkbox("tags"):
            st.subheader("Top tags")
            img_path = os.path.join("resources", "imgs", "top_tags.jpg")
            st.image(img_path, use_column_width=True)

        if st.checkbox("cast"):
            st.subheader("Popular cast")
            img_path = os.path.join("resources", "imgs", "cast.jpg")
            st.image(img_path, use_column_width=True)

    

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
 

if __name__ == '__main__':
    main()
