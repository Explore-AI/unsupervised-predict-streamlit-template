
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
import pickle
from PIL import Image

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
    page_options = ["Recommender System","Solution Overview", "About Us",
                   "Contact Us"]

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
        st.write("This page describes the winning approach.")
                
        def datasets():
            st.markdown("### **_Datasets_**")
            st.write("""
            A snapshot of the data sets used in training and testing the model.
                    """)
            st.markdown("#### **_Train Data_**")
            st.write(pd.DataFrame({"userId": [5163, 106343, 146790],
                                  "movieId": [57669, 5, 5459],
                                  "rating": [4.0, 4.5, 5.0],
                                  "timestamp": [1518349992, 1206238739, 1076215539]}))
            
            st.markdown("#### **_Test Data_**")
            st.write(pd.DataFrame({"userId": [1, 1, 1],
                                  "movieId": [2011, 4144, 5767]}))
                       
        def eda():
            st.markdown("### **_Exploratory Data Analysis_**")
            st.write("""
            A summary of the insights in the movies data set.
                    """)

            # Reads in saved graphs
            bar = """The bar chart describes the number of ratings in millions for each 
            movie in the database scaled from a rating of 0.5 to 5.0. The lowest 
            rated movies are given a 0.5 rating and the highest rated movies are
            given a 4.0. On average the ratings are 3.0 and above indicating
            that the users enjoy the movies in the data set."""
            
            st.image('resources/imgs/Karabo.jpg', caption = bar,  use_column_width = True)
            
            fig = """
            The line chart describes a count of the number of ratings for each movie.
            The shape of the chart indicates a negative relationship between the count
            ratings and the number of movies. This means that a few movies have a 
            higher count of ratings, and as the number of movies increase the count of
            ratings decreases."""
            st.image('resources/imgs/Karabo.jpg', caption = fig, use_column_width = True)
        
        if st.sidebar.button("Datasets"):
            datasets()
        if st.sidebar.button("Exploratory Data Analysis"):
            eda()
        
    if page_selection == "About Us":
        st.title("About Us Tendai")
        
        def team():
            st.markdown("### **_ Our Data Scientists_**")
                       
            siya = Image.open('resources/imgs/Karabo.jpg')
            viwe = Image.open('resources/imgs/Karabo.jpg') 
            mj = Image.open('resources/imgs/Karabo.jpg') 
            tendi = Image.open('resources/imgs/Karabo.jpg')
            b = Image.open('resources/imgs/Karabo.jpg')
            
            st.image([siya, mj, tendi], 
                     caption = ["Siyasanga", "MJ", "Tendani"],
                     width = 150)
            st.image([viwe, b], caption = ["Siviwe", "Bongani"],
                     width = 150)
            
            st.markdown("### **_ Learn more about Team_3_CPT_**")
            st.write("""Like mystery, Siyasanga creates wonder and wonder is the basis of 
                     her desire to understand.""")
            st.write("""Free spirited and adaptable are the truest words that describe 
                     Siviwe. A little something for rainbows and sunny skies to envy.""")
            st.write("Optimism and hardwork is what drives MJ to become a data scientist.")
            st.write("The most friendliest person alive... a simple guy and a simple motto.")
            st.write(""""All I want is to be a real boy in front of a computer begging
                    my program to run." - Bongani""")
             
        def mission():
            st.markdown("### **_Our Mission_**")
            st.write("""
            We are a creative and passionate group of data scientists who are
            on a mission to make a difference in our community by bringing
            innovative programs and projects that promote ingenuity, inclusivity
            and integrity. We want to make our community a better place by 
            giving people tools and information to make better decisions.""")
        
        def statement():
            st.markdown("### **_Problem Statement_**")
            st.write("""
            To construct a recommendation algorithm based on content or 
            collaborative filtering, capable of accurately predicting how
            a user will rate a movie they have not yet viewed based on their 
            historical preferences.""")
        
        def landscape():
            st.markdown("### **_Problem Landscape_**")
            
            st.image('resources/imgs/Karabo.jpg', use_column_width = True)
            st.write("""
            Providing an accurate and robust solution to this challenge has 
            immense economic potential, with users of the system being 
            exposed to content they would like to view or purchase - 
            generating revenue and platform affinity.""")

        def motivation():
            st.markdown("### **_Motivation_**")
            st.write("""Improve customer experience by exposing users to 
            content that matches their taste.""")
            st.write("""Increase sales for service providers.""")
            st.write("""Reduce transaction costs of finding and selecting 
            relevant content in an online platform.""")
            
        if st.sidebar.button("Team"):
            team()
        if st.sidebar.button("Our Mission"):
            mission()
        if st.sidebar.button("Problem Statement"):
            statement()
        if st.sidebar.button("Problem Landscape"):
            landscape()
        if st.sidebar.button("Motivation"):
            motivation()
        
    if page_selection == "Contact Us":
        st.title("Contact Us")
        st.markdown("### **_Have any questions? We would love to hear from you._**")
           
        st.text_input("""Name:""")
        st.text_input("""Surname:""")
        st.text_input("""Email:""")
        st.text_area("""Comment:""")
        st.button("""Submit""")
        
        st.markdown("### **_Contact Info_**")
        st.write("""Tel: 012 589 4856""")
        st.write("""Fax: 012 589 4800""")
        st.write("""Email: info@team3cpt.com""")
        st.write("""Postal Address""")
        st.write("""Private Bag X756, Observatory, Western Cape,
                 South Africa""")

        st.markdown("### **_Social Media_**")
        st.write("""LinkedIn: Team_3_CPT""")
        st.write("""Facebook: Team_3_CPT""")
        st.write("""Instagram: @team_3_cpt""")
        st.write("""Twitter: @team_3_cpt""")
        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()