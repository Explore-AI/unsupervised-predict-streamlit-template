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
    page_options = ["Recommender System","Explore Movies", "Solution Overview", "About Us", "Contact Us"]

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
    # Explore Movies  
    if page_selection == "Explore Movies":
        st.title("Explore Movies")

        search = st.text_input("Search for a movie")
        if st.button("Search"):
            if search:
                # Load the ratings and movies datasets
                ratings = pd.read_csv("resources/data/ratings.csv")
                movies = pd.read_csv("resources/data/movies.csv")

                # Merge the ratings and movies datasets on the movieId column
                merged_df = pd.merge(ratings, movies, on='movieId')

                # Group the merged dataset by movie title and calculate the average rating for each movie
                grouped_df = merged_df.groupby('title')['rating'].mean().reset_index()

                # Sort the grouped dataset by average rating in descending order
                sorted_df = grouped_df.sort_values(by='rating', ascending=False)

                # Perform fuzzy string matching on the movie titles to find close matches to the search input
                from fuzzywuzzy import fuzz
                from fuzzywuzzy import process

                close_matches = process.extract(search, sorted_df['title'], limit=5, scorer=fuzz.token_set_ratio)
                match_titles = [match[0] for match in close_matches]

                # Select the matching movie titles and their corresponding ratings from the sorted dataset
                match_df = sorted_df[sorted_df['title'].isin(match_titles)]

                match_df = match_df.sort_values(by='rating', ascending=False)

                st.write("Search Results:")
                for i, row in match_df.iterrows():
                    st.write(f"{i+1}. {row['title']} (Rating: {row['rating']:.2f})")
            else:
                st.write("Search input is empty. Please enter a movie name to search.")
            st.markdown("# ")
            st.markdown("# ")


        # Read in the ratings and movies datasets
        ratings = pd.read_csv("resources/data/ratings.csv")
        movies = pd.read_csv("resources/data/movies.csv")

        # Merge the ratings and movies datasets on the movieId column
        merged_df = pd.merge(ratings, movies, on='movieId')

        # Group the merged dataset by movie title and calculate the average rating for each movie
        grouped_df = merged_df.groupby('title')['rating'].mean().reset_index()

        # Sort the grouped dataset by average rating in descending order and select the top 10 movies
        top_rated_movies = grouped_df.sort_values(by='rating', ascending=False).head(10)

        st.markdown("### Top Rated Movies")

        # Create a horizontal row to display the top-rated movies
       
        for i, movie in enumerate(top_rated_movies['title']):
            st.write(f"{i+1}. {movie}")
    
        # Find the 10 hottest movies (i.e., most highly rated in the latest 1,000 records) based on timestamp
        hottest_df = merged_df.sort_values(by='timestamp', ascending=False).head(1000)
        hottest_df = hottest_df.groupby('title')['rating'].mean().reset_index()
        hottest_df = hottest_df.sort_values(by='rating', ascending=False).head(10)
        st.markdown("# ")
        st.markdown("# ")

        st.markdown("### What People Are Liking Right Now")
        for i, row in enumerate(hottest_df.itertuples(), start=1):
            st.write(f"{i}. {row.title} (Rating: {row.rating:.2f})")


    # Solution Overview
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Our movie recommender system uses a content-based and collaborative-based filtering approaches to recommend movies to users. The system takes in a user's input of a movie title, processes the data using the cosine similarity algorithm, and then recommends the top 10 most similar movies based on the user's input.")
        st.markdown("""
    Before building the recommendation model, we conducted an extensive Exploratory Data Analysis (EDA) on a dataset of movies. 
    During the EDA, we cleaned and preprocessed the data, and performed various visualizations to understand the distribution and relationships of the features in the dataset.
    """)

        st.markdown("""
    Based on the insights gained from the EDA, we identified the important features that would be used as inputs for the recommendation model.
    These features include the movie's **genres, plot keywords, cast, directors and ratings**. By using these features, the model is able to understand the user's preferences and make recommendations that are tailored to their interests or interests of someone similar.
    """)
        st.markdown(""" Here are some key insights we drew from our EDA:""")
        
        st.markdown("- The majority of movies in our dataset are rated as 'average' by critics, with only a small percentage being highly rated or poorly rated.")
        st.markdown("- The majority of movies are English-language films, but there is a significant number of foreign-language films as well.")
        st.markdown("- Action and Adventure are the most popular genres in our dataset, followed by Comedy and Thriller.")
        st.markdown("- The majority of movies in our dataset have a runtime of between 90-120 minutes.")
        st.markdown("- There is a positive correlation between the budget of a movie and its revenue.")    
        st.markdown("""The solution was designed and developed by the team of **MovieGenius** company.""")     
        
        # About Us
    if page_selection == "About Us":
        st.header("About Us")
        st.write("Our team consists of experienced data scientists and engineers who are passionate about using technology to enhance the movie-watching experience. We at Movie Magic Inc. strive to provide the best movie recommendations to our users by constantly updating and improving our model.")
        
        st.write("Our team members:")
        st.write("- Malik Kabir, Team Lead")
        st.write("- Mariam M'mbetsa, Machine Learning Engineer")
        st.write("- Mahlatse Motlanthi, Data Scientist")
        st.write("- Haruna Jibrin, Data Analyst")
        st.write("- Babajide Adelekan, Business Analyst")
        st.write("- Ncedo Fakude, Business Analyst II")
        
        st.write("Our movie recommendation system is based on a state-of-the-art content-based filtering algorithm. This approach takes into account the features of the movie such as the cast, crew, plot, and keywords to provide personalized and accurate recommendations.")
        st.write("We have a vast movie database that is constantly updated to ensure that you always have access to the latest releases and hidden gems.")
        st.write("In addition, we offer a user-friendly web interface that allows you to easily search for movies and view our top recommendations.")
        st.markdown("""
    Feel free to **Contact Us** for any further information.
    """)

        st.success("Exploratory Data Analysis (EDA)")
        st.info("- Cleaning and preprocessing of the data")
        st.info("- Understanding distribution and relationships of the features in the dataset")
        st.info("- Identifying important features to be used as inputs for the recommendation model")

        #st.image('/unsupervised/unsupervised-predict-streamlit-template/resources/imgs/eda.jpg', width=600)
        st.write("Thank you for choosing MovieGenius for alla your movie recommendation needs!")
        
        # Contact Us
    if page_selection == "Contact Us":
        st.header("Contact Us")
        st.write("We would love to hear from you!")
        st.write("Email us at contact@moviegenius.com")
        st.write("Follow us on social media:")
        st.write("Twitter: @moviegenius")
        st.write("Facebook: /moviegenius")
        st.write("Instagram: @moviegenius")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
