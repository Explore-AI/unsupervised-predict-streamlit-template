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
    page_options = ["Recommender System","EDA","Solution Overview","About"]
    
 

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

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    # Define the dark theme
    if page_selection == "About":
            # Page layout
            st.title("About")
            st.markdown("---")
    
         # Company Description
            st.header("Welcome to SmrtByte Solutions!")
            st.write("We are a leading technology solutions provider committed to delivering innovative software solutions that solve complex problems.")
    
    # Company Mission
            st.header("Our Mission")
            st.write("Our mission is to empower businesses and individuals by leveraging cutting-edge technologies to drive growth and success.")
    
    # Team Members
            st.header("Our Team")
            st.write("Meet the brilliant minds behind SmrtByte Solutions.")
    
    # Team Members' Profiles
            #st.subheader("John Doe")
            #st.image("john_doe.jpg", caption="Chief Technology Officer")
            #st.write("John Doe is an experienced technologist with a passion for developing scalable and robust solutions.")
    
            st.subheader("The Team")
            Tha = Image.open("resouces/imgs/tha.png")
            st.image(Tha,use_column_width=False, clamp=False, width = 150, output_format="PNG")
            #st.image('C:/Users/thabi/Downloads/Github Clone/unsupervised-predict-streamlit-template/resourcesimgs', use_column_width=True, caption='Lead Software Engineer') 
            #st.write("Jane Smith is a skilled software engineer specializing in backend development and cloud architecture.")
    
    # Contact Information
            st.header("Contact Us")
            st.write("We'd love to hear from you! Get in touch with us:")
            st.write("- Email: info@smrtbytesolutions.com")
            st.write("- Phone: +1 123-456-7890")
    
    # Footer
            st.markdown("---")
            st.write("© 2023 SmrtByte Solutions. All rights reserved.")

import streamlit as st

# Adding an image to the sidebar
#st.sidebar.image('C:/Users/thabi/Downloads/Github Clone/unsupervised-predict-streamlit-template/resources/imgs', use_column_width=True)


# Rest of your Streamlit app code
# ...
 

if __name__ == '__main__':
    main()
