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
import requests
import json
import base64
import joblib,os
import base64


# Custom Libraries
from utils.data_loader import load_movie_titles
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# background-size: cover

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
st.set_page_config(page_title="Explo Insight", layout="wide", page_icon=":sparkles:")


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-attachment: fixed;
        background-size: cover
       
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
def load_lottieurl(url: str):
    r = requests.get(url)

    if r.status_code != 200:
        return None
    return r.json()    
add_bg_from_local('resources/imgs/the_one_bck.jpg')


load_lottie_home =load_lottieurl ("https://assets3.lottiefiles.com/packages/lf20_khzniaya.json")
# App declaration

def main():
    page_selection = option_menu(
        menu_title= "Explo Insight",
        options = ["Recommender System","Home","Solution Overview", "fun facts","Contact us"],
        icons=["house", "skip-backward", "file-person","book-half", "bar-chart-line-fill"],
        menu_icon =":gem:",
        orientation = "horizontal"
    )
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    
    #page_options = ["Recommender System","Solution Overview","Home", "fun facts","Contact us "]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    #page_selection = st.sidebar.selectbox("Choose Option", page_options)
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
        
    if page_selection == "Home":
        st_lottie(load_lottie_home, speed=1, loop=True, quality="high", width=750, reverse=True)

    if page_selection == "Contact us":
        st.header("Contact us:")
        cont = st.radio("Select how you wan to contact us", ("Leave us a message", "Get in touch with us", "Visit our offices"))
        if cont == "Leave us a message":
            st.info("Name")
            st.text_area("Please enter your Nme")
            st.info("Contact information")
            st.text_area("Please let us know how we can contact you (Email or Cellphone number)")
            st.info("Message ")
            st.text_area("Please leave your message")
            send = st.button("Submit")
           
        if cont == "Get in touch with us":
            st.info("Comming to attend to you")
        if cont == "Come to our offices":
            st.info("Comming to attend to you as well")
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitc.


if __name__ == '__main__':
    main()
