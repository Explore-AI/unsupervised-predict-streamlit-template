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
import streamlit as st
import joblib,os
from PIL import Image

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
    page_options = ["Recommender System","About", "Solution Overview", "About team 5"]

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
    if page_selection == "About":
        #Title
        st.title('About')
        st.write('--------------------------------------')
        #introduction
        st.markdown('INTRODUCTION')
        from PIL import Image
        movies = Image.open('resources/imgs/movies.PNG')
        st.image(movies, width=650)
        st.info("""Recommender Systems is a subclass of information filtering system that
                    seeks to predict the "rating" or "preference" a user would give
                    to an item. Recommender systems are used by companies
                    like Youtube, Netflix and Amazon for e-commerce and
                    online advertisement. They are very critical because
                    that is how many companies are able to generate money.
                    We have two types of recommender systems, content based
                    and collaborative fltering.
                    Collaborative methods for recommender systems are methods
                    that are based solely on the past interactions such as a user's
                    reaction which can be a Likert scale (0 - 5), recorded between
                    users and items in order to produce new recommendations.
                    Unlike collaborative methods that only rely on the user-item
                    interactions, content based approaches use additional information
                    about users and/or items such as their gender, location or age group.""")
        st.markdown('EXPLORATORY DATA ANALYSIS')
        from PIL import Image
        i = Image.open("resources/imgs/total_data.PNG")
        st.image(i)
        st.text("     ")
        st.markdown('USERS & RATINGS')
        st.write("""Users give a rating of movies they have watched, ratings are a scale from 0 to 5.
                   0 means the user did not like the movie and 5 means the user liked the movie a lot.
                   The ratings consist of decimal numbers and integers. It is clear that the rating
                   users usually give movies is 4.0 followed by 3.0""")
        rating = Image.open("resources/imgs/rating_dis.PNG")
        st.image(rating)
        st.info("""Integer values have taller bars than the floating values since most
                   of the users assign rating as integer value""")
        st.text("     ")
        from PIL import Image
        day_rating = Image.open("resources/imgs/l_rating.PNG")
        st.image(day_rating, caption='Average number of ratings per day')
        st.info("""We calcated the average rating for each day of the week
                   and we can see that we receive the most ratings on a Sunday and on a Saturday. The reason
                   could be that it's the weekend and people have time to watch movies.""")
        st.text("     ")
        from PIL import Image
        st.markdown('GENRES, TAGS & MOVIES')
        st.info("""Movie tags are a user's way of identifying movies for an example a user might
                   identify a movie as being funny or violent or a fantasy. A movie genre is
                   determined by the plot, character, story and setting of the movie eg: comedy or
                   musical. People like different genre of movies and that can be inflenced by their
                   age, gender or culture. Plot keywords are words that describe motifs, themes,
                   or plot details. Most are generic eg: murder or crying, some are clever and others
                   are oddly specific.""")
        bar_genre =Image.open("resources/imgs/l_genre.PNG")
        st.image(bar_genre, caption='Most common genres', width=650)
        st.info("""In the above histogram we can see that the Drama genre seems to be having the
                 most movies tags with a little over 25000 released movies followed by the Comedy
                 genre that has over over 15000 movies. This could possible mean that most ratings
                 are coming from these two genres as well.""")
        if st.button("Wordcloud for Tags"):
            from PIL import Image
            tag = Image.open('resources/imgs/tag_word.PNG')
            st.image(tag, caption='Most common tags', width=650)
        if st.button("Wordcloud for plot keywords"):
            from PIL import Image
            plot = Image.open('resources/imgs/plot.PNG')
            st.image(plot, caption='Most common plot keywords', width=650)
        st.text("      ")
        from PIL import Image
        movie_per = Image.open("resources/imgs/movie_per.PNG")
        st.image(movie_per, caption="Number of movies released per year", width=650)
        st.info("""Number of movies released per year increasing almost exponentially until 2010,
                 then flattening and dropping signifincantly in 2011. The numbers of movies produced
                 has been increasing with each year because of availability of resources and popular use
                 of technology that was not available during 1960s. Most movies heavily depend on the use
                 of technology and some of it was not available 40 or 30 years ago. """)
        st.text("      ")
        month =Image.open("resources/imgs/month.PNG")
        st.image(month, caption='Number of ratings each month')
        st.info("""The above graph is showing that most ratings are received from the month of September
                    up until November in a year, and then start decreasing in the month of December.
                    The decrease is not significant, but that is maybe because users are busy with holiday
                    commitments during that time. """)
        st.markdown("MOVIE RUNTIME")
        runtime = Image.open('resources/imgs/runtime.PNG')
        st.image(runtime, caption='Top 5 movies with longest runtime in minutes', width=650)
        st.text("      ")
        st.info("The longest movie in our dataset is Taken")
        st.text("     ")
        st.write('DIRECTORS')
        director = Image.open('resources/imgs/director.PNG')
        st.image(director, caption="Top 5 directors with most ratings", width=650)
        st.info("""The director with most ratings is Quentin Tarantino, the average rating on his movies
                 is 3.9""")


    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("The type of recommender system we choose to use is collaborative filtering.")
        st.info("""The measure of how well the model performs was defined by the RMSE score which is a value
                 between 1 and 0. It is used to measure the differences between values predicted by the
                 model and the values actually observed. The lower the RMSE, the more accurate the model""")
        st.info(""" Firstly, we used Principal Component Analysis which is a dimentionality reduction method
                that is often used to reduce the dimensionality of large data sets, by transforming a large
                set of variables into a smaller one that still contains most of the information in the large
                set. We used it with Random Forest and XGBoost. The RMSE score we were striving for was expected
                to be lower than 0.85""")
        st.markdown('RESULTS')
        from PIL import Image
        xg = Image.open('resources/imgs/xg.PNG')
        st.image(xg, caption='XGBoost RMSE score', width=650)
        st.text("      ")
        forest = Image.open('resources/imgs/forest.PNG')
        st.image(forest,caption="Random forest RMSE score", width=650)

    if page_selection =="About team 5":
        st.write('### Team 5')
        st.markdown("We build recommender systems")
        from PIL import Image
        team = Image.open("resources/imgs/team.PNG")
        st.image(team, width=650)
        st.info("""We help our clients discover and take advantage of the most essential
                   technology in the movie industry. We provide them with a system that has
                   two types of recommender methods, content based and collaborative filtering.
                   Recommender systems are critical because they aid companies to increase their
                   revenue income.""")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
