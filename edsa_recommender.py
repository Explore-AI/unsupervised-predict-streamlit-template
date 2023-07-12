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
    title_template ="""
        <div style="background-color:Black;padding:10px;border-radius:10px;margin:20px;">
        <h3 style="color:white;text-align:center;">UNSUPERVISED ML TEAM</h3>
        <h4 style="color:white;text-align:center;">Mosibudi Sehata</h4>
        <h4 style="color:white;text-align:center;">Thebe Dikobo </h4>
        <h4 style="color:white;text-align:center;">Ayanda Witboi</h4>
        <h4 style="color:white;text-align:center;">Ayanda Ndlovu </h4>
        <h4 style="color:white;text-align:center;">Vasco Eti</h4>
        </div>
        """


    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","Recommender System","Keep Learning","Analysis","Solution Overview"]

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
                    st.title("We think you'll like:")
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

    if page_selection== "Welcome":
        
         st.markdown(html_template.format('blue', 'white'), unsafe_allow_html=True)
         st.image('resources/imgs/Home.jpg',use_column_width=True)

    if page_selection == "Keep Learning":
        st.write("### Oveview: Keep learning on Unsupervised, and manage the skill to generate movie recommendations")

        st.write("Let's go and learn more about Unsupervised Prediction")

        st.subheader("Technology created things for us tob be more Easy")
    
        st.subheader("Data Overview")
        st.write("""This dataset consists of several million 5-star ratings obtained from users of the online MovieLens movie recommendation service. 
                 The <a href="https://movielens.org/">MovieLens</a> dataset has long been used by industry and academic 
                 researchers to improve the performance of explicitly-based recommender systems, and now you get to as well!
                 For this Predict, we'll be using a special version of the MovieLens dataset which has enriched with additional data, 
                 and resampled for fair evaluation purposes.""",unsafe_allow_html=True)

        st.write("""### Source:""")
        st.write("""The data for the MovieLens dataset is maintained by the <a href="https://grouplens.org/">GroupLens</a> research group in the Department of Computer Science and Engineering at the University of Minnesota. 
                 Additional movie content data was legally scraped from <a href="https://www.imdb.com/">IMDB</a>.""", unsafe_allow_html=True)

        st.write("""### Supplied Files:
        - genome_scores.csv: a score mapping the strength between movies and tag-related properties.
        - genome_tags.csv: user assigned tags for genome-related scores
        - imdb_data.csv: additional movie metadata scraped from IMDB using the links.csv file
        - links.csv: file providing a mapping between a MovieLens ID and associated IMDB and TMDB IDs
        - sample_submission.csv: sample of the submission format for the hackathon
        - tags.csv: user assigned tags for the movies within the dataset
        - test.csv: the test split of the dataset. Contains user and movie IDs with no rating data
        - train.csv: the training split of the dataset. Contains user and movie IDs with associated rating data.
        """)


    if page_selection == "Analysis":
        st.title('Exploratory Data Analysis')

        if st.checkbox("ratings"):
            st.subheader("Movie ratings")
            st.image('resources/imgs/rating.PNG',use_column_width=True)

        
        if st.checkbox("genre wordcloud"):
            st.subheader("Top Genres")
            st.image('resources/imgs/genre_wordcloud.png',use_column_width=True)
        
        if st.checkbox("genres"):
            st.subheader("Top Genres")
            st.image('resources/imgs/top_genres.PNG',use_column_width=True)

        if st.checkbox("tags"):
            st.subheader("Top tags")
            st.image('resources/imgs/top_tags.PNG',use_column_width=True)

        if st.checkbox("cast"):
            st.subheader("Popular cast")
            st.image('resources/imgs/cast.PNG',use_column_width=True)

    

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    st.markdown(title_template, unsafe_allow_html=True)

if __name__ == '__main__':
    main()