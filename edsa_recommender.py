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
import hydralit_components as hc

# Data handling dependencies
import pandas as pd
import numpy as np
from sympy import im

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import functions.youtube_scrapper as top_trailers
import menu.trailers as t
import menu.data_professionals as dreamers
import menu.statistics as stat
import menu.helper as h
import menu.About as a
import time
# Data Loading
title_list = load_movie_titles('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/movies.csv')

st.set_page_config(page_icon='resources/imgs/MovieXplorer.png', page_title= 'Movie Xplorer', layout='wide', initial_sidebar_state='auto')

over_theme = {'txc_inactive': '#FFFFFF'}

# specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label':'About'},
    {'id':'Trailers','icon':'fas fa-film','label':'Trailers'},
    {'icon': 'far fa-chart-bar', 'label':'Statistics'}, #no tooltip message
    {'id':'Contact Us','icon': 'fas fa-laptop', 'label':'Contact Us'},
    {'id':'Help', 'icon': 'fas fa-question', 'label':'Help'}
]

# App declaration

def main():
    # define hydralit navbar
    menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    
    home_name='Home',
    # login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)
    page_selection = f'{menu_id}'
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    # page_options = ["Recommender System", "About", "Trailers", "Statistics", "The Dream Team", "Help Page"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    # page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == 'Home':
        # Header contents
        st.write('# Movie Xplorer')
        # st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Header2L.gif',use_column_width=True)
        # Recommender System algorithm selection
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;} </style>', unsafe_allow_html=True)
        st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-right:2px;}</style>', unsafe_allow_html=True)
        sys = st.radio("", ('Content Based Filtering', 'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Select Your Three Favorite Movies')
        movie_1 = st.selectbox('1ˢᵗ Movie',title_list[14930:15200])
        movie_2 = st.selectbox('2ⁿᵈ Movie',title_list[25055:25255])
        movie_3 = st.selectbox('3ʳᵈ Movie',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button('Recommend'):
                try:
                    # intialize hydralit loaders
                    with hc.HyLoader('We\'re getting movies only you will love...\n',hc.Loaders.standard_loaders,index=[5,0,3]):
                        # get top 10 recommended movies using the content_model algorithm
                        top_recommendations = content_model(movie_list=fav_movies, top_n=10)
                        time.sleep(5)
                    st.title('Only you will love these movies...')
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        # get trailer from youtube
                        top_trailers.youtubeScrapper(top_recommendations[i])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button('Recommend'):
                try:
                    # intialize hydralit loaders
                    with hc.HyLoader('We\'re getting movies only you will love...\n',hc.Loaders.standard_loaders,index=[5,0,3]):
                        # get top 10 recommended movies using the collab_model algorithm
                        top_recommendations = collab_model(movie_list=fav_movies, top_n=10)
                        time.sleep(5)
                    st.title('Only you will love these movies...')
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        # get trailer from youtube
                        top_trailers.youtubeScrapper(top_recommendations[i])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------
    elif page_selection == 'About':
        # navigate to the About page
        a.about()
    elif page_selection == 'Trailers':
        # navigate to the Trailers page
        t.vids()
    elif page_selection == 'Contact Us':
        # navigate to the Contact Us page
        dreamers.data_professionals()
    elif page_selection == 'Statistics':
        # navigate to the Statistics page
        stat.visuals()
    elif page_selection == 'Help':
        # navigate to the Help page
        h.helppage()
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

if __name__ == '__main__':
    main()
