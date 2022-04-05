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
    page_options = ["Home","About App","Exploratory Data Analysis","Recommender System", "Solution Overview"]

    #st.sidebar.image("default.png", use_column_width=True)
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

    if page_selection == "Home":
        st.title('Home')
        st.write('#')
        st.image('pictures/appname.png',use_column_width=True)

    if page_selection == "About App":
        st.title("TEQSPHERE by Rinae Apps")
        st.image('pictures/our_app.jpg',use_column_width=True)
        st.write("""Watching a movie is fun, but finding the next movie is a stressful experience. You scroll Netflix endlessly, watch trailers, wasting about an hour 
        but you still can't decide what to watch; ring a bell?. TEQSPHERE Recommendation system got you; it answers the "what to watch next?" question. Say goodbye to
         wasting time searching for what to watch next, and hello to TEQSPHERE movie recommendations that display only movies relevant to you.""")  
        st.write('#') 
        st.title('Why choose TEQSPHERE ?') 
        st.write(""" - Great User Interface; Unique, Appealing And Easy To Use""")
        st.write(""" - Fast Loading Time and High Performance.""")
        st.write(""" - TEQSPHERE asks the user to select three favourite movies, and then recommends ten movies similar to their favourite movies. """)
        st.write(""" - You choose your preferred recommendation method; content-based or collaborative-based. """)


    if page_selection == "Exploratory Data Analysis":
        st.title('Visualising Your Data')
        st.write('Data visualization gives us a clear idea of what the information means by giving it visual context through maps or graphs. This makes the data more natural for the human mind to comprehend and therefore makes it easier to identify trends, patterns, and outliers within large data sets.')
        st.write('### Distribution of Ratings per movie')
        st.write('#')
        st.image('pictures/tail.PNG',use_column_width=True)
        st.write('#')
        st.write('The plot plot shows the distribution of ratings/movie popularity with 653 popular movies and 45760 unpopular movies.')
        st.write('##')
        st.write('### Movie Ratings from the Users')
        st.write('#')
        st.image('pictures/Dis.JPG',use_column_width=True)
        st.write('#')
        st.write(""" 
        Most movies recieved ratings of 4, while others recieved less. It was expected that there would be a normal distrubtion with a mean rating of 3.
        Instead, we observe that users tend to rate movies quite favourably and tend to avoid negative ratings. This skew might be explained by the tendency
        of users to rate movies they liked.In other words, if a user doesn't like a movie, it is unlikely that they will watch it through to the end, let alone rate it.
        """)
        st.write('### Movie Genres')
        st.write('#')
        st.image('pictures/populargenres.jpeg')
        st.write('#')
        st.write("""Drama, Comedy and Action are top 3 most common movie genres. """)
        st.write('#')
        st.write('### Popular cast')
        st.write('#')
        st.image('pictures/popularcast.jpeg')
        st.write('#')
        st.write("""The most well-known cast members are Samuel L. Jackson and Steve Buscemi, with the remaining members having a slight variation in recognition.""")
        st.write('#')
        st.write('### Movie Runtime')
        st.write('#')
        st.image('pictures/longtail.jpeg',use_column_width=True)
        st.write('An average movie plays for 100 minutes.')
        st.write('### Top Tags')
        st.write('#')
        st.image('pictures/Toptags.JPG',use_column_width=True)
        st.write('#')
        st.write("""Sci-fi is the most popular tag while classic has the least number of counts. Science fiction movies have pioneered the development of artificial intelligence, science and technology in general.""")


    if page_selection == "Solution Overview":

        st.title("Solution Overview")
        st.write(""" After weighing on the differences between the collaborative filtering and content based filtering, the former approach wins. The criteria is not
        only based on the implementation.
        
        
Content-based filtering:
- Would not recommend products that have less content: if less information about a certain product, it would not be easy to find similar products for recommendations.
- Would not recommend popular products to users who have never used them. 

The collaborative filtering solves the novelty problem. The collaborative filtering is easy to implement. Similarities between the ratings that users give to certain products can be modelled
way better than in the content-based recommmender systems. We use the rating data with user information(movies they have seen and also the ratings given to those movies). The Singular Value Decomposition
is used to make the predictions on the ratings that a user would give to a movie they have never seen. Similarities are computed between the users, the same is computed for movie ratings. Ten most similar movies to the ones that the user likes will be recommended to the user.""")
        


    
if __name__ == '__main__':
    main()
