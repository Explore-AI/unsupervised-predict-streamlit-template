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
    page_options = ["Home Page","Recommender System","Data & Insights",
                    "Solution Overview", "Exploratory Data Analysis","About Us"]

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

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------

    profiles_html = """
	<div class="container marketing">
        <div class="row">
          <div class="col-lg-4">
            <img class="rounded-circle" src="https://media-exp1.licdn.com/dms/image/C4D03AQE_hQfcylm9fg/profile-displayphoto-shrink_400_400/0?e=1600300800&v=beta&t=6IJmdWzXTldtb-hlKiyZM-CYFtS2XxBMCygInueQF3g" alt="Profile Pic" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/akshar-jadoonandan/">Akshar Jadoonandan</a></h3>
            <p><li>Lead Data Scientist</li><li>Machine Learning</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img class="rounded-circle" src="https://avatars3.githubusercontent.com/u/60362470?s=400&v=4" alt="Generic placeholder image" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/azukile-kobe-a22297183/">Azukile Kobe</a></h3>
            <p><li>Data Scientist</li><li>Machine Learning</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
          <div class="col-lg-4">
            <img class="rounded-circle" src="https://avatars3.githubusercontent.com/u/60362470?s=400&v=4" alt="Generic placeholder image" width="140" height="140">
            <h3>Sandile Dladla</h3>
            <p><li>Data Engineer</li><li>Research</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
	  <div class="col-lg-4">
            <img class="rounded-circle" src="https://media-exp1.licdn.com/dms/image/C5603AQFQg17f1NUnhw/profile-displayphoto-shrink_400_400/0?e=1600300800&v=beta&t=WzfozWzixxm2Gb4tmszxCCpNRQ8rlVdqeauvIqEQsTA" alt="Generic placeholder image" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/sibonelo-junior-malakiya/">Sibonelo Malakiya Jr</a></h3>
            <p><li>Data Scientist</li><li>Big Data Engineer</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
	  <div class="col-lg-4">
            <img class="rounded-circle" src="https://media-exp1.licdn.com/dms/image/C4D03AQFd-pzyq0Gg1A/profile-displayphoto-shrink_400_400/0?e=1600300800&v=beta&t=NNVu04JF0uIofiJ9UmtRexDql47EUr9i0OD_tZtOUzE" alt="Generic placeholder image" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/sizwe-ncube-a6b85b8a/">Sizwe Ncube</a></h3>
            <p><li>Data Scientist</li><li>Web Dev</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
	  <div class="col-lg-4">
            <img class="rounded-circle" src="https://media-exp1.licdn.com/dms/image/C4D03AQGlQuKN7vSm7A/profile-displayphoto-shrink_400_400/0?e=1600300800&v=beta&t=OaP37Ya-P_N0aD6tcrMan6Temqvs_dQoU83qdG7NJXE" alt="Generic placeholder image" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/lizwi-khanyile/">Lizwi Khanyile</a></h3>
            <p><li>Data Scientist</li><li>Web Dev</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
        </div><!-- /.row -->
</div>
    
    """
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    if page_selection == "Home Page":
        st.title("")
        html_temp = """
        <div style="background-color:yellow;padding:10px">
        <h2 style="color:red;text-align:center;">Popcorn Plug</h2>
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)
        st.header('')
        # st.write("<p style='text-align: left; color: red;'>Make entertainment exciting, again.🔥</p>", unsafe_allow_html=True) 
        st.write("### Welcome to our Machine Learning Movie Recommender App") 
        st.write("The app uses machine learning models to recommend best movies to our users")

        st.write("________________________________________________________________________________")
        # st.write("### Popcorn Plug ")
        # st.write("<p style='text-align: left; color: red;'>Make entertainment exciting, again.🔥</p>", unsafe_allow_html=True) 
        st.image('https://media0.giphy.com/media/dXQlx5RfbNwQVtqMet/giphy.gif?cid=6c09b9526ae25bf2202fbb861880e79c9c35b42b1257517b&rid=giphy.gif',use_column_width=True)
        st.write("________________________________________________________________________________")
        
        st.write("<p style='text-align: center; color: red;'>Find out what to watch next!.</p>", unsafe_allow_html=True) 

    if page_selection == "Data & Insights":
        st.title("Movie Recommender Engine")

        st.write("### Below are some visuals, and insights gained from the data") 
        # st.write("The app uses machine learning models to recommend best movies to our users") 
        
        # st.image('https://media0.giphy.com/media/dXQlx5RfbNwQVtqMet/giphy.gif?cid=6c09b9526ae25bf2202fbb861880e79c9c35b42b1257517b&rid=giphy.gif',use_column_width=True)


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "Exploratory Data Analysis":
        st.title("Exploratory Data Analysis")
        st.write("EDA HERE")


    # About us page
    if page_selection == "About Us":
        html_temp = """
        <div style="background-color:yellow;padding:10px">
        <h2 style="color:red;text-align:center;">Meet the team</h2>
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)
        st.header('')
        st.markdown(profiles_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
