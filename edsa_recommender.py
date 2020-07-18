"""

    Streamlit webserver-based Recommender Engine.

    Author: TEAM_1_DBN.

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.


"""
# Streamlit dependencies
import streamlit as st

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
    page_options = ["Home Page","Recommender System","Data & Insights","Solution Overview", "Exploratory Data Analysis"]

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
        st.write("Describe your winning approach on this page")

    if page_selection == "Home Page":
        st.title("Popcorn Plug")
        st.write("<p style='text-align: left; color: red;'>Make entertainment exciting, again.🔥</p>", unsafe_allow_html=True) 
        st.write("### Welcome to our Machine Learning Movie Recommender App") 
        st.write("The app uses machine learning models to recommend best movies to our users")

        st.write("________________________________________________________________________________")
        # st.write("### Popcorn Plug ")
        # st.write("<p style='text-align: left; color: red;'>Make entertainment exciting, again.🔥</p>", unsafe_allow_html=True) 
        st.image('https://media0.giphy.com/media/dXQlx5RfbNwQVtqMet/giphy.gif?cid=6c09b9526ae25bf2202fbb861880e79c9c35b42b1257517b&rid=giphy.gif',use_column_width=True)
        st.write("________________________________________________________________________________")
        
        st.write("<p style='text-align: center; color: red;'>Find out what to watch next!.</p>", unsafe_allow_html=True) 

    if page_selection == "Data & Insights":
        st.title("Movie Recommender Engine")

        st.write("### Below are some visuals, and insights gained from the data") 
        # st.write("The app uses machine learning models to recommend best movies to our users") 
        
        # st.image('https://media0.giphy.com/media/dXQlx5RfbNwQVtqMet/giphy.gif?cid=6c09b9526ae25bf2202fbb861880e79c9c35b42b1257517b&rid=giphy.gif',use_column_width=True)


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "Exploratory Data Analysis":
        st.title("Exploratory Data Analysis")
        st.write("EDA HERE")


if __name__ == '__main__':
    main()
