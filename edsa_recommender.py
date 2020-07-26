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

#Pulls head links
def bfind_head(text_full_string):
	bt_block = ''
	return_var = 0
	for line in text_full_string:
		if '#HEAD\n' == line:
			return_var = 1
			continue
		if return_var == 1:
			if '#HEAD_END\n' == line:
				break
			else:
				bt_block += line
	return bt_block

#Pulls home page
def bfind_home(text_full_string):
	bt_block = ''
	return_var = 0
	for line in text_full_string:
		if '#HOME_PAGE\n' == line:
			return_var = 1
			continue
		if return_var == 1:
			if '#HOME_PAGE_END\n' == line:
				break
			else:
				bt_block += line
	return bt_block

#Loads in bootstrap html block to use in st.markdown. For Raw Data Section
def bfind_raw_data(text_full_string):
	bt_block = ''
	return_var = 0
	for line in text_full_string:
		if '#RAW_DATA\n' == line:
			return_var = 1
			continue
		if return_var == 1:
			if '#RAW_DATA_END\n' == line:
				break
			else:
				bt_block += line
	return bt_block

#Pulls home page
def bfind_home2(text_full_string):
	bt_block = ''
	return_var = 0
	for line in text_full_string:
		if '#HOME_2\n' == line:
			return_var = 1
			continue
		if return_var == 1:
			if '#HOME_2_END\n' == line:
				break
			else:
				bt_block += line
	return bt_block

#Pulls home page
def bfind_about(text_full_string):
	bt_block = ''
	return_var = 0
	for line in text_full_string:
		if '#ABOUT\n' == line:
			return_var = 1
			continue
		if return_var == 1:
			if '#ABOUT_END\n' == line:
				break
			else:
				bt_block += line
	return bt_block

#load in local css styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

bootstrap_blocks = open('bootstrap.txt','r')
text_full_string = bootstrap_blocks.readlines()

RAW_DATA = bfind_raw_data(text_full_string)
HOME_PAGE = bfind_home(text_full_string)
HEAD = bfind_head(text_full_string)
ABOUT = bfind_about(text_full_string)
#HOME_2 = bfind_home2(text_full_string)
#print(HOME_2)
local_css('styles.css')

st.markdown(HEAD,unsafe_allow_html=True)
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home Page","Movie Recommenders","Statistics and insights","Meet the team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == 'Home Page':
        st.markdown(HOME_PAGE, unsafe_allow_html=True)
        #st.markdown(HOME_2,unsafe_allow_html=True)
    if page_selection == "Movie Recommenders":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering',
                        'Popularity Based'))

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
    if page_selection == "Statistics and insights":
        insight_selection = st.selectbox('Data Exploration',['Raw Data','Distribution plot for ratings','Top 15 Genres',\
                                         'Ratings over time (1995 - 2019)','Popular words in movie descriptive data'])
        if insight_selection == "Raw Data":
            bootstrap_block_1 = RAW_DATA
            bootstrap_block_1 = bootstrap_block_1.replace('$$', 'The data set use for training')
            bootstrap_block_1 = bootstrap_block_1.replace('&&',
                                                          "<ul>This is the training dataset it contains the following values" \
                                                          "<li><b>moviesId</b> - the id values given to the movie</li>" \
                                                          "<li><b>userId</b> - the id values given to the movie</li><ul>")
            st.markdown(bootstrap_block_1, unsafe_allow_html=True)
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    if page_selection == 'Meet the team':
        st.markdown(ABOUT,unsafe_allow_html=True)
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
