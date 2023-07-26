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
    page_options = ["Recommender System","Solution Overview","Movie Mate","About Us", "Exploratory Data Analysis"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "About Us":
        st.title("About Us")
        st.write("We are a team of data scientists passionate about recommendations systems.")
        st.write("Our goal is to provide the best Movie recommendatiosn for users across our platforms.")

        st.header("Team Members")
        # Create three columns
        col1, col2, col3 = st.columns(3)
        desc1, desc2, desc3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        desc4,desc5,desc6 = st.columns(3)

        # Place the images in separate columns
        col1.image("resources/aa.jpg", caption="Chief Data Scientist", width=200)
        col3.image("resources/sm.jpg", caption="Senior Developer", width=200)
        col2.image("resources/aag.jpg", caption="Chief Technical Officer", width=200)

        desc1.subheader("Abdulmalik Adeyemo")
        desc1.write("Abdulmalik is an experienced data scientist. He has a strong background in machine learning and deep learning.")

        desc2.subheader("Ayomide Aladetuyi")
        desc2.write("Ayomide is an experienced data analyst specializing in drawing insights from data. He has a strong background in Finance.")

        desc3.subheader("Setshaba Mashigo")
        desc3.write("Setshaba is an experienced data expert specializing in modelling. He has a strong background in Quality Assesment.")

        col4.image("resources/os.jpg", caption="Chief Administrative Officer", width=200)

        desc4.subheader("Olaniyi Samuel")
        desc4.write("Olaniyi is an experienced administrative specialist specialized in presenting amazing insights and presentations.")

        desc5.subheader("Seye Tare Garanwei")
        desc5.write("Seye is our Market researcher. He has a strong background in Market research.")


    if page_selection == "Exploratory Data Analysis":
        st.info("Exploratory Data Analysis")
        st.write("1. Movie ratings play a crucial role in guiding audiences' choices and determining a film's success or failure. Understanding the distribution of movie ratings is essential for filmmakers, studios, and critics alike. In this analysis, we delve into the distribution of movie ratings and uncover a fascinating trend that sheds light on user preferences and the overall positivity of the ratings landscape.")
        st.write("a. The majority of movies (1) receive ratings higher than the average, suggesting a favorable reception among audiences. This might be influenced by selection bias, leading to inflated ratings for well-received films.")
        st.write("b. Most frequently assigned ratings include 3.0, 4.0, and 5.0 (2), representing positive thresholds. High ratings near 5.0 indicate outstanding films that leave a lasting impression, influenced by social factors.")
        st.write("c. The left-skewed distribution of ratings (3) confirms the positive landscape, with fewer negative ratings. This could be due to users rating films they enjoyed and neglecting poorly received movies.")
        st.write("d. Users prefer whole numbers (4) over decimals when rating movies, possibly due to simplicity and the psychological impact of round numbers, making it easier to express their opinions")
        st.image('resources/imgs/eda1.png',use_column_width=True)

        st.write("2. In the dynamic world of movie ratings, understanding the trends across different time periods can provide valuable insights into audience preferences and cultural influences. In this analysis, we explore the quantity of ratings received by movies from different decades, with a particular focus on the 1990s. It is important to note that this study does not assess the sentiment or quality of the ratings; rather, it aims to highlight the popularity and enduring appeal of 90's movies based on the sheer number of ratings they have accumulated.")
        st.write("a. Movies from the 1990s receive the highest quantity of ratings, reflecting their lasting global impact.")
        st.write("b. The popularity of 90's movies stems from their cultural significance and nostalgia as cultural touchstones.")
        st.write("c. Accessibility through streaming platforms boosts ratings, as viewers easily discover and rate these classics.")
        st.write("d. 90's movies continue to captivate newer audiences, cementing their position as enduring rating favorites.")
        st.image('resources/imgs/eda2.png',use_column_width=True)

        st.write("3.The realm of cinema has continually captivated audiences with its ability to transport them to worlds filled with excitement, wonder, and thrill. Among the vast array of films, certain masterpieces rise above the rest, garnering accolades and admiration from critics and viewers alike. In this write-up, we delve into the highest-rated movies, with special focus on the top two films—parts I and II of Planet Earth—providing insights into their genres and the reasons behind their overwhelming success.")
        st.write("a. Common genres like action, adventure, and thriller dominate highly-rated movies, captivating audiences with adrenaline-pumping narratives and compelling storytelling. Understanding this preference is crucial for grasping cinematic appeal and the success of these captivating films.")
        st.write("b. Planet Earth parts I and IIs unparalleled success exemplifies the genres allure. With extraordinary efforts and visionary storytelling, the series showcases breathtaking landscapes and natures wonders, immersing audiences in Earths raw beauty and diverse ecosystems.")
        st.write("c. Action-Packed Adventure: The Planet Earth series is an action-packed adventure, immersing viewers in gripping encounters between predators and prey. Exploring remote and challenging terrains, the series captures heart-stopping moments, from breathtaking aerial chases to dramatic hunts, showcasing the raw survival instincts of Earth's inhabitants. Audiences are left on the edge of their seats, experiencing the thrill of the chase as if they were witnessing it firsthand.")
        st.write("d. Thrills in the Natural World: Planet Earth series delivers unparalleled thrills through intimate portrayals of the animal kingdom. Filmmakers capture rare footage of animals in their natural habitats, evoking empathy and awe as viewers witness the beauty and fragility of wildlife, leading to a deeper understanding of Earth's delicate ecological balance")
        st.image('resources/imgs/eda3.png',use_column_width=True)

        st.write("4.The genres of movies, when considered as an isolated feature, have minimal determining influence on the ratings they receive. This is evident from the comparable distributions observed in both the top 100 and bottom 100 rated movies. These movies exhibit similar genre compositions with similar frequencie.")
        st.write("a. Genres have minimal isolated influence on movie ratings. Analyzing top 100 and bottom 100 rated films shows similar genre distributions, suggesting specific genres don't guarantee high or low ratings. Other factors play a more significant role in determining a movie's success. The presence of genres alone doesn't define audience reception. Filmmakers should focus on storytelling, performances, direction, and production quality to impact ratings positively")
        st.write("b.The top 100 and bottom 100 rated movies have comparable genre compositions and frequencies. This indicates that genres alone don't heavily influence a film's reception. Other factors like storytelling, performances, direction, and production quality play a more significant role in determining audience response.")
        st.image('resources/imgs/eda4.png',use_column_width=True)



        # st.subheader("Data Cleaning")

    if page_selection == "Movie Mate":
        # Header contents
        st.write('# Movie Mate')
        st.write('### Team RR Movie Recommender Model ')
        st.image('resources/imgs/moviemate.PNG',use_column_width=True)
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
    if page_selection == "Solution Overview":
        st.title("Solution Overview")

        st.info(" Recommender systems play a vital role in todays technology-driven world. They are crucial for ensuring that individuals can make appropriate choices surrounding the content they engage with on a daily basis. A well-designed movie recommendation system can significantly enhance user experience and satisfaction. Especially with the recent surge in streaming platforms across the internet. Major streaming platforms like Netflix, Amazon Prime, Showmax, Disney, and others heavily rely on recommender systems to recommend content to their users. These platforms use intelligent algorithms to analyze user behavior, historical preferences, and movie ratings to curate personalized movie lists. By building a functional and accurate recommendation system, you can unlock immense economic potential. Users will be exposed to content that aligns with their tastes, increasing platform affinity and generating revenue through increased content consumption.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
