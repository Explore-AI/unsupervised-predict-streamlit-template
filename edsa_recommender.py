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
from sklearn.decomposition import TruncatedSVD
import streamlit as st
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv

# Data handling dependencies
import pandas as pd
import numpy as np
import codecs
from pandas_profiling import ProfileReport
from PIL import Image

# Custom Libraries
from utils.data_loader import (
    load_movie_titles, read_file, local_css, remote_css)
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from views import html_temp, html_overview, rec_header, sweet, prof, slides, team, eda_header

# Data Loading
title_list = load_movie_titles(
    'resources/data/movies.csv')


# ============ SweetViz Report =========================
def display_sweetviz(report_html, width=1000, height=500):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, width=width, height=height, scrolling=True)

# =========== Load CSS ======================


def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()),
                    unsafe_allow_html=True)


load_css("./utils/styles.css")

# ============ Load Icons ============================================


def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name),
                unsafe_allow_html=True)


# =====Load Images=======================================================
def load_image(file_name):
    img = Image.open(file_name)
    return st.image(img, width=300)
# ===========================================================================

# App declaration


def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["About Us", "Recommender System", "Data Overview", "Sweetviz",
                    "Exploratory Data Analysis", "Solution Overview", "Slides"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.markdown(rec_header, unsafe_allow_html=True)
        st.image('resources/imgs/Image_header.png', use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option', title_list[14930:15200])
        movie_2 = st.selectbox('Second Option', title_list[25055:25255])
        movie_3 = st.selectbox('Third Option', title_list[21100:21200])
        fav_movies = [movie_1, movie_2, movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i, j in enumerate(top_recommendations):
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
                    for i, j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    # -------------- Pandas Profiling -------------------------------------

    if page_selection == "Data Overview":
        st.markdown(prof, unsafe_allow_html=True)
        data_source = st.radio("Select Data Source",
                               ("movies data", "ratings data"))
        if data_source == "movies_data":
            data_file = "resources/data/movies.csv"
        else:
            data_file = "resources/data/ratings.csv"
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            profile = ProfileReport(df)
            st_profile_report(profile)
        pass
# ----------------------------|SweetViz Report----------------------

    if page_selection == "Sweetviz":
        st.markdown(sweet, unsafe_allow_html=True)
        data_source = st.radio("Select Data Source",
                               ("movies data", "ratings data"))
        if data_source == "movies_data":
            data_file = "resources/data/movies.csv"
        else:
            data_file = "resources/data/ratings.csv"
        if data_file is not None:
            df2 = pd.read_csv(data_file)
            st.dataframe(df2.head())
        if st.button("Generate SweetViz Report"):
            report = sv.analyze(df2)
            report.show_html()
            display_sweetviz("SWEETVIZ_REPORT.html")

# --------------------------------------------------------------------------
# ----------------------------Exploratory Data Analysis---------------------
    if page_selection == "Exploratory Data Analysis":
        # Ratings Grouped by Year
        st.markdown(eda_header, unsafe_allow_html=True)
        # components.html()

        # Movie release before 1995 and After
        if st.checkbox("Comparing Movie Release Periods"):
            st.image("resources/imgs/Movie_release_over_T.PNG")
            st.write("Period between 1995 to 2019 saw the production of 29,906 movies. In comparison\
            17,937 movies were produced from 1994 backwards to 1874. The sharp increase in movie production\
                can be attributed to advancements in technology and funding availability. A movie recommender system is key\
                    for users who have a large number of movies to select what to watch.")

        # components.html()

        # Ratings Frequency Per Year (Past 25 Years)
        if st.checkbox("Frequency of Ratings Per Year"):
            st.image("resources/imgs/dst.png")
            st.image("resources/imgs/dst1.PNG")
            st.image("resources/imgs/dst2.PNG")
            st.write("From 1995-2019,the most common rating is 4.0, which might mean only the users who loved the movie are likely to leave a rating.\
            The period between 1995 and 1999 did no have a very high number of ratings and a rating of 3.0 was the most popular.\
                The patterns in ratings in all the periods indicated in the graphs can be used to explain about patterns in movie development and user preferences.\
                    Interestingly, movie data can be used to infer so much about movie popularity, behavior of movie lovers and the likelihood of one rating a movie after watching.")

        if st.checkbox("Ratings Per Year"):
            st.image('resources/imgs/ratings_by_year.png')
            st.write("A substantial increase in movie ratings from 1995 to 1997 before dipping in 1998. The year 2000 and 2015 had some of the \
                highest number of ratings. It might be attributed to the release of very good movies and advancements in technology. Technology\
                    increases the reach and quality of movies. Recommender systems are a form of technology that are meant to make it easy for users\
                        to find movies to watch.")
        # components.html()

        if st.checkbox("Movie Release Decades"):
            st.image('resources/imgs/dc.png')
            st.write('The general view is that from the late 1800s the world has seen a steady increase in the numbers of movie released per year.\
                It can be attributed to economic growth, technological advancements and a rise in talents within the movie making industry.')
# --------------------------Slides----------------------------------
    if page_selection == "Slides":
        st.markdown(slides, unsafe_allow_html=True)

        # load_css('utils/icon.css')

# -----------------------------Solution Overview------------------

    if page_selection == "Solution Overview":
        st.markdown(html_temp, unsafe_allow_html=True)
        st.markdown(html_overview, unsafe_allow_html=True)


# ---------------------------Home-------------------------------
    if page_selection == "About Us":
        st.markdown(team, unsafe_allow_html=True)
        # components.html()

# You may want to add more sections here for aspects such as an EDA,
# or to provide your business pitch.


if __name__ == '__main__':
    main()
