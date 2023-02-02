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
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import joblib,os
from PIL import Image
import requests
import json

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
ratings = pd.read_csv('resources/data/ratings.csv')

# App declaration
def main():
    st.set_page_config(page_title="Movie Recommender Engine",
                       page_icon=":guardsman:",
                       layout="wide")
                    #    background_color="#F4EFEF")
                       
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","EDA","Solution Overview","About Us", "Improvements",]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------

    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Data Innovate Movie Recommender Engine')
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


   
    if page_selection == "EDA":
        st.title('Exploratory Data Analysis')
        st.image('./resources/imgs/ratings_distribution.png', use_column_width=True)
        st.markdown(' This graph shows The Distribution Of Ratings')
        st.markdown('--------')  
    
        st.image('./resources/imgs/PopularGenre.png', use_column_width=True)
        st.markdown(' This graph shows Popular Genres')
        st.markdown('--------')

        # st.image('./resources/imgs/popular actors.PNG', use_column_width=True)
        # st.markdown('This graph shows the top 20 of popular actors')
        # st.markdown('--------')

        # st.image('./resources/imgs/number of movie per director.PNG', use_column_width=True)
        # st.markdown('This graphs shows the number of movies per director ')
        # st.markdown('--------')

        # st.image('./resources/imgs/rating per user.PNG', use_column_width=True)
        # st.markdown('This graph shows the rating per user')
        # st.markdown('--------')

        # st.image('./resources/imgs/total movie release per year.PNG', use_column_width=True)
        # st.markdown('The graph shows the total movies release per year')
        # st.markdown('--------')

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("At Data Innovate, we understand the importance of providing accurate and reliable movie recommendations. That's why we compared five different models - SVD, BaseOnly, CoClustering, SVDpp, and SlopeOne - to determine which one would provide the best results. At Data Innovate, we believe in using the best tools and techniques to deliver the most accurate recommendations to our users. The SVD model is a testament to this commitment and provides our users with a movie-watching experience that is second to none.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    if page_selection == "About Us":

        st.title("About Us")
        col1, col2 = st.columns((2, 1))
        with col1:
            st.title("Background")
            st.write("##")
            st.write("Welcome to Data Innovate, a cutting-edge data science company founded in 2023 by a team of young, ambitious, talented, and hardworking individuals in South Africa. We specialize in leveraging the latest technologies and techniques to extract insights and knowledge from data, empowering our clients to make data-driven decisions and drive innovation. Our team of experts includes data scientists, data engineers, machine learning engineers, business intelligence analysts, big data engineers, and data governance analysts, all dedicated to providing our clients with the best possible solutions. We pride ourselves on being able to understand our clients' unique needs and tailor our services to fit their specific requirements. We specialize in a wide range of industries, including finance, entertainment, healthcare, retail, and manufacturing, and our services include data analysis, machine learning, predictive modelling, and big data management. We use the latest tools and technologies to provide our clients with accurate, actionable insights that can be used to drive growth and improve operations. If you're looking to harness the power of data to drive your business forward, look no further than Data Innovate. Contact us today to learn more about how we can help you achieve your goals")
            st.write("##")
       
        with col2:
            st.write("###") 
            st.write("###") 
            st.write("###")  
            st.write("###")
            st.write("###") 
        st.subheader("")
        st.subheader("Team")
        fig_col1, fig_col2,fig_col3,fig_col4,fig_col5,fig_col6 = st.columns(6)
        with fig_col1:
            image_climate = Image.open(os.path.join("resources/imgs/Risima.jpg"))
            image_climate = image_climate.resize((300,300))
            st.image(image_climate, caption='CEO: Risima')

        with fig_col2:
            image_climate = Image.open(os.path.join("resources/imgs/Karabo.jpg"))
            image_climate = image_climate.resize((300,300))
            st.image(image_climate, caption='Chief Technical Officer: Karabo')

        with fig_col3:
            image_climate = Image.open(os.path.join("resources/imgs/Jackie.jpeg"))
            image_climate = image_climate.resize((300,300))
            st.image(image_climate, caption='Client Liason: Jackie')

        with fig_col4:
            image_climate = Image.open(os.path.join("resources/imgs/Tiyisela.jpeg"))
            image_climate = image_climate.resize((300,300))
            st.image(image_climate, caption='Chief Information Officer: Tiyisela')

        with fig_col5:
            image_climate = Image.open(os.path.join("resources/imgs/Daisy.jpeg"))
            image_climate = image_climate.resize((300,300))
            st.image(image_climate, caption='Data Scientist: Daisy')
        
        with fig_col6:
            image_climate = Image.open(os.path.join("resources/imgs/Thibello.jpeg"))
            image_climate = image_climate.resize((300,300))
            st.image(image_climate, caption='Data Scientist: Thibello')
    
    if page_selection == "Improvements":
        
        with st.form("my_form",clear_on_submit=True):
           
            st.title("Improvements")
            st.text_area("Describe we can make your experience better when using the app")

            if (st.form_submit_button(label="Submit", help=None, on_click=None, args=None, kwargs=None, disabled=False)):
                st.success("Thank you for your feedback👍!!!!")
            st.image('resources/imgs/Data_Innovate_logo.png',use_column_width=True)


if __name__ == '__main__':
    main()