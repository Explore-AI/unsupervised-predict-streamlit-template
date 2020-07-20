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
from PIL import Image,ImageFilter,ImageEnhance
import os
import cufflinks as cf
from plotly.offline import init_notebook_mode, iplot



# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
rating = 'resources/data/ratings.csv'
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","Recommender System","Data & Insights",
                    "Solution Overview", "About Us"]

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
            <img class="rounded-circle" src="https://media-exp1.licdn.com/dms/image/C4D03AQHcahIyvHWPyg/profile-displayphoto-shrink_400_400/0?e=1600905600&v=beta&t=6cWqGknK3vmpQgAHEQ5D7nKF8hwAC5pSShFRCyeQinE" alt="Generic placeholder image" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/sandile-dladla/">Sandile Dladla Jr</a></h3>
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
            <p><li>Data Scientist</li><li>App Dev</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
	  <div class="col-lg-4">
            <img class="rounded-circle" src="https://media-exp1.licdn.com/dms/image/C4D03AQGlQuKN7vSm7A/profile-displayphoto-shrink_400_400/0?e=1600300800&v=beta&t=OaP37Ya-P_N0aD6tcrMan6Temqvs_dQoU83qdG7NJXE" alt="Generic placeholder image" width="140" height="140">
            <h3><a href="https://www.linkedin.com/in/lizwi-khanyile/">Lizwi Khanyile</a></h3>
            <p><li>Data Scientist</li><li>App Dev</li></ul></p>
            <div class="col-sm-5 col-md-4 col-lg-3 social-links text-center">
            <ul class="list-inline mt-5">
            </ul>
            </div>
          </div><!-- /.col-lg-4 -->
        </div><!-- /.row -->
</div>
    
    """
    if page_selection == "Solution Overview":
        html_temp = """
        <div style="background-color:black;padding:10px">
        <h2 style="color:yellow;text-align:center;">Solution Overview</h2>
        </div>"""
        
        st.markdown(html_temp,unsafe_allow_html=True)
    
    # Home Page
    if page_selection == "Welcome":
        st.title("")
        html_temp = """
        <div style="background-color:black;padding:10px">
        <h2 style="color:yellow;text-align:center;">🔥POPCORN PLUG🔥</h2>
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)
        st.header('') 
        st.markdown('Welcome to the **Popcorn Plug**, The days of searching for the perfect movie to watch are over!!!' \
                    ' We know **exactly** which movies you want to watch. So **sit back**, **Plug in** and press **PLAY**.')
        st.image('https://media.giphy.com/media/fwtbN85BvsXknut34x/giphy.gif' , width = 695)
        st.write("________________________________________________________________________________")
    
    # Exploratory Data Analysis Page
    if page_selection == "Data & Insights":
        html_temp = """
        <div style="background-color:black;padding:10px">
        <h2 style="color:yellow;text-align:center;">Exploratory Data Analysis</h2>
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)

        st.write("### Below is the data, some visuals, and insights gained from the data") 
        st.write('')

        #To Improve speed and cache data
        @st.cache(persist=True)
        def explore_data(dataset):
            df = pd.read_csv(os.path.join(dataset))
            return df 

        # Load Our Dataset
        data = explore_data(rating)

        # Show Entire Dataframe
        insights = ['Raw Data','Descriptive Statistics','Movie Rating']
        selection_info = st.selectbox("Select page", insights)

        if selection_info == "Raw Data":
            st.markdown("""
            ### About the data set
            + The data we used for the model is the train set - (train.csv), which contains all movie ratings.
            + Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).
            + Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.

            """)
            st.dataframe(data)
            # Show Dataset
            if st.checkbox("Preview DataFrame Head or Tail"):
                if st.button("Head"):
                    st.write(data.head())
                elif st.button("Tail"):
                    st.write(data.tail())
        
        if selection_info == "Descriptive Statistics":
            st.markdown("""
            ### Descriptive Statistics.
            + Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.

            """)
            st.dataframe(data.describe().T)

            if st.checkbox("UserId Plot"):
                data.userId.plot(kind='box')
                st.pyplot()
                st.markdown("""
            ### Insights.
            + The data seems to be well distributed for the userId column.
            """)
            elif st.checkbox("MovieId Plot"):
                data.movieId.plot(kind='box')
                st.pyplot()
                st.markdown("""
            ### Insights.
            + The mean is higher than the median, that shows us that we have major outliers in the high end of the data, you can see on the plot
            """)
            elif st.checkbox("Rating Plot"):
                data.rating.plot(kind='box')
                st.pyplot()
                st.markdown("""
            ### Insights.
            + The mean is lower than the median, showings that we have outliers in the lower end of the data, you can see on the plot
            """)

        if selection_info == "Movie Rating":
            st.markdown("### Movie Rating")
            data.rating.value_counts().plot(kind='bar',color='gold')
            st.pyplot()
            st.markdown("""
            ### Insights.
            + The most frequent rating is 4.0
            + The least frequent rating is 0.5
            + The mean rating is 3.5
            + There are no 0 ratings in the dataset.
            """)
        



        # st.write("The app uses machine learning models to recommend best movies to our users") 
        
        # st.image('https://media0.giphy.com/media/dXQlx5RfbNwQVtqMet/giphy.gif?cid=6c09b9526ae25bf2202fbb861880e79c9c35b42b1257517b&rid=giphy.gif',use_column_width=True)


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    # if page_selection == "Exploratory Data Analysis":
    #     st.title("Exploratory Data Analysis")
    #     st.write("EDA HERE")


    # About us page
    if page_selection == "About Us":
        html_temp = """
        <div style="background-color:black;padding:10px">
        <h2 style="color:yellow;text-align:center;">Meet the team</h2>
        </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)
        st.header('')
        st.markdown(profiles_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
