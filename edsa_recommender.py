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
from streamlit_option_menu import option_menu

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
    page_options = ["Recommender System","Solution Overview","About Us","Contact Us"]
    
    with st.sidebar:
        selection = option_menu("Main Menu", ["Home", "About Us", "Information", "Contact Us"], 
        icons=['house', 'people','graph-up-arrow','info-circle','envelope'], menu_icon="cast", default_index=0)
    
    selected2 = option_menu(None, ["Home", "About Us", "Information", 'Contact Us'], 
    icons=['house', 'people', "list-task", 'info-circle'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


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
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # Building out the "About Us" page
    if page_selection == "About Us":
		# This is our company logo
		#st.image("resources/imgs/LeafLogo.png", caption='Our company logo')

		# Centering the logo image
        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")

        #with col2:
            #st.image("resources/imgs/LeafLogo.png")

        with col3:
            st.write("")

		# You can read a markdown file from supporting resources folder
		#st.title("Who Are We?")
        st.markdown("")
        st.markdown("")

        st.markdown('<div style="text-align: center; color:Black; font-weight: bold; font-size: 30px;">Who Are We?</br></br></div>', unsafe_allow_html=True)

        st.subheader("Intellitech")
        st.markdown('We are a company that creates movie recommender systems and web applications \
					for businesses.\
					Most of what we do revolves around the full Data Science Life Cycle:   \
					')
        st.markdown(f"""
				- Data Collection
				- Data Cleaning
				- Exploratory Data Analysis
				- Model Building
				- Model Deployment
				""")
		#st.subheader("Meet The Team")
        st.markdown('<div style="text-align: center; color:Black; font-weight: bold; font-size: 30px;">Meet The Team</br></br></div>', unsafe_allow_html=True)

        col1, col2, col3, col4, col5, col6 = st.columns(6)
		
        with col1:
			#st.subheader("Caron")
            st.markdown('Ofentse')
            #st.image("resources/imgs/Caron_Sathekge2.jpg")

        with col2:
            #st.subheader("Hlengiwe")
            st.markdown('Caron')
            st.image("resources/imgs/Caron_Sathekge2.jpg")

        with col3:
			#st.subheader("Jade")
            st.markdown('Jade')
            st.image("resources/imgs/Jade.jpg")

        with col4:
			#st.subheader("Palesa")
            st.markdown('Sizakele')
            #st.image("resources/imgs/Palesa3.jpg")

        with col5:
			#st.subheader("Kgotlelelo")
            st.markdown('Rethabile')
            #st.image("resources/imgs/Kgotlelelo2.jpg")

        with col6:
			#st.subheader("Nakedi")
            st.markdown('Thembani')
            #st.image("resources/imgs/Nakedi2.jpg")


if __name__ == '__main__':
    main()
