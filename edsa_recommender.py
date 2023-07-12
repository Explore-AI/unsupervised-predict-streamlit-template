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
    page_options = ["Recommender System","Solution Overview", "Latest Movie News", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        head, im = st.columns(2)
        head.title('DATA LENS ANALYTICS')
        im.image('resources/imgs/lens.jpeg', caption = 'See the Real-Time World Through our Eyes', width = 125)
        st.write('### Movie Recommender Engine')
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
    
    if page_selection == "Latest Movie News":
        st.title("Get The Latest Movie news")
        st.write('---')
		
        st.write("""Stay updated on matters relating to movie releases, actors,
        awards, financing. Never miss an update on upcoming movies and ticket releas dates to
        be the first on at the big screen. Know about your favourite films and movie stars with single click.

		"""
		)
        st.write('##')
        st.image("resources/imgs/news_img.jpg", width=600, caption=" Source: https://www.freepik.com/")
        st.write('---')
        st.write("""
		Click the button below to to get a round up of the latest news in Hollywood from around the web.
		 You can proceed to the news source by clicking the provided link to the article
		""")
        btn = st.button("Click to get latest movies related news")

        if btn:
            url ="https://newsapi.org/v2/everything?" 
            request_params = {
		    	"q": 'hollywood OR upcomming movies OR new movies OR hollywood actors',
				"sort by": "latest",
				"language": 'en',
				"apikey": "950fae5906d4465cb25932f4c5e1202c"
			}
            r = requests.get(url, request_params)
            r = r.json()
            articles = r['articles']

            for article in articles:
                st.header(article['title'])
                if article['author']:
                    st.write(f"Author: {article['author']}")
                st.write(f"Source: {article['source']['name']}")
                st.write(article['description'])
                st.write(f"link to article: {article['url']}")
                st.image(article['urlToImage'])
    
    if page_selection == "About Us":
        st.title("About Us")
        st.write("We are a team of Data Scientists and Engineers passionate about building efficient Machine Learning Models")
        st.write("Our goal is to provide accurate movie recommendations so as to provide the ultimate user experience")
        
        st.header("The Team")
        
        #create space for images and their descriptions
        col1, col2, col3 = st.columns(3)
        des1, des2, des3 = st.columns(3)
        col4, col5 = st.columns(2)
        des4, des5 = st.columns(2)
        
        col1.image('resources/imgs/Obinna.jpg', caption = "Data Engineer", width = 200)
        col2.image('resources/imgs/Mark.jpg', caption = "Data Scientist", width = 200)
        col3.image('resources/imgs/Salami.jpg', caption = "Data Scientist", width = 200)
        
        des1.subheader("Obinna Ekesi")
        des1.write("Obinna is our steadfast team leader and experienced data scientist. He has a strong background in Data analytics and Project Management.")

        des2.subheader("Mark Kasavuli")
        des2.write("Mark is an experienced data scientist and app developer. He has a strong background in Data science and Front-End App Development.")
        
        des3.subheader("Oluwaseyi Olanike Rachael")
        des3.write("Oluwaseyi is an experienced Project Coordinator and Data Enginner. She has background knowledge in Project Control and Data analytics.")

        col4.image('resources/imgs/Musa.jpg', caption = "Data Engineer", width = 200)
        col5.image()
        
        des4.subheader("Musa Aliu")
        des4.write("Musa is an experienced Data Engineer and pipeline developer. He has vast experience with Exploratory Data Analysis.")
        
        des5.subheader("Richard Sam")
        des5.write("Richard is an experienced Data Scientist. He as a strong background in Machine Learning Model Development and Deployment.")
        
        
if __name__ == '__main__':
    main()
