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

# image
from PIL import Image

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Solution Overview", "About Us"]
    st.sidebar.write("## Autonomous Insights")
    image = Image.open("./resources/imgs/logo-bg.png")
    st.sidebar.image(image, width=200)
    

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.write('#### We give you best movie recommendations')
        st.write('#### Select one the algorithms andyour three favorite movies to get recommendations')
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
        # st.write("Describe your winning approach on this page")
        st.write("### Problem Statement")
        st.write("The world of movies is vast and diverse, with countless options available to movie enthusiasts. However, with such a vast selection, finding the perfect movie that aligns with individual preferences can be an overwhelming and time-consuming task. Movie recommendation systems have attempted to address this issue, but many of them fall short, providing generic and inaccurate suggestions that do not resonate with users.")
        st.write("## Our Winning Approach")
        st.write("At Autonomous Insights, we have taken up the challenge to create a movie recommendation system that stands apart from the rest. Our winning approach combines cutting-edge technology, innovative algorithms, and a passion for cinema to deliver an unparalleled movie-watching experience.")
        st.write("## Advanced Machine Learning Techniques")
        st.write("Our movie recommender system leverages the power of advanced machine learning techniques to analyze vast amounts of movie-related data. By employing collaborative filtering, we identify patterns in users' viewing habits to suggest movies that others with similar tastes have enjoyed. Additionally, our content-based filtering algorithms analyze movie attributes to recommend films based on thematic similarities.")
        st.write("### Insight:")
        st.write("By utilizing collaborative filtering, we tap into collective wisdom, understanding that users with similar movie preferences often discover hidden gems that resonate with their tastes. Content-based filtering ensures that recommendations are not solely reliant on others' preferences but also take into account specific movie attributes that users enjoy.")
        st.write("## Hybrid Recommendation System")
        # st.write("## Contact Us")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    if page_selection == "About Us":
        st.write("## Our Vision")
        st.write("At Autonomous Insights, we are driven by a singular vision:to enhance your movie-watching experience by delivering personalized and accurate movie recommendations. We believe that every individual should have access to a seamless and delightful movie selection process, tailored to their unique tastes and preferences.")
        st.write("## Who We Are")
        st.write("Autonomous Insights is a passionate team of movie enthusiasts, data scientists, and AI experts dedicated to revolutionizing how you discover and enjoy movies. With a deep love for cinema and a profound understanding of artificial intelligence, we strive to bring you the ultimate movie recommendation platform.")
        st.write("## Our Technology")
        st.write("Our cutting-edge movie recommender system is powered by state-of-the-art machine learning algorithms and sophisticated deep learning models. We have meticulously curated and analyzed vast amounts of movie data to build an intelligent system that goes beyond generic recommendations.")
        st.write("## How It Works")
        st.write("Our web app, built on the powerful Streamlit framework, provides an intuitive and user-friendly interface. It employs a blend of collaborative filtering, content-based filtering, and hybrid recommendation techniques to offer you personalized movie suggestions that align perfectly with your tastes.")
        st.write("## Your Movie Journey")
        st.write("At Autonomous Insights, we are committed to being your loyal movie companion throughout your cinematic journey. Whether you are a casual moviegoer or an avid cinephile, our system adapts and evolves with your changing preferences, ensuring that every movie you watch is a delightful experience.")
        st.write("## Privacy and Security")
        st.write("We prioritize your privacy and data security above all else. Rest assured that your personal information and viewing history are encrypted and protected. We never share your data with third parties, and you have full control over your account settings.")
        st.write("## Join Us Today")
        st.write("Embark on a new adventure in cinema with Autonomous Insights. Sign up now and discover a world of movies tailored exclusively for you. Let us empower you with insightful movie recommendations and make your movie nights truly extraordinary.")
        

        st.subheader("The Team")
        # Team images
        harmony = Image.open("resources/imgs/Team/harmony.png")
        emanuel = Image.open("resources/imgs/Team/emanuel.jpg")
        kgopotso = Image.open("resources/imgs/Team/kgopotso.jpg")
        lehlohonono = Image.open("resources/imgs/Team/lehlohonono.jpg")
        ndumiso = Image.open("resources/imgs/Team/ndumiso.jpg")
        phindulo = Image.open("resources/imgs/Team/phindulo.jpg")
        precious = Image.open("resources/imgs/Team/precious.jpg")
        yvonne = Image.open("resources/imgs/Team/yvonne.jpg")

        col1 ,col2, col3 = st.columns(3)

        with col1:
            st.image(phindulo,use_column_width=False, clamp=False, width = 150, output_format="JPEG")
        with col2:
            st.image(harmony, use_column_width=False, clamp=True, width=150, output_format="JPEG")
        with col3:
            st.image(lehlohonono, use_column_width=False, clamp=False, width=150, output_format="JPEG")
            
        col4, col5, col6 = st.columns(3)
        
        with col4:
            st.write("Data Scientist")
            st.write("Ndumiso Nkosi")
            st.write("NdumisoNkosi@autiinsights.com")
        with col5:
            st.write("Machine Learning Engineer")
            st.write("Emmanuel Nkosi")
            st.write("EmmanuelNkosi@autiinsights.com")
        with col6:
            st.write("Data Engineer")
            st.write("Kgopotso Tlaka")
            st.write("KgopotsoTlaka@autiinsights.com")
            
        col7, col8, col9 = st.columns(3)

        with col7:
            st.image(ndumiso, use_column_width=False, clamp=True, width=150, output_format="JPEG")
        with col8:
            st.image(emanuel, use_column_width=False, clamp=True, width=150, output_format="JPEG")
        with col9:
            st.image(kgopotso, use_column_width=False, clamp=True, width=150, output_format="JPEG")
            
        col10, col11, col12 = st.columns(3)
        
        with col10:
            st.write("Data Scientist")
            st.write("Ndumiso Nkosi")
            st.write("NdumisoNkosi@autiinsights.com")
        with col11:
            st.write("Machine Learning Engineer")
            st.write("Emmanuel Nkosi")
            st.write("EmmanuelNkosi@autiinsights.com")
        with col12:
            st.write("Data Engineer")
            st.write("Kgopotso Tlaka")
            st.write("KgopotsoTlaka@autiinsights.com")
        
        col13, col14 = st.columns(2)
        
        with col13:    
            st.image(yvonne, use_column_width=False, clamp=True, width=150, output_format="JPEG")
            
        with col14:    
            st.image(precious, use_column_width=False, clamp=True, width=150, output_format="JPEG")
            
        col15, col16 = st.columns(2)
        
        with col15:
            st.write("Data Analyst")
            st.write("Yvonne Malinga")
            st.write("YvonneMalinga@autiinsights.com")
            
        with col16:
            st.write("Data Analyst")
            st.write("Lesego Precious Sefike")
            st.write("LesegoPrecious @autiinsights.com")

        import os
        print(os.path.abspath("resources/imgs/EDSA_logo.png"))
        print(os.path.abspath("resources/imgs/EDSA_logo.png"))
        print(os.path.abspath("resources/imgs/EDSA_logo.png"))

        st.write("## Contact Us")
        st.write("For inquiries or assistance, reach out to us at contact@autonomousinsights.com. We are open for business")
        

        st.write("Our website - autonomousinsights.com")


if __name__ == '__main__':
    main()
