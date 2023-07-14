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
gen=pd.read_csv("resources/data/aggregated_rating_streamlit.csv")
mov=pd.read_csv("resources/data/movie_details_average.csv")
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Instruction & Overview", 'Genre Insights', 'Movie Insights', 'Contact Us']

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
    if page_selection == "Instruction & Overview":
        st.title("Instruction & Overview")
        st.write("Type how to work the app")
        st.write("Overview of the pages")
    
    if page_selection == "Genre Insights":
        st.markdown("<h2 style=color:#3FBEBF;>Top Rated Movies By Genres</h2>",unsafe_allow_html=True)
        col1,mid,col2=st.columns([40,2,60])
        with col1:
            act=st.checkbox("Action")
            war=st.checkbox("War")
            rom=st.checkbox("Romantic")
            com=st.checkbox("Comedy")
            drm=st.checkbox("Drama")
            adv=st.checkbox("Adventure")
            sf=st.checkbox("Sci-fi")
            thr=st.checkbox("Thriller")
            ani=st.checkbox("Animation")
            doc=st.checkbox("Documentary")
            chi=st.checkbox("Children")
            fan=st.checkbox("Fantasy")
            cri=st.checkbox("Crime")
            hor=st.checkbox("Horror")
            mys=st.checkbox("Mystery")
            im=st.checkbox("IMAX")
            mus=st.checkbox("Musical")
            wes=st.checkbox("Western")
            fil=st.checkbox("Film-Noir")

            ls="True"
            btn=st.button("Explore")

        if btn:
            if act:
                ls=ls+"& gen['Genres'].str.contains(\"Action\")"
            if war:
                ls=ls+"& gen['Genres'].str.contains(\"War\")"
            if rom:
                ls=ls+"& gen['Genres'].str.contains(\"Romance\")"
            if com:
                ls=ls+"& gen['Genres'].str.contains(\"Comedy\")"
            if drm:
                ls=ls+"& gen['Genres'].str.contains(\"Drama\")"
            if adv:
                ls=ls+"& gen['Genres'].str.contains(\"Adventure\")"
            if sf:
                ls=ls+"& gen['Genres'].str.contains(\"Sci-Fi\")"
            if thr:
                ls=ls+"& gen['Genres'].str.contains(\"Thriller\")"
            if ani:
                ls=ls+"& gen['Genres'].str.contains(\"Animation\")"
            if doc:
                ls=ls+"& gen['Genres'].str.contains(\"Documentary\")"
            if chi:
                ls=ls+"& gen['Genres'].str.contains(\"Children\")"
            if fan:
                ls=ls+"& gen['Genres'].str.contains(\"Fantasy\")"
            if cri:
                ls=ls+"& gen['Genres'].str.contains(\"Crime\")"
            if hor:
                ls=ls+"& gen['Genres'].str.contains(\"Horror\")"
            if mys:
                ls=ls+"& gen['Genres'].str.contains(\"Mystery\")"
            if im:
                ls=ls+"& gen['Genres'].str.contains(\"IMAX\")"
            if mus:
                ls=ls+"& gen['Genres'].str.contains(\"Musical\")"
            if wes:
                ls=ls+"& gen['Genres'].str.contains(\"Western\")"
            if fil:
                ls=ls+"& gen['Genres'].str.contains(\"Film-Noir\")"

                #with col2:

            exec("st.write(gen["+ls+"].sort_values(by=['rating'], ascending=False,ignore_index=True)[['Title']])")



    ls="True"
    if page_selection == "Movie Insights":
       #st.write('Detailed explanation of the movie')
       with st.form(key='searchform'):
           nav1,midn,nav2=st.columns([10,3,3])
           with nav1:
               search_term=st.text_input("Search Movie")
           with nav2:
               st.text(" ")
               st.text(" ")
               submit_search=st.form_submit_button(label='Search')
       if submit_search:
        st.success("You have searched for the movie **{}**.".format(search_term))
        ls=ls+"& mov['title'].str.contains(search_term)"
        exec("st.write(mov["+ls+"][['title','rating','genres','year','director','runtime','budget','title_cast']])")


    if page_selection == "Contact Us":
        st.write('Teams contact details here')


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
